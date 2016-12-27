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

use k_base;

grant select, insert, update, delete on k_base.* to 'base-data'@'%' identified by 'base-data';

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 'uansr_repo'
-- ----------------------------
DROP TABLE IF EXISTS `uansr_repo`;
CREATE TABLE `uansr_repo` (
  `id` varchar(255) NOT NULL,
  `author` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `year` int(8) DEFAULT NULL,
  `orginal_publication` varchar(255) DEFAULT NULL,
  `volume` varchar(64) DEFAULT NULL,
  `issue` varchar(64) DEFAULT NULL,
  `paper_id` int(16) DEFAULT NULL,
  `start_page` int(16) DEFAULT NULL,
  `end_page` int(16) DEFAULT NULL,
  `page_counter` int(16) DEFAULT NULL,
  `citing_paper` varchar(255) DEFAULT NULL,
  `doi` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `institution_owner` varchar(255) DEFAULT NULL,
  `author_with_institution` varchar(255) DEFAULT NULL,
  `summary` varchar(1024) DEFAULT NULL,
  `author_keyword` varchar(255) DEFAULT NULL,
  `index_keyword` varchar(255) DEFAULT NULL,
  `analysis_serial_number` varchar(255) DEFAULT NULL,
  `cas` varchar(255) DEFAULT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `manufacturer` varchar(255) DEFAULT NULL,
  `funding_info` varchar(255) DEFAULT NULL,
  `reference` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `editor` varchar(255) DEFAULT NULL,
  `funding_agent` varchar(255) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `conference_title` varchar(255) DEFAULT NULL,
  `conference_date` datetime DEFAULT NULL,
  `conference_location` varchar(255) DEFAULT NULL,
  `conference_code` varchar(255) DEFAULT NULL,
  `issn` varchar(255) DEFAULT NULL,
  `isbn` varchar(255) DEFAULT NULL,
  `coden` varchar(255) DEFAULT NULL,
  `pubmed_id` varchar(255) DEFAULT NULL,
  `language` varchar(255) DEFAULT NULL,
  `orginal_publication_abbr` varchar(255) DEFAULT NULL,
  `paper_type` varchar(255) DEFAULT NULL,
  `source_of_publication` varchar(255) DEFAULT NULL,
  `eid` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
