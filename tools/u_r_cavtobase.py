#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

import aiohttp, asyncio
import json, time
import xlrd, re

NAME_MATCH = re.compile(r'^[a-zA-Z][\w\W]*\.$')

COLUM_FAMILY = ['author' , 'title' , 'year' , 'orginal_publication' , 'volume' , 'issue' , 'paper_id' , 'start_page' , 'end_page' , 'page_counter' , 'citing_paper' , 'doi' , 'url' , 'institution_owner' , 'author_with_institution' , 'summary' , 'author_keyword' , 'index_keyword' , 'analysis_serial_number' , 'cas' , 'brand' , 'manufacturer' , 'funding_info' , 'references' , 'postal_addr' , 'editor' , 'funding_agent' , 'publisher' , 'conference_name' , 'conference_date' , 'conference_location' , 'conference_code' , 'issn' , 'isbn' , 'coden' , 'pubmed_id' , 'language' , 'orginal_publication_abbr' , 'paper_type' , 'source_of_publication' , 'eid']

#DB_HOST = '1.85.37.132'
DB_HOST = 'localhost'
ROUTE = r'u_r_/uansr_1.xlsx'

async def uansr_data(client, data, headers):

	'''
		operations related to 'u_r_university' table
	'''
	university_id = ''
	author_id = ''
	literature_id = ''

	UNIVERSITY_NAME = 'Moscow Power Engineering Institute'
	UNIVERSITY_ALIAS_NAME = ['power', 'mpei']

	u_params = {'table': 'u_r_university', 'name': UNIVERSITY_NAME}	
	university_json = None
	try:
		get_university = await client.get('http://' + DB_HOST + '/api/u_r_/items', params = u_params)

		assert get_university.status == 200, 'connection error!'

		has_university = await get_university.text()
		university_json = json.loads(has_university)['data']
		await get_university.release()
	except Exception as e:
		await get_university.release()
		return

	need_university_constructed = False
	if university_json is not None:
		if len(university_json) != 0:
			university_id = university_json[0]['id']
		else:
			need_university_constructed = True
	else:
		need_university_constructed = True

	if need_university_constructed:
		item_university = {}
		data_university = {}

		item_university['name'] = UNIVERSITY_NAME
		item_university['alias'] = str(UNIVERSITY_ALIAS_NAME)

		data_university['item'] = item_university
		data_university['table'] = 'u_r_university'
		try:
			r_university = await client.post('http://' + DB_HOST + '/api/u_r_/items', data=json.dumps(data_university), headers = headers)

			assert r_university.status == 200, 'connection error!'

			res_university = await r_university.content.readany()
			university_id = res_university.decode()
			await r_university.release()
			if university_id.startswith('<!'):
				return
		except Exception as e:
			await r_university.release()
			return

	'''
		iterator operations for data item
	'''
	for item in data['items']:

		'''
			extract name lists and affiliation lists from the item
		'''
		name_list = []
		affiliation_list = []
		if isinstance(item['author'], str) and item['author'] != '':
			name_list = item['author'].split(',')
			print(name_list)
		else:
			continue
		item.pop('author')

		if isinstance(item['author_with_institution'], str) and item['author_with_institution'] != '':
			affiliation_list = item['author_with_institution'].split(';')
			print(affiliation_list)
		else:
			continue
		item.pop('author_with_institution')

		'''
			handle the error format data item
		'''
		if len(name_list) != len(affiliation_list):
			continue

		'''
			operations related to 'u_r_coference' table
		'''
		item_conf = {}
		data_conf = {}
		if item['conference_name'] == '':
			item['conference_name'] = time.time()

		c_params = {'table': 'u_r_conference', 'name': item['conference_name']}	
		conference_json = None
		try:
			get_conference = await client.get('http://' + DB_HOST + '/api/u_r_/items', params = c_params)

			assert get_conference.status == 200, 'connection error!'

			has_conference = await get_conference.text()
			conference_json = json.loads(has_conference)['data']
			await get_conference.release()
		except Exception as e:
			await get_conference.release()
			continue

		need_constructed = False
		need_constructed_m = []
		need_constructed_m_final = 0
		
		if conference_json is not None:
			if len(conference_json) != 0:
				need_constructed_m_final = 1
				for i in range(len(conference_json)):
					need_constructed_m.append(False)
				j_ = 0
				for j in conference_json:
					if j['name'] != item['conference_name']:
						need_constructed_m[j_] = True
					j_ = j_ + 1;
			else:
				need_constructed = True
		else:
			need_constructed = True

		for p in need_constructed_m:
			need_constructed_m_final = need_constructed_m_final * p	

		if need_constructed or need_constructed_m_final:
			item_conf['name'] = item['conference_name']
			item_conf['date'] = item['conference_date']
			item_conf['location'] = item['conference_location']
			item_conf['code'] = item['conference_code']

			data_conf['item'] = item_conf
			data_conf['table'] = 'u_r_conference'
			try:
				r_conf = await client.post('http://' + DB_HOST + '/api/u_r_/items', data=json.dumps(data_conf), headers = headers)

				assert r_conf.status == 200, 'connection error!'

				await r_conf.release()
			except Exception as e:
				await r_conf.release()
				continue

		'''
			operations related to 'u_r_literature' table
		'''
		item.pop('institution_owner')
		item.pop('conference_date')
		item.pop('conference_location')
		item.pop('conference_code')

		item['u_id'] = university_id

		data_literature = {}
		data_literature['item'] = item
		data_literature['table'] = 'u_r_literature'
		try:
			r_literature = await client.post('http://' + DB_HOST + '/api/u_r_/items', data=json.dumps(data_literature), headers = headers)

			assert r_literature.status == 200, 'connection error!'

			res_literature = await r_literature.content.readany()

			literature_id = res_literature.decode()
			await r_literature.release()
			if literature_id.startswith('<!'):
				continue
		except Exception as e:
			await r_literature.release()
			continue

		'''
			operations related to 'u_r_author' and 'u_r_written_by' and 'u_r_affiliated_with' tables
		'''
		r = 0
		for a_name in name_list:

			'''
				extract the author and the corresponding affiliation
			'''
			author_name = a_name.strip()
			author_affiliation = ''

			author_alias = author_name.replace(' ', ', ')
			print('@author name is : %s' % author_name)
			if NAME_MATCH.match(author_name):
				pass
			else:
				continue
			try:
				affiliation_t = affiliation_list[r]
				r = r + 1
				if affiliation_t.find(author_alias) == -1:
					continue
				start = affiliation_t.find(author_alias) + len(author_alias) + 1
				author_affiliation_ = affiliation_t[start:].strip()

				has_u_alias_names = []
				for u_alias_name in UNIVERSITY_ALIAS_NAME:
					if author_affiliation_.lower().find(u_alias_name.lower()) != -1:
						has_u_alias_names.append(True)
					else:
						has_u_alias_names.append(False)
				has_u_alias_names_final = 0
				for has_u_alias_name in has_u_alias_names:
					has_u_alias_names_final = has_u_alias_names_final or has_u_alias_name

				if author_affiliation_.lower().find(UNIVERSITY_NAME.lower()) != -1 or has_u_alias_names_final:
					author_affiliation = UNIVERSITY_NAME
				else:
					author_affiliation = '_others: ' + author_affiliation_
				print('@affiliation is : %s' % author_affiliation)
			except Exception as e:
				author_affiliation = '_others: ' + author_affiliation_

			'''
				operations related to 'u_r_author' table
			'''
			'''
			if author_affiliation == UNIVERSITY_NAME:
				params = {'table': 'u_r_author', 'alias': author_alias.lower(), 'affiliation': author_affiliation}
			else:
				params = {'table': 'u_r_author', 'alias': author_alias.lower(), 'affiliation': '_others:'}
			'''
			params = {'table': 'u_r_author', 'alias': author_alias.lower(), 'affiliation': author_affiliation}
			author_json = None
			try:
				get_author = await client.get('http://' + DB_HOST + '/api/u_r_/items', params = params)
				assert get_author.status == 200, 'connection error!'

				has_author = await get_author.text()
				author_json_ = json.loads(has_author)
				author_json = author_json_['data']
				await get_author.release()
			except Exception as e:
				await get_author.release()
				continue

			judge_author_find = False
			need_author_constructed = False
			if author_json is not None:
				if len(author_json) != 0:
					author_id = author_json[0]['id']
					judge_author_find = True
				else:
					need_author_constructed = True
			else:
				need_author_constructed = True

			if need_author_constructed:
				item_author = {}
				data_author = {}

				item_author['name'] = author_name
				item_author['alias'] = author_alias.lower()
				item_author['affiliation'] = author_affiliation

				data_author['item'] = item_author
				data_author['table'] = 'u_r_author'
				try:
					r_author = await client.post('http://' + DB_HOST + '/api/u_r_/items', data=json.dumps(data_author), headers = headers)

					assert r_author.status == 200, 'connection error!'

					res_author = await r_author.content.readany()
					author_id = res_author.decode()
					await r_author.release()
					if author_id.startswith('<!'):
						continue
				except Exception as e:
					await r_author.release()
					continue

			print('#author_id is : %s' % author_id)
			print('#university_id is : %s' % university_id)
			print('#literature_id is : %s' % literature_id)

			'''
				operations related to 'u_r_affiliated_with' table
			'''
			if author_affiliation == UNIVERSITY_NAME:

				if judge_author_find:
					pass
				else:
					item_affiliated_with = {}
					data_affiliated_with = {}

					item_affiliated_with['author_id'] = author_id
					item_affiliated_with['university_id'] = university_id

					data_affiliated_with['item'] = item_affiliated_with
					data_affiliated_with['table'] = 'u_r_affiliated_with'
					try:
						r_affiliated_with = await client.post('http://' + DB_HOST + '/api/u_r_/items', data=json.dumps(data_affiliated_with), headers = headers)

						assert r_affiliated_with.status == 200, 'connection error!'

						await r_affiliated_with.release()
					except Exception as e:
						await r_affiliated_with.release()
						continue

			'''
				operations related to 'u_r_written_by' table
			'''			
			params = {'table': 'u_r_written', 'author_id': author_id, 'literature_id': literature_id}
			written_by_json = None
			try:
				get_written_by = await client.get('http://' + DB_HOST + '/api/u_r_/items', params = params)
				assert get_written_by.status == 200, 'connection error!'			

				has_written_by = await get_written_by.text()
				written_by_json = json.loads(has_written_by)['data']
				await get_written_by.release()
			except Exception as e:
				await get_written_by.release()
				continue

			need_written_by_constructed = False
			if written_by_json is not None:
				if len(written_by_json) != -1:
					pass
				else:
					need_written_by_constructed = True
			else:
				need_written_by_constructed = True

			if need_written_by_constructed:
				item_written_by = {}
				data_written_by = {}

				item_written_by['author_id'] = author_id
				item_written_by['literature_id'] = literature_id

				data_written_by['item'] = item_written_by
				data_written_by['table'] = 'u_r_written_by'
				try:
					r_written_by = await client.post('http://' + DB_HOST + '/api/u_r_/items', data=json.dumps(data_written_by), headers = headers)

					assert r_written_by.status == 200, 'connection error!'

					await r_written_by.release()
				except Exception as e:
					await r_written_by.release()
					continue



workbook1 = xlrd.open_workbook(ROUTE)

sheet1_name = workbook1.sheet_names()[0]
print(sheet1_name)

sheet1 = workbook1.sheet_by_name(sheet1_name)
print(sheet1.name, sheet1.nrows, sheet1.ncols)

items = []
for i in range(sheet1.nrows):
	if i == 0:
		continue
	rows = sheet1.row_values(i)
	item = {}
	for j in range(len(COLUM_FAMILY)):
		column_name = COLUM_FAMILY[j]
		value_t = sheet1.cell(i,j).value
		if isinstance(value_t, str):
			value_t = value_t.strip()
		item[column_name] = value_t

	items.append(item)

data = {'items':items}

headers = {'content-type': 'application/json'}

with aiohttp.ClientSession() as client:
	tasks = [uansr_data(client, data, headers)]

	asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
