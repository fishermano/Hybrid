#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

import copy
from datetime import *
from aiohttp import web
import pymongo

import gl
from coroweb import get, post
from format import data_res_format, items_num_format, repo_items_num_format, repo_data_res_format
from apis import APIError, APIValueError, APIResourceNotFoundError, APIPermissionError
from models.mysql.models import SR_News_Result, SR_Topics_Result, Top_Companies_Repo, Conf_Repo, Crawler_Repo, Journal_Repo, Oa_Repo, Vod_Repo, Dissertation_Repo, Ebook_Repo, Uansr_Repo, Patent_Repo, Institution_Repo, U_R_Literature, U_R_Written_By, U_R_Affiliated_With, U_R_Author, U_R_University, U_R_Conference, P_T_Repo, P_T_Field, P_T_Belong_To
from models.mongodb.mongodb_models import Logs, Items
from models.es.es_models import Index
from tools import next_id, cur_timestamp, today

@get('/api/test')
def test_api(**kw):
	'''
	#result = yield from Logs.save(doc = {'key': 8, '_id': next_id()})
	
	item = Items(_id = next_id(), date = today())
	item_id = yield from item.save()

	log = Logs(_id = next_id(), item_id = item_id, click_time = cur_timestamp(), user_id = next_id(), keywords = 'test', res_id = next_id(), res_type = 'conf')
	log_id = yield from log.save()
	#result = yield from Logs.remove(doc = {'key': '2'})
	#result = yield from Logs.update(old_doc = {'key': 'value'}, new_doc = {'key': 3})
	#result = yield from Items.find(limit = (1,20))
	return log_id
	'''
	result = yield from Index.searchAll('system computer')

	return data_res_format(data = result)


@get('/api/')
def all_apis():
	test_apis = []
	test_apis.append('Hello: GET /api/hello/:name')
	test_apis.append('Hello: GET /api/hello?name=CX&age=25')
	test_apis.append('Hello: GET /api/hello/multi-keys?name=CX&gender=male&age=25')

	logs_apis = []
	logs_apis.append('Insert Item: POST /api/logs/items')
	logs_apis.append('Retrive Items: GET /api/logs/items?key1=value1&key2=value2')

	hot_topics_apis = []
	hot_topics_apis.append('Insert Item: POST /api/hot_topics/items')
	hot_topics_apis.append('Retrive Items: GET /api/hot_topics/items?key1=value1&key2=value2')
	hot_topics_apis.append('Get Items Num: GET /api/hot_topics/items_num?key1=value1&key2=value2')

	top_companies_apis = []
	top_companies_apis.append('Get Item: GET /api/top_companies/items/:item_id')
	top_companies_apis.append('Insert Item: POST /api/top_companies/items')
	top_companies_apis.append('Delete Item: GET /api/top_companies/items/:item_id')
	top_companies_apis.append('Retrive Items: GET /api/top_companies/items?key1=value1&key2=value2')
	top_companies_apis.append('Get Items Num: GET /api/top_companies/items_num?key1=value1&key2=value2')

	conf_apis = []
	conf_apis.append('Get Item: GET /api/conf/items/:item_id')
	conf_apis.append('Insert Item: POST /api/conf/items')
	conf_apis.append('Delete Item: GET /api/conf/items/:item_id')
	conf_apis.append('Retrive Items: GET /api/conf/items?key1=value1&key2=value2')
	conf_apis.append('Get Items Num: GET /api/conf/items_num?key1=value1&key2=value2')

	crawler_apis = []
	crawler_apis.append('Get Item: GET /api/crawler/items/:item_id')
	crawler_apis.append('Insert Item: POST /api/crawler/items')
	crawler_apis.append('Delete Item: GET /api/crawler/items/:item_id')
	crawler_apis.append('Retrive Items: GET /api/crawler/items?key1=value1&key2=value2')
	crawler_apis.append('Get Items Num: GET /api/crawler/items_num?key1=value1&key2=value2')

	journal_apis = []
	journal_apis.append('Get Item: GET /api/journal/items/:item_id')
	journal_apis.append('Insert Item: POST /api/journal/items')
	journal_apis.append('Delete Item: GET /api/journal/items/:item_id')
	journal_apis.append('Retrive Items: GET /api/journal/items?key1=value1&key2=value2')
	journal_apis.append('Get Items Num: GET /api/journal/items_num?key1=value1&key2=value2')

	oa_apis = []
	oa_apis.append('Get Item: GET /api/oa/items/:item_id')
	oa_apis.append('Insert Item: POST /api/oa/items')
	oa_apis.append('Delete Item: GET /api/oa/items/:item_id')
	oa_apis.append('Retrive Items: GET /api/oa/items?key1=value1&key2=value2')
	oa_apis.append('Get Items Num: GET /api/oa/items_num?key1=value1&key2=value2')

	repo_apis = []
	repo_apis.append('Retrive Items: GET /api/repo/items?key1=value1&key2=value2')
	repo_apis.append('Get Items Num: GET /api/repo/items_num?key1=value1&key2=value2')	

	dissertation_apis = []
	dissertation_apis.append('Get Item: GET /api/dissertation/items/:item_id')
	dissertation_apis.append('Insert Item: POST /api/dissertation/items')
	dissertation_apis.append('Delete Item: GET /api/dissertation/items/:item_id/delete')
	dissertation_apis.append('Retrive Items: GET /api/dissertation/items?key1=value1&key2=value2')
	dissertation_apis.append('Get Items Num: GET /api/dissertation/items_num?key1=value1&key2=value2')

	vod_apis = []
	vod_apis.append('Get Item: GET /api/vod/items/:item_id')
	vod_apis.append('Insert Item: POST /api/vod/items')
	vod_apis.append('Delete Item: GET /api/vod/items/:item_id/delete')
	vod_apis.append('Retrive Items: GET /api/vod/items?key1=value1&key2=value2')
	vod_apis.append('Get Items Num: GET /api/vod/items_num?key1=value1&key2=value2')

	ebook_apis = []
	ebook_apis.append('Get Item: GET /api/ebook/items/:item_id')
	ebook_apis.append('Insert Item: POST /api/ebook/items')
	ebook_apis.append('Delete Item: GET /api/ebook/items/:item_id/delete')
	ebook_apis.append('Retrive Items: GET /api/ebook/items?key1=value1&key2=value2')
	ebook_apis.append('Get Items Num: GET /api/ebook/items_num?key1=value1&key2=value2')

	uansr_apis = []
	uansr_apis.append('Get Item: GET /api/uansr/items/:item_id')
	uansr_apis.append('Insert Item: POST /api/uansr/items')
	uansr_apis.append('Delete Item: GET /api/uansr/items/:item_id/delete')
	uansr_apis.append('Retrive Items: GET /api/uansr/items?key1=value1&key2=value2')
	uansr_apis.append('Get Items Num: GET /api/uansr/items_num?key1=value1&key2=value2')

	patent_apis = []
	patent_apis.append('Get Item: GET /api/patent/items/:item_id')
	patent_apis.append('Insert Item: POST /api/patent/items')
	patent_apis.append('Delete Item: GET /api/patent/items/:item_id/delete')
	patent_apis.append('Retrive Items: GET /api/patent/items?key1=value1&key2=value2')
	patent_apis.append('Get Items Num: GET /api/patent/items_num?key1=value1&key2=value2')

	institution_apis = []
	institution_apis.append('Get Item: GET /api/institution/items/:item_id')
	institution_apis.append('Insert Item: POST /api/institution/items')
	institution_apis.append('Delete Item: GET /api/institution/items/:item_id/delete')
	institution_apis.append('Retrive Items: GET /api/institution/items?key1=value1&key2=value2')
	institution_apis.append('Get Items Num: GET /api/institution/items_num?key1=value1&key2=value2')

	u_r_apis = []
	u_r_apis.append('Insert Item: POST /api/u_r_/items')
	u_r_apis.append('Retrive Items: GET /api/u_r_/items?key1=value1&key2=value2')
	u_r_apis.append('Get Items Num: GET /api/u_r_/items_num?key1=value1&key2=value2')

	all_apis = {'Test':test_apis, 'Log': logs_apis, 'Repo':repo_apis, 'Vod':vod_apis, 'Dissertation':dissertation_apis , 'Hot Topics': hot_topics_apis, 'Top Companies': top_companies_apis, 'Conference': conf_apis, 'Crawler':crawler_apis, 'Journal': journal_apis, 'Oa':oa_apis, 'Ebook':ebook_apis, 'Uansr':uansr_apis, 'Patent': patent_apis, 'Institution': institution_apis, 'U_R_*': u_r_apis}
	return {
		'__template__': 'apis.html',
		'all_apis': all_apis
	}

