#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

from field import StringField, BooleanField, IntegerField, FloatField, TextField, DateTimeField, MediumBlobField

from tools import next_id, cur_timestamp
from config import configs
from .orm import Model

class SR_News_Result(Model):
	__table__ = 'sr_news_result'

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	title = StringField(column_type = 'varchar(255)')
	site_name = StringField(column_type = 'varchar(255)')
	url = StringField(column_type = 'varchar(255)')
	post_time = StringField(column_type = 'varchar(64)')
	related_topic = StringField(column_type = 'varchar(255)')

class SR_Topics_Result(Model):
	__table__ = 'sr_topics_result'

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	keywords = StringField(column_type = 'varchar(64)')
	summary = StringField(column_type = 'varchar(255)')
	topic_time = StringField(column_type = 'varchar(64)')
	doc_num = IntegerField(column_type = 'int(32)')

class Top_Companies_Repo(Model):
	__table__ = 'top_companies_repo'

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	id_of_proquest = StringField(column_type = 'varchar(20)')
	summary = TextField()
	company_organization = StringField(column_type = 'varchar(128)')
	subject = StringField(column_type = 'varchar(256)')
	location = StringField(column_type = 'varchar(256)')
	publisher = StringField(column_type = 'varchar(128)')
	publication_year = StringField(column_type = 'varchar(64)')
	language_of_publication = StringField(column_type = 'varchar(64)')
	document_type = StringField(column_type = 'varchar(64)')
	fact_sheet = TextField()
	overview = TextField()
	history = TextField()
	people = TextField()
	products = TextField()
	subsidiaries = TextField()
	competitors = TextField()
	financials = TextField()

class Conf_Repo(Model):
	__table__ = 'conf_repo'

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	conference_name = StringField(column_type = 'varchar(255)')
	organizer = StringField(column_type = 'varchar(64)')
	language = StringField(column_type = 'varchar(64)')
	eligibility = StringField(column_type = 'varchar(64)')
	start_date = StringField(column_type = 'varchar(64)')
	end_date = StringField(column_type = 'varchar(64)')
	location = StringField(column_type = 'varchar(64)')
	country_region = StringField(column_type = 'varchar(64)')
	manuscript_last_day = StringField(column_type = 'varchar(64)')
	abstract_last_day = StringField(column_type = 'varchar(64)')
	other_contacts = StringField(column_type = 'varchar(255)')
	broad_theme = StringField(column_type = 'varchar(64)')
	classify = StringField(column_type = 'varchar(64)')
	subject = StringField(column_type = 'varchar(64)')
	range_ = StringField(column_type = 'varchar(64)')
	publication_name = StringField(column_type = 'varchar(64)')
	url = StringField(column_type = 'varchar(64)')
	update_ = StringField(column_type = 'varchar(64)')
	include_num = StringField(column_type = 'varchar(64)')
	db = StringField(column_type = 'varchar(64)')
	important_date = StringField(column_type = 'varchar(64)')
	created_at = IntegerField(default=cur_timestamp)

class Crawler_Repo(Model):
	__table__ = 'crawler_repo'

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	title = StringField(column_type = 'varchar(64)')
	content = TextField()
	info_type = StringField(column_type = 'varchar(64)')
	language = StringField(column_type = 'varchar(64)')
	url = StringField(column_type = 'varchar(255)')
	site_name = StringField(column_type = 'varchar(64)')
	image_url = StringField(column_type = 'varchar(255)')
	post_at = DateTimeField()
	created_at = IntegerField(default=cur_timestamp)

class Journal_Repo(Model):
	__table__ = 'journal_repo'
	__selected_escaped_fields__ = configs.escaped_fields.journal_repo

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	name = StringField(column_type = 'varchar(64)')
	label = StringField(column_type = 'varchar(64)')
	db_affiliation = StringField(column_type = 'varchar(255)')
	eissn = StringField(column_type = 'varchar(64)')
	pissn = StringField(column_type = 'varchar(64)')
	unified_id = StringField(column_type = 'varchar(64)')
	url = StringField(column_type = 'varchar(64)')
	lib_url = StringField(column_type = 'varchar(64)')
	type = StringField(column_type = 'varchar(64)')
	language = StringField(column_type = 'varchar(64)')
	access_mode = IntegerField(column_type = 'tinyint(4)')
	discipline_classified = StringField(column_type = 'varchar(64)')
	status = IntegerField(column_type = 'tinyint(4)')
	journal_created = IntegerField(column_type = 'tinyint(4)')
	keywords = StringField(column_type = 'varchar(64)')
	sponsor = StringField(column_type = 'varchar(64)')
	editor_affiliation = StringField(column_type = 'varchar(64)')
	nationality = StringField(column_type = 'varchar(64)')

