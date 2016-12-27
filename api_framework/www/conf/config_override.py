#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

configs = {
	'server':{
		'host': '127.0.0.1'
	},
	'db': {
		'host': '192.168.16.207'
	},
	'escaped_fields':{
		'vod_repo': ['title', 'sort_id', 'content', 'url', 'keywords'],
		'institution_repo': ['title', 'author', 'keywords', 'journal', 'reference_type', 'summary', 'doi', 'volume', 'issue', 'year', 'pages', 'url', 'publisher'],
		'uansr_repo': ['title','author','year', 'orginal_publication','issn', 'paper_type', 'volume','summary','doi','url','reference'],
		'ebook_repo': ['title', 'author', 'summary', 'eisbn', 'year', 'language', 'isbn', 'url', 'img_url', 'publisher', 'page_counter'],
		'patent_repo': ['patent_number', 'title', 'inventor', 'derwent_registry_nums', 'summary', 'assignee_name_or_code', 'pan', 'ipc', 'class_code', 'manual_code', 'patent_details', 'app_details', 'priority_app_info_date'],
		'dissertation_repo': ['foreign_title','name','university','submitting_date','degree','last_updated', 'english_keywords', 'english_abstract', 'full_text'],
		'journal_repo': ['name', 'label', 'eissn', 'pissn', 'url', 'language', 'discipline_classified'],
		'u_r_literature': ['title', 'year','volume','summary','doi','url'],
		'p_t_repo': ['patent_number', 'title', 'inventor', 'derwent_registry_nums', 'summary', 'assignee_name_or_code', 'pan', 'ipc', 'class_code', 'manual_code', 'patent_details', 'app_details', 'priority_app_info_date']
	},
	'mongo_db':{
		'host': '192.168.16.103'
	},
	'es':{
		'host': '192.168.16.100'
	}
}
