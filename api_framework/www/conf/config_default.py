#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

configs = {
	'debug': True,
	'db':{
		'host': '127.0.0.1',
		'port': 3306,
		'user': 'base-data',
		'password': 'base-data',
		'db': 'k_base'
	},
	'server':{
		'host': '127.0.0.1',
		'port': 9000
	},
	'escaped_fields':{
		'vod_repo': ['title'],
		'institution_repo': ['title'],
		'uansr_repo': ['title'],
		'ebook_repo': ['title'],
		'patent_repo': ['title'],
		'dissertation_repo': ['title'],
		'oa_repo': ['literature_title'],
		'journal_repo': ['name'],
		'u_r_literature': ['title'],
		'p_t_repo': ['title']
	},
	'mongo_db':{
		'host': '127.0.0.1',
		'port': 27017,
		'max_pool_size': 1
	},
	'es':{
		'host': '127.0.0.1',
		'port': 9200
	}
}
