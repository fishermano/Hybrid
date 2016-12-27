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

loop = asyncio.get_event_loop()
with aiohttp.ClientSession(loop=loop) as session:
	tasks = [fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'), fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items'),fetch_data(session, 'http://192.168.217.128/api/logs/items')]
	content = loop.run_until_complete(asyncio.wait(tasks))
	print(content)	
