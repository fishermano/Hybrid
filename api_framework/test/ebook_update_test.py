#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

import aiohttp, asyncio
import json

async def fetch_data(session, url):
	with aiohttp.Timeout(10):
		async with session.get(url) as response:
			assert response.status == 200
			return await response.read()

async def ebook_data(client, data, headers):
	r = await client.post('http://1.85.37.132/api/ebook/update/items', data=json.dumps(data), headers = headers)
	await r.release()


loop = asyncio.get_event_loop()
with aiohttp.ClientSession(loop=loop) as session:
	content = loop.run_until_complete(
		fetch_data(session, 'http://1.85.37.132/api/ebook/items'))
	content_json = json.loads(content.decode())

	headers = {'content-type': 'application/json'}
	for item in content_json['data']:
		print(item['id'])
		print(item['url'])

		if item['img_url']:
			pass
		else:
			print('need to update')
			'''
				crawler code

				according to the url to fetch the image url and equal to img_url
			img_url = 
		

			item_ = {'id':item['id'], 'img_url': img_url}

			items = []
			items.append(item_)
			data = {'items':items}
			loop.run_until_complete(ebook_data(session, data, headers))
			'''
		