class Oa_Repo(Model):
	__table__ = 'oa_repo'
	__selected_escaped_fields__ = configs.escaped_fields.oa_repo

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	first_subject = StringField(column_type = 'varchar(255)')
	second_subject = StringField(column_type = 'varchar(255)')
	literature_title = StringField(column_type = 'varchar(255)')
	abstract = TextField()
	url = StringField(column_type = 'varchar(255)')
	author = StringField(column_type = 'varchar(255)')
	journal_title = StringField(column_type = 'varchar(255)')
	journal_volume = StringField(column_type = 'varchar(64)')
	journal_number = StringField(column_type = 'varchar(64)')
	year = IntegerField(column_type = 'tinyint(4)')
	doi = StringField(column_type = 'varchar(64)')


class Vod_Repo(Model):
	__table__ = 'vod_repo'
	__selected_escaped_fields__ = configs.escaped_fields.vod_repo

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	title = StringField(column_type = 'varchar(64)')
	sort_id = StringField(column_type = 'varchar(64)')
	content = TextField()
	url = StringField(column_type = 'varchar(255)')
	keywords = StringField(column_type = 'varchar(64)')

class Institution_Repo(Model):
	__table__ = 'institution_repo'
	__selected_escaped_fields__ = configs.escaped_fields.institution_repo

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	reference_type = StringField(column_type = 'varchar(64)')
	uid = StringField(column_type = 'varchar(64)')
	author = StringField(column_type = 'varchar(255)')
	year = IntegerField(column_type = 'tinyint(4)')
	title = StringField(column_type = 'varchar(255)')
	priority = StringField(column_type = 'varchar(64)')
	star = StringField(column_type = 'varchar(64)')
	url = StringField(column_type = 'varchar(255)')
	secondary_author = StringField(column_type = 'varchar(255)')
	secondary_title = StringField(column_type = 'varchar(255)')
	place_published = StringField(column_type = 'varchar(64)')
	publisher = StringField(column_type = 'varchar(255)')
	journal = StringField(column_type = 'varchar(255)')
	volume = StringField(column_type = 'varchar(64)')
	issue = StringField(column_type = 'varchar(64)')
	number_of_volumes = StringField(column_type = 'varchar(255)')
	number = StringField(column_type = 'varchar(255)')
	pages = IntegerField(column_type = 'int(16)')
	number_of_words = IntegerField(column_type = 'int(16)')
	price = IntegerField(column_type = 'int(16)')
	section = StringField(column_type = 'varchar(64)')
	tertiary_author = StringField(column_type = 'varchar(255)')
	tertiary_title = StringField(column_type = 'varchar(255)')
	cited_count = IntegerField(column_type = 'int(16)')
	num_of_bibliographies = IntegerField(column_type = 'int(16)')
	bibliographies = StringField(column_type = 'varchar(1024)')
	edition = IntegerField(column_type = 'int(16)')
	doi = StringField(column_type = 'varchar(255)')
	date_displayed = DateTimeField()
	date = DateTimeField()
	type_of_work = StringField(column_type = 'varchar(255)')
	subsidiary_author = StringField(column_type = 'varchar(255)')
	short_title = StringField(column_type = 'varchar(255)')
	alternate_title = StringField(column_type = 'varchar(255)')
	isbn_or_issn = StringField(column_type = 'varchar(255)')
	original_publication = StringField(column_type = 'varchar(255)')
	reprint_edition = StringField(column_type = 'varchar(255)')
	reviewed_item = StringField(column_type = 'varchar(255)')
	accession_number = StringField(column_type = 'varchar(255)')
	call_number = StringField(column_type = 'varchar(255)')
	subject_category = StringField(column_type = 'varchar(255)')
	category = StringField(column_type = 'varchar(255)')
	tags = StringField(column_type = 'varchar(255)')
	bib_tex_key = StringField(column_type = 'varchar(255)')
	keywords = StringField(column_type = 'varchar(255)')
	subject_headings = StringField(column_type = 'varchar(255)')
	summary = StringField(column_type = 'varchar(1024)')
	impact_factor = IntegerField(column_type = 'int(16)')
	collection_scope = StringField(column_type = 'varchar(255)')
	subject = StringField(column_type = 'varchar(255)')
	memo = StringField(column_type = 'varchar(255)')
	image = StringField(column_type = 'varchar(255)')
	funding = StringField(column_type = 'varchar(255)')
	author_affiliation = StringField(column_type = 'varchar(255)')
	author_address = StringField(column_type = 'varchar(255)')
	caption = StringField(column_type = 'varchar(255)')
	translated_author = StringField(column_type = 'varchar(255)')
	translated_title = StringField(column_type = 'varchar(255)')
	translated_place_published = StringField(column_type = 'varchar(255)')
	translated_publisher = StringField(column_type = 'varchar(255)')
	database_provider = StringField(column_type = 'varchar(255)')
	language = StringField(column_type = 'varchar(255)')
	country = StringField(column_type = 'varchar(255)')
	date_accessed = DateTimeField()
	date_created = DateTimeField()
	date_modified = DateTimeField()
	custom_1 = StringField(column_type = 'varchar(255)')
	custom_2 = StringField(column_type = 'varchar(255)')
	custom_3 = StringField(column_type = 'varchar(255)')
	custom_4 = StringField(column_type = 'varchar(255)')
	custom_5 = StringField(column_type = 'varchar(255)')
	custom_integer_1 = IntegerField(column_type = 'int(16)')
	custom_integer_2 = IntegerField(column_type = 'int(16)')
	custom_integer_3 = IntegerField(column_type = 'int(16)')
	custom_integer_4 = IntegerField(column_type = 'int(16)')
	custom_integer_5 = IntegerField(column_type = 'int(16)')

