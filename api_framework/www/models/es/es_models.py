#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LM'

from field import StringField, TextField
from .es_orm import ESModel

class Index(ESModel):
	__index__ = 'silkroad'
	
	id = StringField(column_type = 'varchar(255)')
	title = StringField(column_type = 'varchar(255)')
	type = StringField(column_type = 'varchar(64)')
	summary = TextField()