@get('/api/hello/{name}')
def index(*, name):
	return {
		'__template__': 'default.html',
		'name': name
	}

@get('/api/hello')
def hello_named_key(*, name, age):
	name = name + ', and you are ' + age + ' years old'
	return {
		'__template__': 'default.html',
		'name': name
	}

@get('/api/hello/multi-keys')
def hello_multi_key(**kw):
	name = ''
	i = 0
	for k, v in kw.items():
		if i == 0:
			name = name + k + ' = ' +v
			i = 1
			continue
		name = name + ' , ' + k + ' = ' + v
	
	return {
		'__template__': 'default.html',
		'name': name
	}

############################################################################################
#                                   API for logs
############################################################################################

@post('/api/logs/items')
def logs_insert_items(*, item):
	if not isinstance(item, dict):
		raise APIValueError('data', message = 'data\'s type should be a dict')

	item_id = None
	is_item = yield from Items.find(doc = {'date': today()})
	if len(is_item) != 0:
		item_id = is_item[0]['_id']
	else:
		item_id = next_id()
		item = Items(_id = item_id, date = today())
		yield from item.save()
	
	_id = None
	log = Logs(_id = next_id(), item_id = item_id, **item)
	yield from log.save()

	return log._id


@get('/api/logs/items')
def logs_retrive_all_items(**kw):
		
	if kw:
		results = []

		orderby = kw.get('orderby', None)
		field = None
		direction = None
		if orderby:
			field = orderby.split(' ')[0]
			direction_ = orderby.split(' ')[1]
			if direction_ == 'asc':
				direction = pymongo.ASCENDING
			elif direction_ == 'desc':
				direction = pymongo.DESCENDING	
			kw.pop('orderby')

		sort = None
		if field and direction:
			sort = [(field, direction)]

		p = kw.get('p', None)
		if p:
			kw.pop('p')

		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			limit = (p_, pcount_)

		
		try:
			items = yield from Items.find(sort = sort, limit = limit)

			for _item in items:

				item = {}

				item['date'] = _item['date']
				item['logs'] = yield from Logs.find(doc = {'item_id': _item['_id']})

				results.append(item)

			return data_res_format(data = results)			
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		results = []
		try:
			items = yield from Items.find()

			for _item in items:

				item = {}

				item['date'] = _item['date']
				item['logs'] = yield from Logs.find(doc = {'item_id': _item['_id']})

				results.append(item)

			return data_res_format(data = results)
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))		
	


############################################################################################
#                                   API for hot_topics
############################################################################################

@post('/api/hot_topics/items')
def hot_topics_insert_items(*, table, item):
	if not isinstance(item, dict):
		raise APIValueError('data', message = 'data\'s type should be a dict')

	if table is None:
		raise APIValueError('data', message = 'table\'s value should be defined')

	iid = next_id()
	item_obj = None
	if table == 'sr_news_result':
		item_obj = SR_News_Result(id = iid, **item)
		yield from item_obj.save()
		return item_obj.id
	elif table == 'sr_topics_result':
		item_obj = SR_Topics_Result(id = iid, **item)
		yield from item_obj.save()
		return item_obj.id

@get('/api/hot_topics/items/{id}')
def hot_topics_retrive_items(*, id, **kw):
	if kw:
		items = []

		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')

		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		try:
			topic_item = yield from SR_Topics_Result.find(id)

			if topic_item:
				item = {}

				item['id'] = topic_item['id']
				item['keywords'] = topic_item['keywords']
				item['summary'] = topic_item['summary']
				item['doc_num'] = topic_item['doc_num']
				item['topic_time'] = topic_item['topic_time']

				where_str = 'related_topic = ?'
				args_list = []
				args_list.append(topic_item['id'])
				item['related_news'] = yield from SR_News_Result.findAll(where = where_str, args = args_list, **kw_other)
				
				items.append(item)

			return data_res_format(p = p, pcount = pcount, data = items)

		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	else:
		items = []
		try:
			topic_item = yield from SR_Topics_Result.find(id)

			if topic_item:
				item = {}

				item['id'] = topic_item['id']
				item['keywords'] = topic_item['keywords']
				item['summary'] = topic_item['summary']
				item['doc_num'] = topic_item['doc_num']
				item['topic_time'] = topic_item['topic_time']

				where_str = 'related_topic = ?'
				args_list = []
				args_list.append(topic_item['id'])
				item['related_news'] = yield from SR_News_Result.findAll(where = where_str, args = args_list)
				
				items.append(item)

			return data_res_format(data = items)
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))


@get('/api/hot_topics/items')
def hot_topics_retrive_all_items(**kw):
		
	if kw:
		items = []

		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')

		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		prefetch = kw.get('prefetch', None)
		if prefetch:
			kw.pop('prefetch')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		try:
			topic_items = yield from SR_Topics_Result.findAll(**kw_other)

			for topic_item in topic_items:
				item = {}

				item['id'] = topic_item['id']
				item['keywords'] = topic_item['keywords']
				item['summary'] = topic_item['summary']
				item['doc_num'] = topic_item['doc_num']
				item['topic_time'] = topic_item['topic_time']

				where_str = 'related_topic = ?'
				args_list = []
				args_list.append(topic_item['id'])
				if prefetch:
					kw_other_ = {
						'orderby': 'post_time desc',
						'limit': (0, int(prefetch))
					}
					item['related_news'] = yield from SR_News_Result.findAll(where = where_str, args = args_list, **kw_other_)
				else:
					item['related_news'] = yield from SR_News_Result.findAll(where = where_str, args = args_list)
				
				items.append(item)

			return data_res_format(p = p, pcount = pcount, data = items)

		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	else:
		items = []
		try:
			topic_items = yield from SR_Topics_Result.findAll()

			for topic_item in topic_items:
				item = {}

				item['id'] = topic_item['id']
				item['keywords'] = topic_item['keywords']
				item['summary'] = topic_item['summary']
				item['doc_num'] = topic_item['doc_num']
				item['topic_time'] = topic_item['topic_time']

				where_str = 'related_topic = ?'
				args_list = []
				args_list.append(topic_item['id'])
				item['related_news'] = yield from SR_News_Result.findAll(where = where_str, args = args_list)
				
				items.append(item)

			return data_res_format(data = items)
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))