class Uansr_Repo(Model):

	__table__ = 'uansr_repo'
	__selected_escaped_fields__ = configs.escaped_fields.uansr_repo

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	author = StringField(column_type = 'varchar(255)')
	title = StringField(column_type = 'varchar(255)')
	year = IntegerField(column_type = 'tinyint(4)')
	orginal_publication = StringField(column_type = 'varchar(255)')
	volume = StringField(column_type = 'varchar(64)')
	issue = StringField(column_type = 'varchar(64)')
	paper_id = IntegerField(column_type = 'int(16)')
	start_page = IntegerField(column_type = 'int(16)')
	end_page = IntegerField(column_type = 'int(16)')
	page_counter = IntegerField(column_type = 'int(16)')
	citing_paper = StringField(column_type = 'varchar(255)')
	doi = StringField(column_type = 'varchar(255)')
	url = StringField(column_type = 'varchar(255)')
	institution_owner = StringField(column_type = 'varchar(255)')
	author_with_institution = StringField(column_type = 'varchar(255)')
	summary = StringField(column_type = 'varchar(1024)')
	author_keyword = StringField(column_type = 'varchar(255)')
	index_keyword = StringField(column_type = 'varchar(255)')
	analysis_serial_number = StringField(column_type = 'varchar(255)')
	cas = StringField(column_type = 'varchar(255)')
	brand = StringField(column_type = 'varchar(255)')
	manufacturer = StringField(column_type = 'varchar(255)')
	funding_info = StringField(column_type = 'varchar(255)')
	reference = StringField(column_type = 'varchar(255)')
	address = StringField(column_type = 'varchar(255)')
	editor = StringField(column_type = 'varchar(255)')
	funding_agent = StringField(column_type = 'varchar(255)')
	publisher = StringField(column_type = 'varchar(255)')
	conference_title = StringField(column_type = 'varchar(255)')
	conference_date = DateTimeField()
	conference_location = StringField(column_type = 'varchar(255)')
	conference_code = StringField(column_type = 'varchar(255)')
	issn = StringField(column_type = 'varchar(255)')
	isbn = StringField(column_type = 'varchar(255)')
	coden = StringField(column_type = 'varchar(255)')
	pubmed_id = StringField(column_type = 'varchar(255)')
	language = StringField(column_type = 'varchar(255)')
	orginal_publication_abbr = StringField(column_type = 'varchar(255)')
	paper_type = StringField(column_type = 'varchar(255)')
	source_of_publication = StringField(column_type = 'varchar(255)')
	eid = StringField(column_type = 'varchar(64)')

class Ebook_Repo(Model):
	__table__ = 'ebook_repo'
	__selected_escaped_fields__ = configs.escaped_fields.ebook_repo

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	isbn = StringField(column_type = 'varchar(64)')
	eisbn = StringField(column_type = 'varchar(64)')
	author = StringField(column_type = 'varchar(255)')
	title = StringField(column_type = 'varchar(255)')
	page_counter = StringField(column_type = 'varchar(64)')
	place_published = StringField(column_type = 'varchar(64)')
	publisher = StringField(column_type = 'varchar(64)')
	year = IntegerField(column_type = 'tinyint(4)')
	series_identification = StringField(column_type = 'varchar(64)')
	series_name = StringField(column_type = 'varchar(64)')
	series_id = StringField(column_type = 'varchar(64)')
	url = StringField(column_type = 'varchar(255)')
	img_url = StringField(column_type = 'varchar(255)')
	summary = TextField()
	keys_or_subjects = StringField(column_type = 'varchar(255)')
	language = StringField(column_type = 'varchar(64)')
	class_num = StringField(column_type = 'varchar(64)')
	nation = StringField(column_type = 'varchar(64)')

