/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50627
Source Host           : localhost:3306
Source Database       : k_base

Target Server Type    : MYSQL
Target Server Version : 50627
File Encoding         : 65001

Date: 2016-04-25 17:18:26
*/

use k_base;

grant select, insert, update, delete on k_base.* to 'base-data'@'%' identified by 'base-data';

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 'u_r_author'
-- ----------------------------
DROP TABLE IF EXISTS `u_r_author`;
CREATE TABLE `u_r_author` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `affiliation` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for 'u_r_university'
-- ----------------------------
DROP TABLE IF EXISTS `u_r_university`;
CREATE TABLE `u_r_university` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for 'u_r_conference'
-- ----------------------------
DROP TABLE IF EXISTS `u_r_conference`;
CREATE TABLE `u_r_conference` (
  `name` varchar(255) NOT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for 'u_r_literature'
-- ----------------------------
DROP TABLE IF EXISTS `u_r_literature`;
CREATE TABLE `u_r_literature` (
  `id` varchar(255) NOT NULL,
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
  `summary` varchar(1024) DEFAULT NULL,
  `author_keyword` varchar(255) DEFAULT NULL,
  `index_keyword` varchar(255) DEFAULT NULL,
  `analysis_serial_number` varchar(255) DEFAULT NULL,
  `cas` varchar(255) DEFAULT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `manufacturer` varchar(255) DEFAULT NULL,
  `funding_info` varchar(255) DEFAULT NULL,
  `references` varchar(255) DEFAULT NULL,
  `postal_addr` varchar(255) DEFAULT NULL,
  `editor` varchar(255) DEFAULT NULL,
  `funding_agent` varchar(255) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `conference_name` varchar(255) DEFAULT NULL,
  `issn` varchar(255) DEFAULT NULL,
  `isbn` varchar(255) DEFAULT NULL,
  `coden` varchar(255) DEFAULT NULL,
  `pubmed_id` varchar(255) DEFAULT NULL,
  `language` varchar(255) DEFAULT NULL,
  `orginal_publication_abbr` varchar(255) DEFAULT NULL,
  `paper_type` varchar(255) DEFAULT NULL,
  `source_of_publication` varchar(255) DEFAULT NULL,
  `eid` varchar(64) DEFAULT NULL,
  `u_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`conference_name`) REFERENCES `u_r_conference` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for 'u_r_written_by'
-- ----------------------------
DROP TABLE IF EXISTS `u_r_written_by`;
CREATE TABLE `u_r_written_by` (
  `literature_id` varchar(255) NOT NULL,
  `author_id` varchar(255) NOT NULL,
  PRIMARY KEY (`literature_id`,`author_id`),
  FOREIGN KEY (`literature_id`) REFERENCES `u_r_literature`(`id`),
  FOREIGN KEY (`author_id`) REFERENCES `u_r_author`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for 'u_r_affiliated_with'
-- ----------------------------
DROP TABLE IF EXISTS `u_r_affiliated_with`;
CREATE TABLE `u_r_affiliated_with` (
  `author_id` varchar(255) NOT NULL,
  `university_id` varchar(255) NOT NULL,
  PRIMARY KEY (`author_id`,`university_id`),
  FOREIGN KEY (`author_id`) REFERENCES `u_r_author`(`id`),
  FOREIGN KEY (`university_id`) REFERENCES `u_r_university`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;


CREATE UNIQUE INDEX literature_index ON u_r_literature (`id`);
CREATE UNIQUE INDEX author_index ON u_r_author (`id`);
CREATE UNIQUE INDEX university_index ON u_r_university (`id`);
CREATE UNIQUE INDEX conference_index ON u_r_conference (`name`);
