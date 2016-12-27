#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LM'

import json, time, asyncio, logging
logging.basicConfig(level = logging.INFO)
from datetime import datetime
from elasticsearch import Elasticsearch

from field import Field

def create_es_client(**kw):
	logging.info('create es connection client...')
	global __es
	try:
		__es = Elasticsearch([{'host': kw.get('host', 'localhost'), 'port': kw.get('port', 9200)}])
		
	except Exception as e:
		logging.info('create es connection client error: %s' % str(e))
		sys.exit()


def do_search(index, body):

	return __es.search(index = index, body = body)

		
class ESModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		if name == 'ESModel':
			return type.__new__(cls, name, bases, attrs)
			
		index = attrs.get('__index__', None) or name
		logging.info('found model: %s (index table: %s)' % (name, index))

		mappings = dict()
		fields = []
		for k, v in attrs.items():
			if isinstance(v, Field):
				logging.info(' found mapping: %s ==> %s' % (k, v))
				mappings[k] = v
				fields.append(k)
		for k in mappings.keys():
			attrs.pop(k)
		
		attrs['__index__'] = index
		attrs['__mappings__'] = mappings
		attrs['__fields__'] = fields
		
		return type.__new__(cls, name, bases, attrs)
		
class ESModel(dict, metaclass=ESModelMetaclass):
	def __init__(self, **kw):
		super(ESModel, self).__init__(**kw)
	
	@classmethod
	@asyncio.coroutine		
	def searchAll(cls, keywords, search_type=2, min_match='75%', t_boost=2, s_boost=1, max_results = 100):

		query1 = {
		          'from': 0, 
				  'size': max_results,
		          'query': {
				     'bool': {
						'should': [
						           {'match': {'title': {'query': keywords, 'minimum_should_match': min_match, 'boost': t_boost}}}, 
								   {'match': {'summary': {'query': keywords, 'minimum_should_match': min_match, 'boost': s_boost}}}
								  ]
							 }
						   }
		        }
		query2 = {
		           'from': 0,
                   'size': max_results,				   
		           'query': {
				      'multi_match': {
					     'query': keywords,
						 'type': 'best_fields',
						 'fields': ['title', 'summary']
					  }
				    }
		         }

		if search_type == 1:
			res = do_search(index=cls.__index__, body=query1)
		elif search_type == 2:
			res = do_search(index=cls.__index__, body=query2)
		else:
			raise ValueError('Invalid search_type value: %s' % str(search_type))
	

		r_l = []
		for r in res['hits']['hits']:
			r_d = {}
			r_d['id'] = r['_id']
			r_d['type'] = r['_type']
			r_d['summary'] = r['_source']['summary']
			r_d['title'] = r['_source']['title']
			r_l.append(r_d)

		return [cls(**p) for p in r_l]