class Patent_Repo(Model):
	__table__ = 'patent_repo'
	__selected_escaped_fields__ = configs.escaped_fields.patent_repo

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')

	patent_number = StringField(column_type = 'varchar(64)')
	title = StringField(column_type = 'varchar(255)')
	inventor = StringField(column_type = 'varchar(64)')
	assignee_name_or_code = StringField(column_type = 'varchar(64)')
	pan = StringField(column_type = 'varchar(255)')
	summary = StringField(column_type = 'varchar(255)')
	extension_summary = StringField(column_type = 'varchar(255)')
	euivalent_summary = StringField(column_type = 'varchar(255)')
	class_code = StringField(column_type = 'varchar(64)')
	manual_code = StringField(column_type = 'varchar(64)')
	ipc = StringField(column_type = 'varchar(64)')
	patent_details = StringField(column_type = 'varchar(255)')
	app_details = StringField(column_type = 'varchar(64)')
	further_app_details = StringField(column_type = 'varchar(64)')
	priority_app_info_date = StringField(column_type = 'varchar(64)')
	designated_states = StringField(column_type = 'varchar(64)')
	field_of_search = StringField(column_type = 'varchar(64)')
	citing_patents = StringField(column_type = 'varchar(255)')
	citing_reference = StringField(column_type = 'varchar(255)')
	dn = StringField(column_type = 'varchar(64)')
	mn = StringField(column_type = 'varchar(64)')
	ring_index_nums = StringField(column_type = 'varchar(64)')
	cited_inventor = StringField(column_type = 'varchar(255)')
	derwent_registry_nums = StringField(column_type = 'varchar(255)')


class Dissertation_Repo(Model):
	__table__ = 'dissertation_repo'
	__selected_escaped_fields__ = configs.escaped_fields.dissertation_repo

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	title = StringField(column_type = 'varchar(255)')
	title_spelling = StringField(column_type = 'varchar(255)')
	name = StringField(column_type = 'varchar(64)')
	name_spelling = StringField(column_type = 'varchar(64)')
	student_id = StringField(column_type = 'varchar(64)')
	university = StringField(column_type = 'varchar(64)')
	school = StringField(column_type = 'varchar(64)')
	discipline = StringField(column_type = 'varchar(64)')
	major = StringField(column_type = 'varchar(64)')
	degree = StringField(column_type = 'varchar(64)')
	degree_type = StringField(column_type = 'varchar(64)')
	oral_defense_date = DateTimeField()
	secret_level = StringField(column_type = 'varchar(64)')
	submitting_date = StringField(column_type = 'varchar(64)')
	foreign_title = StringField(column_type = 'varchar(255)')
	mentor_name = StringField(column_type = 'varchar(64)')
	mentor_work_unit = StringField(column_type = 'varchar(64)')
	chinese_keywords = StringField(column_type = 'varchar(64)')
	english_keywords = StringField(column_type = 'varchar(64)')
	total_pages = IntegerField(column_type = 'int(16)')
	num_of_bibliography = IntegerField(column_type = 'int(16)')
	chinese_abstract = StringField(column_type = 'varchar(1024)')
	english_abstract = StringField(column_type = 'varchar(1024)')
	nationality = StringField(column_type = 'varchar(64)')
	discipline_code = StringField(column_type = 'varchar(64)')
	last_updated = DateTimeField()
	call_num = StringField(column_type = 'varchar(64)')
	full_text = StringField(column_type = 'varchar(64)')

