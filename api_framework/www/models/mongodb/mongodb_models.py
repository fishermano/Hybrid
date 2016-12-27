#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

from datetime import date

from field import StringField, DateTimeField
from tools import next_id, today
from .mongodb_orm import MongoDBModel

class Items(MongoDBModel):
	__database__ = 'tests'
	__collection__ = 'items'

	_id = StringField(default = next_id, column_type = 'varchar(255)')
	date = DateTimeField(default = today)

class Logs(MongoDBModel):
	__database__ = 'tests'
	__collection__ = 'logs'

	_id = StringField(default = next_id, column_type = 'varchar(255)')
	item_id = StringField(column_type = 'varchar(255)')
	click_time = DateTimeField()
	user_id = StringField(column_type = 'varchar(255)')
	keywords = StringField(column_type = 'varchar(255)')
	res_id = StringField(column_type = 'varchar(255)')
	res_type = StringField(column_type = 'varchar(64)')
	operation = StringField(column_type = 'varchar(64)')
	explorer = StringField(column_type = 'varchar(64)')
	action = StringField(column_type = 'varchar(64)')
	ip = StringField(column_type = 'varchar(64)')