@get('/api/hot_topics/items_num')
def hot_topics_retrive_items_num(**kw):

	table = kw.get('table', None)
	if table is None:
		
		total_data_count = 0

		try:
			total_data_count = yield from SR_Topics_Result.getNumber()							
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))		

		return items_num_format(total_data_count = total_data_count)

	else:
		return items_num_format(code = 500, ok = False, msg = 'error api invoked!')


############################################################################################
#                                   API for top_companies
############################################################################################

@post('/api/top_companies/items')
def top_companies_insert_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')
	top_companies_repo = []
	for item in items:

		iid = next_id()
		top_companies = Top_Companies_Repo(id = iid, **item)
		yield from top_companies.save()
		top_companies_repo.append(top_companies)

	try:
		gl.TOP_COMPANIES_REPO_TDC = yield from Top_Companies_Repo.getNumber()
	except Exception as e:
		pass

	return top_companies_repo

@get('/api/top_companies/items/{item_id}/delete')
def top_companies_delete_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Top_Companies_Repo.find(item_id)
	yield from item.remove()
	return data_res_format(data = item)

@get('/api/top_companies/items_num')
def top_companies_retrive_items_num(**kw):
	total_data_count = 0
	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count = yield from Top_Companies_Repo.getNumber(where = where_str, args = args_list)	
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))
	else:
		if gl.TOP_COMPANIES_REPO_TDC == -1:
			try:
				gl.TOP_COMPANIES_REPO_TDC = yield from Top_Companies_Repo.getNumber()
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))

		total_data_count = gl.TOP_COMPANIES_REPO_TDC

	return items_num_format(total_data_count = total_data_count)

@get('/api/top_companies/items')
def top_companies_retrive_all_items(**kw):
	items = []
	p = None
	pcount = None
	if kw:
		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)

		try:
			items = yield from Top_Companies_Repo.findAll(where = where_str, args = args_list, **kw_other)	
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items = yield from Top_Companies_Repo.findAll()
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	return data_res_format(p = p, pcount = pcount, data = items)

@get('/api/top_companies/items/{item_id}')
def top_companies_get_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Top_Companies_Repo.find(item_id)
	return data_res_format(data = item)


############################################################################################
#                                   API for conf
############################################################################################

@post('/api/conf/items')
def conf_insert_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')
	conf_repo = []
	for item in items:

		iid = next_id()
		created_at = cur_timestamp()

		conf = Conf_Repo(id = iid, created_at = created_at, **item)

		yield from conf.save()
		conf_repo.append(conf)

	try:
		gl.CONF_REPO_TDC = yield from Conf_Repo.getNumber()
	except Exception as e:
		pass

	return conf_repo

@get('/api/conf/items/{item_id}/delete')
def conf_delete_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Conf_Repo.find(item_id)
	yield from item.remove()
	return data_res_format(data = item)

@get('/api/conf/items_num')
def conf_retrive_items_num(**kw):
	total_data_count = 0
	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				if k == 'cur_date':
					where_str = 'end_date > ? and start_date is not null'
				else:
					where_str = k + ' like ?'
				i = i + 1
			else:
				if k == 'cur_date':
					where_str = where_str + ' and ' + 'end_date > ? and start_date is not null'
				else:
					where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				if k == 'cur_date':
					v_ = v
				else:
					v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count = yield from Conf_Repo.getNumber(where = where_str, args = args_list)	
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))
	else:
		if gl.CONF_REPO_TDC == -1:
			try:
				gl.CONF_REPO_TDC = yield from Conf_Repo.getNumber()
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))

		total_data_count = gl.CONF_REPO_TDC

	return items_num_format(total_data_count = total_data_count)

@get('/api/conf/items')
def conf_retrive_all_items(**kw):
	items = []
	p = None
	pcount = None
	if kw:
		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				if k == 'cur_date':
					where_str = 'end_date > ? and start_date is not null'
				else:
					where_str = k + ' like ?'
				i = i + 1
			else:
				if k == 'cur_date':
					where_str = where_str + ' and ' + 'end_date > ? and start_date is not null'
				else:
					where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				if k == 'cur_date':
					v_ = v
				else:
					v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)

		try:
			items = yield from Conf_Repo.findAll(where = where_str, args = args_list, **kw_other)	
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items = yield from Conf_Repo.findAll()
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	'''
	items_s = []
	items_e = []
	cur_time = date.today()
	for item in items:

		if (datetime.strptime(item['end_date'], '%Y-%m-%d %H:%M:%S').date() > cur_time):
			items_s.append(item)
		else:
			items_e.append(item)
	
	items_s.extend(items_e)
	'''
	return data_res_format(p = p, pcount = pcount, data = items)

@get('/api/conf/items/{item_id}')
def conf_get_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Conf_Repo.find(item_id)
	return data_res_format(data = item)


############################################################################################
#                                   API for repo
############################################################################################

