#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

import aiohttp
import asyncio
import json, time, datetime

class MyJsonEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime.datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj, datetime.date):
			return obj.strftime('%Y-%m-%d')
		else:
			return json.JSONEncoder.default(self, obj)

async def crawler_data(client, data, headers):
	r = await client.post('http://localhost/api/conf/items', data=json.dumps(data, cls = MyJsonEncoder), headers = headers)
	await r.release()


item = {'classify':'www.test.com', 'range_':'this is test!', 'broad_theme':'test!', 'url':'http://img1.goepe.com/201303/1362711679_2501.jpg'}

items = []
for i in range(1):
	items.append(item)
data = {'items':items}
headers = {'content-type': 'application/json'}

with aiohttp.ClientSession() as client:
	tasks = [crawler_data(client, data, headers)]

	asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))

	
