#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

import asyncio, motor, sys, logging
logging.basicConfig(level = logging.INFO)

import motor.motor_asyncio

from field import Field

from config import configs

MAX_LENGTH = None

@asyncio.coroutine
def create_client(**kw):
	logging.info('create mongodb connection client...')
	global __client

	try:
		__client = motor.motor_asyncio.AsyncIOMotorClient(kw.get('host', 'localhost'),kw.get('port', 27017))
		yield from __client.admin.command('ping')
	except Exception as e:
		logging.info('create mongodb connection client error: %s' % str(e))
		sys.exit()

#MONGODB_HOST = configs.mongo_db.get('host', 'localhost')
#MONGODB_PORT = configs.mongo_db.get('port', '27017')

@asyncio.coroutine
def do_insert(db, col, doc):
	#__client = motor.motor_asyncio.AsyncIOMotorClient('192.168.16.103', 27017)
	database = __client[db]
	collection = database[col]
	result = yield from collection.insert(doc)
	return result
	
@asyncio.coroutine
def do_remove(db, col, doc):
	#__client = motor.motor_asyncio.AsyncIOMotorClient('192.168.16.103', 27017)
	database = __client[db]
	collection = database[col]
	result = yield from collection.remove(doc)
	return result

@asyncio.coroutine
def do_update(db, col, old_doc, new_doc):
	#__client = motor.motor_asyncio.AsyncIOMotorClient('192.168.16.103', 27017)
	database = __client[db]
	collection = database[col]
	result = yield from collection.update(old_doc, new_doc)
	return result

@asyncio.coroutine
def do_find(db, col, doc, sort, limit):
	#__client = motor.motor_asyncio.AsyncIOMotorClient('192.168.16.103', 27017)
	database = __client[db]
	collection = database[col]
	if sort:
		if limit:
			cursor = collection.find(doc).sort(sort).skip((limit[0]-1)*limit[1]).limit(limit[1])
		else:
			cursor = collection.find(doc).sort(sort)
	else:
		if limit:
			cursor = collection.find(doc).skip((limit[0]-1)*limit[1]).limit(limit[1])
		else:
			cursor = collection.find(doc)
	result = yield from cursor.to_list(length = MAX_LENGTH)
	return result


class MongoDBModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		if name == 'MongoDBModel':
			return type.__new__(cls, name, bases, attrs)

		database = attrs.get('__database__', None) or name
		collection = attrs.get('__collection__', None) or name
		logging.info('found model: %s (database:collection-> %s:%s)' % (name, database, collection))

		mappings = dict()
		fields = []
		for k, v in attrs.items():
			if isinstance(v, Field):
				logging.info(' found mapping: %s ==> %s' % (k, v))
				mappings[k] = v
				fields.append(k)
		for k in mappings.keys():
			attrs.pop(k)

		attrs['__database__'] = database
		attrs['__collection__'] = collection
		attrs['__mappings__'] = mappings
		attrs['__fields__'] = fields

		return type.__new__(cls, name, bases, attrs)

class MongoDBModel(dict, metaclass=MongoDBModelMetaclass):
	def __init__(self, **kw):
		super(MongoDBModel, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'MongoModel' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def getValue(self, key):
		return getattr(self, key, None)

	def getValueOrDefault(self, key):
		value = getattr(self, key, None)
		if value is None:
			field = self.__mappings__[key]
			if field.default is not None:
				value = field.default() if callable(field.default) else field.default
				logging.debug('using default value for %s: %s' % (key, str(value)))
				setattr(self, key, value)
		return value

	@classmethod
	@asyncio.coroutine
	def find(self, doc = None, sort = None, limit = None):
		database = self.__database__
		collection = self.__collection__
		result = yield from do_find(db = database, col = collection, doc = doc, sort = sort, limit = limit)
		return result

	@classmethod
	@asyncio.coroutine
	def remove(self, doc):
		database = self.__database__
		collection = self.__collection__
		result = yield from do_remove(db = database, col = collection, doc = doc)
		return result

	@classmethod
	@asyncio.coroutine
	def update(self, old_doc, new_doc):
		database = self.__database__
		collection = self.__collection__
		result = yield from do_update(db = database, col = collection, old_doc = old_doc, new_doc = new_doc)
		return result

	@asyncio.coroutine
	def save(self):
		database = self.__database__
		collection = self.__collection__
		doc = {}
		for field in self.__fields__:
			doc[field] = self.getValueOrDefault(field)
		result = yield from do_insert(db = database, col = collection, doc = doc)
		return result