@get('/api/repo/items_num')
def repo_retrive_items_num(**kw):
	total_data_count = {}
	total_data_count_d = 0
	total_data_count_e = 0
	total_data_count_u = 0
	total_data_count_p = 0
	total_data_count_c = 0

	if kw:

		where_str_d = ''
		where_str_e = ''
		where_str_u = ''
		where_str_p = ''
		where_str_c = ''

		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				if k == 'title':
					where_str_d = 'foreign_title like ?'
					where_str_e = k + ' like ?'
					where_str_u = k + ' like ?'
					where_str_p = k + ' like ?'
					where_str_c = 'conference_name like ?'

				elif k == 'summary':
					where_str_d = 'match(english_abstract) against(?)'
					where_str_e = 'match(summary) against(?)'
					where_str_u = 'match(summary) against(?)'
					where_str_p = 'match(summary) against(?)'
					where_str_c = 'publication_name like ?'

				else:
					where_str_d = k + ' like ?'
					where_str_e = k + ' like ?'
					where_str_u = k + ' like ?'
					where_str_p = k + ' like ?'
					where_str_c = k + ' like ?'

				i = i + 1
			else:
				if k == 'title':
					where_str_d = where_str_d + ' or ' + 'foreign_title like ?'
					where_str_e = where_str_e + ' or ' + k + ' like ?'
					where_str_u = where_str_u + ' or ' + k + ' like ?'
					where_str_p = where_str_p + ' or ' + k + ' like ?'
					where_str_c = where_str_c + ' or ' + 'conference_name like ?'

				elif k == 'summary':
					where_str_d = where_str_d + ' or ' + 'match(english_abstract) against(?)'	
					where_str_e = where_str_e + ' or ' + 'match(summary) against(?)'
					where_str_u = where_str_u + ' or ' + 'match(summary) against(?)'
					where_str_p = where_str_p + ' or ' + 'match(summary) against(?)'
					where_str_c = where_str_c + ' or ' + 'publication_name like?'

				else:
					where_str_d = where_str_d + ' or ' + k + ' like ?'	
					where_str_e = where_str_e + ' or ' + k + ' like ?'
					where_str_u = where_str_u + ' or ' + k + ' like ?'
					where_str_p = where_str_p + ' or ' + k + ' like ?'
					where_str_c = where_str_c + ' or ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count_d = yield from Dissertation_Repo.getNumber(where = where_str_d, args = args_list)
			total_data_count_e = yield from Ebook_Repo.getNumber(where = where_str_e, args = args_list)
			total_data_count_u = yield from Uansr_Repo.getNumber(where = where_str_u, args = args_list)
			total_data_count_p = yield from Patent_Repo.getNumber(where = where_str_p, args = args_list)
			total_data_count_c = yield from Conf_Repo.getNumber(where = where_str_c, args = args_list)


		except Exception as e:
			return repo_items_num_format(code = 500, ok = False, msg = str(e))
	else:
		if gl.DISSERTATION_REPO_TDC == -1:
			try:
				gl.DISSERTATION_REPO_TDC = yield from Dissertation_Repo.getNumber()
			except Exception as e:
				return repo_items_num_format(code = 500, ok = False, msg = str(e))

		if gl.EBOOK_REPO_TDC == -1:
			try:
				gl.EBOOK_REPO_TDC = yield from Ebook_Repo.getNumber()
			except Exception as e:
				return repo_items_num_format(code = 500, ok = False, msg = str(e))

		if gl.UANSR_REPO_TDC == -1:
			try:
				gl.UANSR_REPO_TDC = yield from Uansr_Repo.getNumber()
			except Exception as e:
				return repo_items_num_format(code = 500, ok = False, msg = str(e))

		if gl.PATENT_REPO_TDC == -1:
			try:
				gl.PATENT_REPO_TDC = yield from Patent_Repo.getNumber()
			except Exception as e:
				return repo_items_num_format(code = 500, ok = False, msg = str(e))

		if gl.CONFERENCE_REPO_TDC == -1:
			try:
				gl.CONFERENCE_REPO_TDC = yield from Conf_Repo.getNumber()
			except Exception as e:
				return repo_items_num_format(code = 500, ok = False, msg = str(e))


		total_data_count_d = gl.DISSERTATION_REPO_TDC
		total_data_count_e = gl.EBOOK_REPO_TDC
		total_data_count_u = gl.UANSR_REPO_TDC
		total_data_count_p = gl.PATENT_REPO_TDC
		total_data_count_c = gl.CONFERENCE_REPO_TDC

	total_data_count['dissertation_nums'] = total_data_count_d
	total_data_count['ebook_nums'] = total_data_count_e
	total_data_count['uansr_nums'] = total_data_count_u
	total_data_count['patent_nums'] = total_data_count_p
	total_data_count['conference_nums'] = total_data_count_c

	return repo_items_num_format(total_data_count = total_data_count)

@get('/api/repo/items')
def repo_retrive_all_items(**kw):
	items = {}
	items_d = []
	items_e = []
	items_u = []
	items_p = []
	items_c = []

	p = None
	pcount = None
	if kw:
		rtype = kw.get('rtype', None)
		if rtype:
			kw.pop('rtype')

		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return repo_data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str_d = ''
		where_str_e = ''
		where_str_u = ''
		where_str_p = ''
		where_str_c = ''

		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				if k == 'title':
					where_str_d = 'foreign_title like ?'
					where_str_e = k + ' like ?'
					where_str_u = k + ' like ?'
					where_str_p = k + ' like ?'
					where_str_c = 'conference_name like ?'

				elif k == 'summary':
					where_str_d = 'match(english_abstract) against(?)'
					where_str_e = 'match(summary) against(?)'
					where_str_u = 'match(summary) against(?)'
					where_str_p = 'match(summary) against(?)'
					where_str_c = 'publication_name like ?'

				else:
					where_str_d = k + ' like ?'
					where_str_e = k + ' like ?'
					where_str_u = k + ' like ?'
					where_str_p = k + ' like ?'
					where_str_c = k + ' like ?'

				i = i + 1
			else:
				if k == 'title':
					where_str_d = where_str_d + ' or ' + 'foreign_title like ?'
					where_str_e = where_str_e + ' or ' + k + ' like ?'
					where_str_u = where_str_u + ' or ' + k + ' like ?'
					where_str_p = where_str_p + ' or ' + k + ' like ?'
					where_str_c = where_str_c + ' or ' + 'conference_name like ?'

				elif k == 'summary':
					where_str_d = where_str_d + ' or ' + 'match(english_abstract) against(?)'	
					where_str_e = where_str_e + ' or ' + 'match(summary) against(?)'
					where_str_u = where_str_u + ' or ' + 'match(summary) against(?)'
					where_str_p = where_str_p + ' or ' + 'match(summary) against(?)'
					where_str_c = where_str_c + ' or ' + 'publication_name like ?'

				else:
					where_str_d = where_str_d + ' or ' + k + ' like ?'	
					where_str_e = where_str_e + ' or ' + k + ' like ?'
					where_str_u = where_str_u + ' or ' + k + ' like ?'
					where_str_p = where_str_p + ' or ' + k + ' like ?'
					where_str_c = where_str_c + ' or ' + k + ' like ?'


			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)

		try:
			
			args_list_d = copy.deepcopy(args_list)
			args_list_e = copy.deepcopy(args_list)
			args_list_u = copy.deepcopy(args_list)
			args_list_p = copy.deepcopy(args_list)
			args_list_c = copy.deepcopy(args_list)

			if rtype == 'dissertation':
				items_d = yield from Dissertation_Repo.findAll(where = where_str_d, args = args_list_d, **kw_other)

			elif rtype == 'ebook':
				items_e = yield from Ebook_Repo.findAll(where = where_str_e, args = args_list_e, **kw_other)

			elif rtype == 'uansr':
				items_u = yield from Uansr_Repo.findAll(where = where_str_u, args = args_list_u, **kw_other)

			elif rtype == 'patent':
				items_p = yield from Patent_Repo.findAll(where = where_str_p, args = args_list_p, **kw_other)

			elif rtype == 'conference':
				items_c = yield from Conf_Repo.findAll(where = where_str_c, args = args_list_c, **kw_other)			

			else:
				items_d = yield from Dissertation_Repo.findAll(where = where_str_d, args = args_list_d, **kw_other)
				items_e = yield from Ebook_Repo.findAll(where = where_str_e, args = args_list_e, **kw_other)
				items_u = yield from Uansr_Repo.findAll(where = where_str_u, args = args_list_u, **kw_other)
				items_p = yield from Patent_Repo.findAll(where = where_str_p, args = args_list_p, **kw_other)
				items_c = yield from Conf_Repo.findAll(where = where_str_c, args = args_list_c, **kw_other)

		except Exception as e:
			return repo_data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items_d = yield from Dissertation_Repo.findAll()
			items_e = yield from Ebook_Repo.findAll()
			items_u = yield from Uansr_Repo.findAll()
			items_p = yield from Patent_Repo.findAll()
			items_c = yield from Conf_Repo.findAll()
		except Exception as e:
			return repo_data_res_format(code = 500, ok = False, msg = str(e))

	items['dissertation_items'] = items_d
	items['ebook_items'] = items_e
	items['uansr_items'] = items_u
	items['patent_items'] = items_p
	items['conference_items'] = items_c

	return repo_data_res_format(p = p, pcount = pcount, data = items)

