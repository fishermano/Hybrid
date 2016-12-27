/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50627
Source Host           : localhost:3306
Source Database       : k_base

Target Server Type    : MYSQL
Target Server Version : 50627
File Encoding         : 65001

Date: 2016-01-20 17:18:26
*/

/*
drop database if exists k_base;

create database k_base;
*/

use k_base;

grant select, insert, update, delete on k_base.* to 'base-data'@'%' identified by 'base-data';

SET FOREIGN_KEY_CHECKS=0;


-- ----------------------------
-- Table structure for 'institution_repo'
-- ----------------------------
DROP TABLE IF EXISTS `institution_repo`;
CREATE TABLE `institution_repo` (
  `id` varchar(255) NOT NULL,
  `reference_type` varchar(64) DEFAULT NULL,
  `uid` varchar(64) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `year` int(8) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `priority` varchar(64) DEFAULT NULL,
  `star` varchar(64) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `secondary_author` varchar(255) DEFAULT NULL,
  `secondary_title` varchar(255) DEFAULT NULL,
  `place_published` varchar(64) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `journal` varchar(255) DEFAULT NULL,
  `volume` varchar(64) DEFAULT NULL,
  `issue` varchar(64) DEFAULT NULL,
  `number_of_volumes` varchar(255) DEFAULT NULL,
  `number` varchar(255) DEFAULT NULL,
  `pages` int(16) DEFAULT NULL,
  `number_of_words` int(16) DEFAULT NULL,
  `price` int(16) DEFAULT NULL,
  `section` varchar(64) DEFAULT NULL,
  `tertiary_author` varchar(255) DEFAULT NULL,
  `tertiary_title` varchar(255) DEFAULT NULL,
  `cited_count` int(16) DEFAULT NULL,
  `num_of_bibliographies` int(16) DEFAULT NULL,
  `bibliographies` varchar(1024) DEFAULT NULL,
  `edition` int(16) DEFAULT NULL,
  `doi` varchar(255) DEFAULT NULL,
  `date_displayed` datetime DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `type_of_work` varchar(255) DEFAULT NULL,
  `subsidiary_author` varchar(255) DEFAULT NULL,
  `short_title` varchar(255) DEFAULT NULL,
  `alternate_title` varchar(255) DEFAULT NULL,
  `isbn_or_issn` varchar(255) DEFAULT NULL,
  `original_publication` varchar(255) DEFAULT NULL,
  `reprint_edition` varchar(255) DEFAULT NULL,
  `reviewed_item` varchar(255) DEFAULT NULL,
  `accession_number` varchar(255) DEFAULT NULL,
  `call_number` varchar(255) DEFAULT NULL,
  `subject_category` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL,
  `bib_tex_key` varchar(255) DEFAULT NULL,
  `keywords` varchar(255) DEFAULT NULL,
  `subject_headings` varchar(255) DEFAULT NULL,
  `summary` varchar(1024) DEFAULT NULL,
  `impact_factor` int(16) DEFAULT NULL,
  `collection_scope` varchar(255) DEFAULT NULL,
  `subject` varchar(255) DEFAULT NULL,
  `memo` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `funding` varchar(255) DEFAULT NULL,
  `author_affiliation` varchar(255) DEFAULT NULL,
  `author_address` varchar(255) DEFAULT NULL,
  `caption` varchar(255) DEFAULT NULL,
  `translated_author` varchar(255) DEFAULT NULL,
  `translated_title` varchar(255) DEFAULT NULL,
  `translated_place_published` varchar(255) DEFAULT NULL,
  `translated_publisher` varchar(255) DEFAULT NULL,
  `database_provider` varchar(255) DEFAULT NULL,
  `language` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `date_accessed` datetime DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_modified` datetime DEFAULT NULL,
  `custom_1` varchar(255) DEFAULT NULL,
  `custom_2` varchar(255) DEFAULT NULL,
  `custom_3` varchar(255) DEFAULT NULL,
  `custom_4` varchar(255) DEFAULT NULL,
  `custom_5` varchar(255) DEFAULT NULL,
  `custom_integer_1` int(16) DEFAULT NULL,
  `custom_integer_2` int(16) DEFAULT NULL,
  `custom_integer_3` int(16) DEFAULT NULL,
  `custom_integer_4` int(16) DEFAULT NULL,
  `custom_integer_5` int(16) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

