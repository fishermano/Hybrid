#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

import aiohttp, asyncio
import json, time


COLUM_FAMILY = ['keywords', 'summary', 'doc_num', 'topic_time', 'title', 'site_name', 'url', 'post_time']
DB_HOST = '1.85.37.132'
#DB_HOST = 'localhost'

async def hot_topics_data(client, data, headers):

	for item in data['items']:

		topic_id = ''
		item_topic = {}
		data_topic = {}
		item_topic['keywords'] = item['keywords']
		item_topic['summary'] = item['summary']
		item_topic['doc_num'] = item['doc_num']
		item_topic['topic_time'] = item['topic_time']

		data_topic['item'] = item_topic
		data_topic['table'] = 'sr_topics_result'
		
		try:
			r_topic = await client.post('http://' + DB_HOST + '/api/hot_topics/items', data=json.dumps(data_topic), headers = headers)
			res_topic = await r_topic.content.readany()
			topic_id = res_topic.decode()
			await r_topic.release()
			if topic_id.startswith('<!'):
				await r_topic.release()
				return
		except Exception as e:
			await r_topic.release()
			return

		for item_t in item['related_news']:
			
			item_new = {}
			data_new = {}
			item_new['title'] = item_t['title']
			item_new['site_name'] = item_t['site_name']
			item_new['url'] = item_t['url']
			item_new['post_time'] = item_t['post_time']
			item_new['related_topic'] = topic_id

			data_new['item'] = item_new
			data_new['table'] = 'sr_news_result'

			try:
				r_new = await client.post('http://' + DB_HOST + '/api/hot_topics/items', data=json.dumps(data_new), headers = headers)
				await r_new.release()
			except Exception as e:
				await r_new.release()		
				pass
		


items = []
f = open(r'hot_topics/broken_news.json')
s = json.load(f)
f.close()

data = {'items':s['data']}
headers = {'content-type': 'application/json'}

with aiohttp.ClientSession() as client:
	tasks = [hot_topics_data(client, data, headers)]

	asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