############################################################################################
#                                   API for crawler
############################################################################################

@post('/api/crawler/items')
def crawler_insert_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')
	crawler_repo = []
	for item in items:

		iid = next_id()
		created_at = cur_timestamp()

		crawler = Crawler_Repo(id = iid, created_at = created_at, **item)

		yield from crawler.save()
		crawler_repo.append(crawler)

	return crawler_repo

@get('/api/crawler/items/{item_id}/delete')
def crawler_delete_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Crawler_Repo.find(item_id)
	yield from item.remove()
	return data_res_format(data = item)

@get('/api/crawler/items_num')
def crawler_retrive_items_num(**kw):
	total_data_count = 0
	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count = yield from Crawler_Repo.getNumber(where = where_str, args = args_list)	
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			total_data_count = yield from Crawler_Repo.getNumber()
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))

	return items_num_format(total_data_count = total_data_count)

@get('/api/crawler/items')
def crawler_retrive_all_items(**kw):
	items = []
	p = None
	pcount = None
	if kw:
		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)

		try:
			items = yield from Crawler_Repo.findAll(where = where_str, args = args_list, **kw_other)	
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items = yield from Crawler_Repo.findAll()
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	return data_res_format(p = p, pcount = pcount, data = items)

@get('/api/crawler/items/{item_id}')
def crawler_get_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Crawler_Repo.find(item_id)
	return data_res_format(data = item)

############################################################################################
#                                   API for journal
############################################################################################

@post('/api/journal/items')
def journal_insert_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')
	journal_repo = []
	for item in items:

		iid = next_id()

		journal = Journal_Repo(id = iid, **item)

		yield from journal.save()
		journal_repo.append(journal)

	return journal_repo

@get('/api/journal/items/{item_id}/delete')
def journal_delete_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Journal_Repo.find(item_id)
	yield from item.remove()
	return data_res_format(data = item)

@get('/api/journal/items_num')
def journal_retrive_items_num(**kw):
	total_data_count = 0
	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count = yield from Journal_Repo.getNumber(where = where_str, args = args_list)	
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			total_data_count = yield from Journal_Repo.getNumber()
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))

	return items_num_format(total_data_count = total_data_count)

@get('/api/journal/items')
def journal_retrive_all_items(**kw):
	items = []
	p = None
	pcount = None
	if kw:
		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)

		try:
			items = yield from Journal_Repo.findAll(where = where_str, args = args_list, **kw_other)	
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items = yield from Journal_Repo.findAll()
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	return data_res_format(p = p, pcount = pcount, data = items)

@get('/api/journal/items/{item_id}')
def journal_get_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Journal_Repo.find(item_id)
	return data_res_format(data = item)


############################################################################################
#                                   API for oa
############################################################################################

@post('/api/oa/items')
def oa_insert_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')
	oa_repo = []
	i = 1
	for item in items:

		iid = next_id()

		oa = Oa_Repo(id = iid, **item)

		yield from oa.save()
		oa_repo.append(oa)

		i = i + 1
		print(i)

	return oa_repo

@get('/api/oa/items/{item_id}/delete')
def oa_delete_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Oa_Repo.find(item_id)
	yield from item.remove()
	return data_res_format(data = item)

@get('/api/oa/items_num')
def oa_retrive_items_num(**kw):
	total_data_count = 0
	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count = yield from Oa_Repo.getNumber(where = where_str, args = args_list)	
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			total_data_count = yield from Oa_Repo.getNumber()
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))

	return items_num_format(total_data_count = total_data_count)

@get('/api/oa/items')
def oa_retrive_all_items(**kw):
	items = []
	p = None
	pcount = None
	if kw:
		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)

		try:
			items = yield from Oa_Repo.findAll(where = where_str, args = args_list, **kw_other)	
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items = yield from Oa_Repo.findAll()
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	return data_res_format(p = p, pcount = pcount, data = items)

@get('/api/oa/items/{item_id}')
def oa_get_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Oa_Repo.find(item_id)
	return data_res_format(data = item)


############################################################################################
#                                   API for vod
############################################################################################

@post('/api/vod/items')
def vod_insert_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')
	vod_repo = []
	for item in items:

		iid = next_id()
		vod = Vod_Repo(id = iid, **item)
		yield from vod.save()
		vod_repo.append(vod)

	return vod_repo

@get('/api/vod/items/{item_id}/delete')
def vod_delete_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Vod_Repo.find(item_id)
	yield from item.remove()
	return data_res_format(data = item)

@get('/api/vod/items_num')
def vod_retrive_items_num(**kw):
	total_data_count = 0
	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count = yield from Vod_Repo.getNumber(where = where_str, args = args_list)	
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			total_data_count = yield from Vod_Repo.getNumber()
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))

	return items_num_format(total_data_count = total_data_count)

@get('/api/vod/items')
def vod_retrive_all_items(**kw):
	items = []
	p = None
	pcount = None
	if kw:
		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)

		try:
			items = yield from Vod_Repo.findAll(where = where_str, args = args_list, **kw_other)	
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items = yield from Vod_Repo.findAll()
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	return data_res_format(p = p, pcount = pcount, data = items)

@get('/api/vod/items/{item_id}')
def vod_get_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Vod_Repo.find(item_id)
	return data_res_format(data = item)

############################################################################################
#                                   API for dissertation
############################################################################################

@post('/api/dissertation/items')
def dissertation_insert_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')
	dissertation_repo = []
	for item in items:

		iid = next_id()
		dissertation = Dissertation_Repo(id = iid, **item)
		yield from dissertation.save()
		dissertation_repo.append(dissertation)

	try:
		gl.DISSERTATION_REPO_TDC = yield from Dissertation_Repo.getNumber()
	except Exception as e:
		pass

	return dissertation_repo

@get('/api/dissertation/items/{item_id}/delete')
def dissertation_delete_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Dissertation_Repo.find(item_id)
	yield from item.remove()
	return data_res_format(data = item)

@get('/api/dissertation/items_num')
def dissertation_retrive_items_num(**kw):
	total_data_count = 0
	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count = yield from Dissertation_Repo.getNumber(where = where_str, args = args_list)	
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))
	else:
		if gl.DISSERTATION_REPO_TDC == -1:
			try:
				gl.DISSERTATION_REPO_TDC = yield from Dissertation_Repo.getNumber()
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))

		total_data_count = gl.DISSERTATION_REPO_TDC

	return items_num_format(total_data_count = total_data_count)

@get('/api/dissertation/items')
def dissertation_retrive_all_items(**kw):
	items = []
	p = None
	pcount = None
	if kw:
		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)

		try:
			items = yield from Dissertation_Repo.findAll(where = where_str, args = args_list, **kw_other)	
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items = yield from Dissertation_Repo.findAll()
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	return data_res_format(p = p, pcount = pcount, data = items)

@get('/api/dissertation/items/{item_id}')
def dissertation_get_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Dissertation_Repo.find(item_id)
	return data_res_format(data = item)

############################################################################################
#                                   API for ebook
############################################################################################
@post('/api/ebook/update/items')
def ebook_update_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')	
		
	for item in items:
		item_id = item['id'].strip()
		try:
			ebook = yield from Ebook_Repo.find(item_id)
			ebook['img_url'] = item['img_url'].strip()
			yield from ebook.update()
		except Exception as e:
			pass
		
	return
		