class U_R_Literature(Model):

	__table__ = 'u_r_literature'
	__selected_escaped_fields__ = configs.escaped_fields.u_r_literature

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	title = StringField(column_type = 'varchar(255)')
	year = IntegerField(column_type = 'tinyint(4)')
	orginal_publication = StringField(column_type = 'varchar(255)')
	volume = StringField(column_type = 'varchar(64)')
	issue = StringField(column_type = 'varchar(64)')
	paper_id = IntegerField(column_type = 'int(16)')
	start_page = IntegerField(column_type = 'int(16)')
	end_page = IntegerField(column_type = 'int(16)')
	page_counter = IntegerField(column_type = 'int(16)')
	citing_paper = StringField(column_type = 'varchar(255)')
	doi = StringField(column_type = 'varchar(255)')
	url = StringField(column_type = 'varchar(255)')
	summary = StringField(column_type = 'varchar(1024)')
	author_keyword = StringField(column_type = 'varchar(255)')
	index_keyword = StringField(column_type = 'varchar(255)')
	analysis_serial_number = StringField(column_type = 'varchar(255)')
	cas = StringField(column_type = 'varchar(255)')
	brand = StringField(column_type = 'varchar(255)')
	manufacturer = StringField(column_type = 'varchar(255)')
	funding_info = StringField(column_type = 'varchar(255)')
	references = StringField(column_type = 'varchar(255)')
	postal_addr = StringField(column_type = 'varchar(255)')
	editor = StringField(column_type = 'varchar(255)')
	funding_agent = StringField(column_type = 'varchar(255)')
	publisher = StringField(column_type = 'varchar(255)')
	conference_name = StringField(column_type = 'varchar(255)')
	issn = StringField(column_type = 'varchar(255)')
	isbn = StringField(column_type = 'varchar(255)')
	coden = StringField(column_type = 'varchar(255)')
	pubmed_id = StringField(column_type = 'varchar(255)')
	language = StringField(column_type = 'varchar(255)')
	orginal_publication_abbr = StringField(column_type = 'varchar(255)')
	paper_type = StringField(column_type = 'varchar(255)')
	source_of_publication = StringField(column_type = 'varchar(255)')
	eid = StringField(column_type = 'varchar(64)')
	u_id = StringField(column_type = 'varchar(255)')

class U_R_Author(Model):

	__table__ = 'u_r_author'

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	name = StringField(column_type = 'varchar(255)')
	alias = StringField(column_type = 'varchar(255)')
	affiliation = StringField(column_type = 'varchar(255)')

class U_R_University(Model):

	__table__ = 'u_r_university'

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	name = StringField(column_type = 'varchar(255)')
	alias = StringField(column_type = 'varchar(255)')

class U_R_Conference(Model):

	__table__ = 'u_r_conference'

	name = StringField(primary_key = True, column_type = 'varchar(255)')
	alias = StringField(column_type = 'varchar(255)')
	date = DateTimeField()
	location = StringField(column_type = 'varchar(64)')
	code = StringField(column_type = 'varchar(64)')	

class U_R_Written_By(Model):

	__table__ = 'u_r_written_by'

	literature_id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	author_id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')

class U_R_Affiliated_With(Model):

	__table__ = 'u_r_affiliated_with'

	author_id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	university_id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')

class P_T_Repo(Model):
	__table__ = 'p_t_repo'
	__selected_escaped_fields__ = configs.escaped_fields.p_t_repo

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	year = IntegerField(column_type = 'tinyint(8)')
	patent_number = StringField(column_type = 'varchar(64)')
	title = StringField(column_type = 'varchar(255)')
	inventor = StringField(column_type = 'varchar(64)')
	assignee_name_or_code = StringField(column_type = 'varchar(64)')
	pan = StringField(column_type = 'varchar(255)')
	summary = StringField(column_type = 'varchar(255)')
	extension_summary = StringField(column_type = 'varchar(255)')
	euivalent_summary = StringField(column_type = 'varchar(255)')
	class_code = StringField(column_type = 'varchar(64)')
	manual_code = StringField(column_type = 'varchar(64)')
	ipc = StringField(column_type = 'varchar(64)')
	patent_details = StringField(column_type = 'varchar(255)')
	app_details = StringField(column_type = 'varchar(64)')
	further_app_details = StringField(column_type = 'varchar(64)')
	priority_app_info_date = StringField(column_type = 'varchar(64)')
	designated_states = StringField(column_type = 'varchar(64)')
	field_of_search = StringField(column_type = 'varchar(64)')
	citing_patents = StringField(column_type = 'varchar(255)')
	citing_reference = StringField(column_type = 'varchar(255)')
	dn = StringField(column_type = 'varchar(64)')
	mn = StringField(column_type = 'varchar(64)')
	ring_index_nums = StringField(column_type = 'varchar(64)')
	cited_inventor = StringField(column_type = 'varchar(255)')
	derwent_registry_nums = StringField(column_type = 'varchar(255)')

class P_T_Field(Model):

	__table__ = 'p_t_field'

	id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	name = StringField(column_type = 'varchar(255)')
	code = StringField(column_type = 'varchar(64)')

class P_T_Belong_To(Model):

	__table__ = 'p_t_belong_to'

	field_id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	repo_id = StringField(primary_key = True, default = next_id, column_type = 'varchar(255)')
	

