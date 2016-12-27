#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

import aiohttp, asyncio
import json

#DB_HOST = '1.85.37.132'
DB_HOST = 'localhost'

async def fetch_data(session, url):
	with aiohttp.Timeout(10):
		async with session.get(url) as response:
			assert response.status == 200
			return await response.read()

async def crawler_data(client, data, headers):
	r = await client.post('http://1.85.37.132/api/crawler/items', data=json.dumps(data), headers = headers)
	await r.release()

loop = asyncio.get_event_loop()
with aiohttp.ClientSession(loop=loop) as session:
	content = loop.run_until_complete(
		fetch_data(session, 'http://1.85.37.132/api/ebook/items'))
	content_json = json.loads(content.decode())

	headers = {'content-type': 'application/json'}
	for item in content_json['data']:
		print(item['url'])
		print(item['id'])
		'''
			爬虫根据url抓取相应的图片url，然后把将img_url和id数据写入

		'''
		'''
			爬虫解析相关代码
			img_url = ...
		'''

		item_ = {'url':item['url'], 'title':item['id'], 'content':'test!', 'image_url':img_url}

		items = []
		for i in range(1):
			items.append(item)
		data = {'items':items}
		loop.run_until_complete(crawler_data(session, data, headers))
		