@post('/api/ebook/items')
def ebook_insert_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')
	ebook_repo = []

	for item in items:

		iid = next_id()
		ebook = Ebook_Repo(id = iid, **item)
		yield from ebook.save()
		ebook_repo.append(ebook)

	try:
		gl.EBOOK_REPO_TDC = yield from Ebook_Repo.getNumber()
	except Exception as e:
		pass

	return ebook_repo

@get('/api/ebook/items/{item_id}/delete')
def ebook_delete_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Ebook_Repo.find(item_id)
	yield from item.remove()
	return data_res_format(data = item)

@get('/api/ebook/items_num')
def ebook_retrive_items_num(**kw):
	total_data_count = 0
	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count = yield from Ebook_Repo.getNumber(where = where_str, args = args_list)	
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))
	else:
		if gl.EBOOK_REPO_TDC == -1:
			try:
				gl.EBOOK_REPO_TDC = yield from Ebook_Repo.getNumber()
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))

		total_data_count = gl.EBOOK_REPO_TDC

	return items_num_format(total_data_count = total_data_count)

@get('/api/ebook/items')
def ebook_retrive_all_items(**kw):
	items = []
	p = None
	pcount = None
	if kw:
		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_ 
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)

		try:
			items = yield from Ebook_Repo.findAll(where = where_str, args = args_list, **kw_other)	
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items = yield from Ebook_Repo.findAll()
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	return data_res_format(p = p, pcount = pcount, data = items)


@get('/api/ebook/items/{item_id}')
def ebook_get_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Ebook_Repo.find(item_id)
	return data_res_format(data = item)

############################################################################################
#                                   API for uansr
############################################################################################

@post('/api/uansr/items')
def uansr_insert_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')
	uansr_repo = []
	for item in items:

		iid = next_id()
		uansr = Uansr_Repo(id = iid, **item)
		yield from uansr.save()
		uansr_repo.append(uansr)

	try:
		gl.UANSR_REPO_TDC = yield from Uansr_Repo.getNumber()
	except Exception as e:
		pass

	return uansr_repo

@get('/api/uansr/items/{item_id}/delete')
def uansr_delete_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Uansr_Repo.find(item_id)
	yield from item.remove()
	return data_res_format(data = item)

@get('/api/uansr/items_num')
def uansr_retrive_items_num(**kw):
	total_data_count = 0
	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count = yield from Uansr_Repo.getNumber(where = where_str, args = args_list)	
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))
	else:
		if gl.UANSR_REPO_TDC == -1:
			try:
				gl.UANSR_REPO_TDC = yield from Uansr_Repo.getNumber()
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))

		total_data_count = gl.UANSR_REPO_TDC

	return items_num_format(total_data_count = total_data_count)

@get('/api/uansr/items')
def uansr_retrive_all_items(**kw):
	items = []
	p = None
	pcount = None
	if kw:
		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)

		try:
			items = yield from Uansr_Repo.findAll(where = where_str, args = args_list, **kw_other)	
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items = yield from Uansr_Repo.findAll()
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	return data_res_format(p = p, pcount = pcount, data = items)

@get('/api/uansr/items/{item_id}')
def uansr_get_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Uansr_Repo.find(item_id)
	return data_res_format(data = item)

############################################################################################
#                                   API for patent
############################################################################################

@post('/api/patent/items')
def patent_insert_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')
	patent_repo = []
	for item in items:

		iid = next_id()
		patent = Patent_Repo(id = iid, **item)
		yield from patent.save()
		patent_repo.append(patent)

	try:
		gl.PATENT_REPO_TDC = yield from Patent_Repo.getNumber()
	except Exception as e:
		pass

	return patent_repo

@get('/api/patent/items/{item_id}/delete')
def patent_delete_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Patent_Repo.find(item_id)
	yield from item.remove()
	return data_res_format(data = item)

@get('/api/patent/items_num')
def patent_retrive_items_num(**kw):
	total_data_count = 0
	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count = yield from Patent_Repo.getNumber(where = where_str, args = args_list)	
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))
	else:
		if gl.PATENT_REPO_TDC == -1:
			try:
				gl.PATENT_REPO_TDC = yield from Patent_Repo.getNumber()
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))
		total_data_count = gl.PATENT_REPO_TDC

	return items_num_format(total_data_count = total_data_count)

@get('/api/patent/items')
def patent_retrive_all_items(**kw):
	items = []
	p = None
	pcount = None
	if kw:
		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)

		try:
			items = yield from Patent_Repo.findAll(where = where_str, args = args_list, **kw_other)	
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items = yield from Patent_Repo.findAll()
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	return data_res_format(p = p, pcount = pcount, data = items)

@get('/api/patent/items/{item_id}')
def patent_get_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Patent_Repo.find(item_id)
	return data_res_format(data = item)

############################################################################################
#                                   API for institution
############################################################################################

@post('/api/institution/items')
def institution_insert_items(*, items):
	if not isinstance(items, list):
		raise APIValueError('data', message = 'data\'s type should be a list')
	institution_repo = []
	for item in items:

		iid = next_id()
		institution = Institution_Repo(id = iid, **item)
		yield from institution.save()
		institution_repo.append(institution)

	try:
		gl.INSTITUTION_REPO_TDC = yield from Institution_Repo.getNumber()
	except Exception as e:
		pass

	return institution_repo

@get('/api/institution/items/{item_id}/delete')
def institution_delete_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Institution_Repo.find(item_id)
	yield from item.remove()
	return data_res_format(data = item)

@get('/api/institution/items_num')
def institution_retrive_items_num(**kw):
	total_data_count = 0
	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			total_data_count = yield from Institution_Repo.getNumber(where = where_str, args = args_list)	
		except Exception as e:
			return items_num_format(code = 500, ok = False, msg = str(e))
	else:
		if gl.INSTITUTION_REPO_TDC == -1:
			try:
				gl.INSTITUTION_REPO_TDC = yield from Institution_Repo.getNumber()
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))

		total_data_count = gl.INSTITUTION_REPO_TDC

	return items_num_format(total_data_count = total_data_count)	

@get('/api/institution/items')
def institution_retrive_all_items(**kw):
	items = []
	p = None
	pcount = None
	if kw:
		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' like ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' like ?'

			if(isinstance(v,str)):
				v_ = '%' + v + '%'
				args_list.append(v_.encode('utf-8'))
			else:
				args_list.append(v)
		
		try:
			items = yield from Institution_Repo.findAll(where = where_str, args = args_list, **kw_other)	
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))
	else:
		try:
			items = yield from Institution_Repo.findAll()
		except Exception as e:
			return data_res_format(code = 500, ok = False, msg = str(e))

	return data_res_format(p = p, pcount = pcount, data = items)

@get('/api/institution/items/{item_id}')
def institution_get_item(item_id):
	if not item_id or not item_id.strip():
		raise APIValueError('item_id')

	item = yield from Institution_Repo.find(item_id)
	return data_res_format(data = item)


############################################################################################
#                                   API for u_r_*
############################################################################################

@post('/api/u_r_/items')
def u_r_insert_items(*, table, item):
	if not isinstance(item, dict):
		raise APIValueError('data', message = 'data\'s type should be a dict')

	if table is None:
		raise APIValueError('data', message = 'table\'s value should be defined')

	iid = next_id()
	item_obj = None
	if table == 'u_r_author':
		item_obj = U_R_Author(id = iid, **item)
		yield from item_obj.save()
		return item_obj.id
	elif table == 'u_r_university':
		item_obj = U_R_University(id = iid, **item)
		yield from item_obj.save()
		return item_obj.id
	elif table == 'u_r_conference':
		item_obj = U_R_Conference(**item)
		yield from item_obj.save()
		return item_obj.name
	elif table == 'u_r_literature':		
		item_obj = U_R_Literature(id = iid, **item)
		yield from item_obj.save()			

		u_id = item.get('u_id', None)
		if u_id:
			try:
				if gl.U_R_TDC.get(u_id, None):
					gl.U_R_TDC[u_id] = gl.U_R_TDC[u_id] + 1
				else:
					where_str = 'u_id = ?'
					args_list = [u_id]
					gl.U_R_TDC[u_id] = yield from U_R_Literature.getNumber(where = where_str, args = args_list)
			except Exception as e:
				pass								
		else:
			pass

		try:
			gl.U_R_LITERATURE_TDC = yield from U_R_Literature.getNumber()
		except Exception as e:
			pass
		return item_obj.id
	elif table == 'u_r_written_by':
		item_obj = U_R_Written_By(**item)
		yield from item_obj.save()
		return item_obj
	elif table == 'u_r_affiliated_with':
		item_obj = U_R_Affiliated_With(**item)
		yield from item_obj.save()
		return item_obj

@get('/api/u_r_/items')
def u_r_retrive_all_items(**kw):

	table = kw.get('table', None)
	if table is None:
		
		if kw:
			items = []

			orderby = kw.get('orderby', None)
			if orderby:
				kw.pop('orderby')

			p = kw.get('p', None)
			if p:
				kw.pop('p')
	
			pcount = kw.get('pcount', None)
			if pcount:
				kw.pop('pcount')

			limit = None
			if p and pcount:
				try:
					p_ = int(p)
					pcount_ = int(pcount)
				except ValueError as e:
					return data_res_format(code = 500, ok = False, msg = str(e))
				start_item_num = (p_ - 1) * pcount_
				limit = (start_item_num, pcount_)

			kw_other = {
				'orderby': orderby,
				'limit': limit
			}

			u_id = kw.get('u_id', None)
			if u_id:
				kw.pop('u_id')
				if len(kw) != 0:
					return data_res_format(code = 500, ok = False, msg = 'error api invoked!')
				#where_str = 'id in (select author_id from u_r_affiliated_with where university_id = ?)'
				where_str = 'inner join u_r_affiliated_with on u_r_author.id=u_r_affiliated_with.author_id where u_r_affiliated_with.university_id = ?'
				args_list = []
				if(isinstance(u_id,str)):
					args_list.append(u_id.encode('utf-8'))
				else:
					args_list.append(u_id)
				try:
					items = yield from U_R_Author.findAll(where = where_str, args = args_list, **kw_other)							
				except Exception as e:
					return data_res_format(code = 500, ok = False, msg = str(e))				

			a_id = kw.get('a_id', None)
			if a_id:
				kw.pop('a_id')
				if len(kw) != 0:
					return data_res_format(code = 500, ok = False, msg = 'error api invoked!')
				#where_str = 'id in (select literature_id from u_r_written_by where author_id = ?)'
				where_str = 'inner join u_r_written_by on u_r_literature.id=u_r_written_by.literature_id where u_r_written_by.author_id = ?'
				args_list = []
				if(isinstance(a_id,str)):
					args_list.append(a_id.encode('utf-8'))
				else:
					args_list.append(a_id)
				try:
					items_t = yield from U_R_Literature.findAll(where = where_str, args = args_list, **kw_other)

					for item in items_t:
						item_json = {}
						item_json['literature'] = item
						literature_id = item['id']
						
						authors = yield from U_R_Author.findAll(where = 'inner join u_r_written_by on u_r_author.id=u_r_written_by.author_id where u_r_written_by.literature_id = ?', args = [literature_id])
						item_json['authors'] = authors
						items.append(item_json)
							
				except Exception as e:
					return data_res_format(code = 500, ok = False, msg = str(e))

			if not u_id and not a_id:		
				return data_res_format(code = 500, ok = False, msg = 'error api invoked!')

			if len(kw) != 0:
				return data_res_format(code = 500, ok = False, msg = 'error api invoked!')

			return data_res_format(p = p, pcount = pcount, data = items)
		else:
			return data_res_format(code = 500, ok = False, msg = 'error api invoked!')
	else:
		kw.pop('table')

	table = table.strip()

	items = []
	p = None
	pcount = None

	if kw:

		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' = ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' = ?'

			if(isinstance(v,str)):
				args_list.append(v.encode('utf-8'))
			else:
				args_list.append(v)

		if table == 'u_r_author':
			try:
				items = yield from U_R_Author.findAll(where = where_str, args = args_list, **kw_other)	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_university':
			try:
				items = yield from U_R_University.findAll(where = where_str, args = args_list, **kw_other)	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_conference':
			try:
				items = yield from U_R_Conference.findAll(where = where_str, args = args_list, **kw_other)	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_literature':
			try:
				items = yield from U_R_Literature.findAll(where = where_str, args = args_list, **kw_other)	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_written_by':
			try:
				items = yield from U_R_Written_By.findAll(where = where_str, args = args_list, **kw_other)	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_affiliated_with':
			try:
				items = yield from U_R_Affiliated_With.findAll(where = where_str, args = args_list, **kw_other)	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		else:
			return data_res_format(code = 500, ok = False, msg = table + ' is not exist!')
	else:
		if table == 'u_r_author':
			try:
				items = yield from U_R_Author.findAll()	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_university':
			try:
				items = yield from U_R_University.findAll()	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_conference':
			try:
				items = yield from U_R_Conference.findAll()	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_literature':
			try:
				items = yield from U_R_Literature.findAll()	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_written_by':
			try:
				items = yield from U_R_Written_By.findAll()	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_affiliated_with':
			try:
				items = yield from U_R_Affiliated_With.findAll()	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		else:
			return data_res_format(code = 500, ok = False, msg = table + ' is not exist!')				

	return data_res_format(p = p, pcount = pcount, data = items)


@get('/api/u_r_/items_num')
def u_r_retrive_items_num(**kw):

	table = kw.get('table', None)
	if table is None:
		
		if kw:
			total_data_count = 0

			u_id = kw.get('u_id', None)
			if u_id:
				kw.pop('u_id')
				if len(kw) != 0:
					return items_num_format(code = 500, ok = False, msg = 'error api invoked!')
				where_str = 'id in (select author_id from u_r_affiliated_with where university_id = ?)'
				args_list = []
				if(isinstance(u_id,str)):
					args_list.append(u_id.encode('utf-8'))
				else:
					args_list.append(u_id)
				try:
					total_data_count = yield from U_R_Author.getNumber(where = where_str, args = args_list)							
				except Exception as e:
					return items_num_format(code = 500, ok = False, msg = str(e))		

			a_id = kw.get('a_id', None)
			if a_id:
				kw.pop('a_id')
				if len(kw) != 0:
					return items_num_format(code = 500, ok = False, msg = 'error api invoked!')
				where_str = 'id in (select literature_id from u_r_written_by where author_id = ?)'
				args_list = []
				if(isinstance(a_id,str)):
					args_list.append(a_id.encode('utf-8'))
				else:
					args_list.append(a_id)
				try:
					total_data_count = yield from U_R_Literature.getNumber(where = where_str, args = args_list)
							
				except Exception as e:
					return items_num_format(code = 500, ok = False, msg = str(e))

			if not u_id and not a_id:		
				return items_num_format(code = 500, ok = False, msg = 'error api invoked!')

			if len(kw) != 0:
				return items_num_format(code = 500, ok = False, msg = 'error api invoked!')

			return items_num_format(total_data_count = total_data_count)
		else:
			return items_num_format(code = 500, ok = False, msg = 'error api invoked!')
	else:
		kw.pop('table')

	table = table.strip()

	total_data_count = 0

	if kw:

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' = ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' = ?'

			if(isinstance(v,str)):
				args_list.append(v.encode('utf-8'))
			else:
				args_list.append(v)

		if table == 'u_r_author':
			try:
				total_data_count = yield from U_R_Author.getNumber(where = where_str, args = args_list)	
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_university':
			try:
				total_data_count = yield from U_R_University.getNumber(where = where_str, args = args_list)	
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_conference':
			try:
				total_data_count = yield from U_R_Conference.getNumber(where = where_str, args = args_list)	
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_literature':
			u_id = kw.get('u_id', None)
			if u_id:
				if gl.U_R_TDC.get(u_id, None):
					pass			
				else:
					try:
						gl.U_R_TDC[u_id] = yield from U_R_Literature.getNumber(where = where_str, args = args_list)	
					except Exception as e:
						return items_num_format(code = 500, ok = False, msg = str(e))
				total_data_count = gl.U_R_TDC[u_id]	
			else:
				try:
					total_data_count = yield from U_R_Literature.getNumber(where = where_str, args = args_list)	
				except Exception as e:
					return items_num_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_written_by':
			try:
				total_data_count = yield from U_R_Written_By.getNumber(where = where_str, args = args_list)	
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_affiliated_with':
			try:
				total_data_count = yield from U_R_Affiliated_With.getNumber(where = where_str, args = args_list)	
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))
		else:
			return items_num_format(code = 500, ok = False, msg = table + ' is not exist!')
	else:
		if table == 'u_r_author':
			try:
				total_data_count = yield from U_R_Author.getNumber()	
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_university':
			try:
				total_data_count = yield from U_R_University.getNumber()	
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_conference':
			try:
				total_data_count = yield from U_R_Conference.getNumber()	
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_literature':
			if gl.U_R_LITERATURE_TDC == -1:
				try:
					gl.U_R_LITERATURE_TDC = yield from U_R_Literature.getNumber()
				except Exception as e:
					return items_num_format(code = 500, ok = False, msg = str(e))
			total_data_count = gl.U_R_LITERATURE_TDC
		elif table == 'u_r_written_by':
			try:
				total_data_count = yield from U_R_Written_By.getNumber()	
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))
		elif table == 'u_r_affiliated_with':
			try:
				total_data_count = yield from U_R_Affiliated_With.getNumber()	
			except Exception as e:
				return items_num_format(code = 500, ok = False, msg = str(e))
		else:
			return items_num_format(code = 500, ok = False, msg = table + ' is not exist!')				

	return items_num_format(total_data_count = total_data_count)


############################################################################################
#                                   API for p_t_*
############################################################################################

@post('/api/p_t_/items')
def p_t_insert_items(*, table, item):
	if not isinstance(item, dict):
		raise APIValueError('data', message = 'data\'s type should be a dict')

	if table is None:
		raise APIValueError('data', message = 'table\'s value should be defined')

	iid = next_id()
	item_obj = None
	if table == 'p_t_repo':
		item_obj = P_T_Repo(id = iid, **item)
		yield from item_obj.save()
		return item_obj.id
	elif table == 'p_t_field':		
		item_obj = P_T_Field(id = iid, **item)
		yield from item_obj.save()
		return item_obj.id
	elif table == 'p_t_belong_to':
		item_obj = P_T_Belong_To(**item)
		yield from item_obj.save()
		return item_obj

	try:
		gl.P_T_REPO_TDC = yield from P_T_Repo.getNumber()
		gl.P_T_FIELD_TDC = yield from P_T_Field.getNumber()
	except Exception as e:
		pass

@get('/api/p_t_/items')
def p_t_retrive_all_items(**kw):

	table = kw.get('table', None)
	if table is None:
		
		if kw:
			items = []

			orderby = kw.get('orderby', None)
			if orderby:
				kw.pop('orderby')

			p = kw.get('p', None)
			if p:
				kw.pop('p')
	
			pcount = kw.get('pcount', None)
			if pcount:
				kw.pop('pcount')

			limit = None
			if p and pcount:
				try:
					p_ = int(p)
					pcount_ = int(pcount)
				except ValueError as e:
					return data_res_format(code = 500, ok = False, msg = str(e))
				start_item_num = (p_ - 1) * pcount_
				limit = (start_item_num, pcount_)

			kw_other = {
				'orderby': orderby,
				'limit': limit
			}
			return data_res_format(p = p, pcount = pcount, data = items)
	
		else:
			return data_res_format(code = 500, ok = False, msg = 'error api invoked!')
	else:
		kw.pop('table')

	table = table.strip()

	items = []
	p = None
	pcount = None

	if kw:

		orderby = kw.get('orderby', None)
		if orderby:
			kw.pop('orderby')

		p = kw.get('p', None)
		if p:
			kw.pop('p')
	
		pcount = kw.get('pcount', None)
		if pcount:
			kw.pop('pcount')

		limit = None
		if p and pcount:
			try:
				p_ = int(p)
				pcount_ = int(pcount)
			except ValueError as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
			start_item_num = (p_ - 1) * pcount_
			limit = (start_item_num, pcount_)

		kw_other = {
			'orderby': orderby,
			'limit': limit
		}

		where_str = ''
		args_list = []
		i = 1
		for k, v in kw.items():
			if i == 1:
				where_str = k + ' = ?'
				i = i + 1
			else:
				where_str = where_str + ' and ' + k + ' = ?'

			if(isinstance(v,str)):
				args_list.append(v.encode('utf-8'))
			else:
				args_list.append(v)

		if table == 'p_t_repo':
			try:
				items = yield from P_T_Repo.findAll(where = where_str, args = args_list, **kw_other)	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'p_t_field':
			try:
				items = yield from P_T_Field.findAll(where = where_str, args = args_list, **kw_other)	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'p_t_belong_to':
			try:
				items = yield from P_T_Belong_To.findAll(where = where_str, args = args_list, **kw_other)	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		else:
			return data_res_format(code = 500, ok = False, msg = table + ' is not exist!')
	else:
		if table == 'p_t_repo':
			try:
				items = yield from P_T_Repo.findAll()	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'p_t_field':
			try:
				items = yield from P_T_Field.findAll()	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		elif table == 'p_t_belong_to':
			try:
				items = yield from P_T_Belong_To.findAll()	
			except Exception as e:
				return data_res_format(code = 500, ok = False, msg = str(e))
		else:
			return data_res_format(code = 500, ok = False, msg = table + ' is not exist!')				

	return data_res_format(p = p, pcount = pcount, data = items)

