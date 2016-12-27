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
-- Table structure for 'conf_repo'
-- ----------------------------
DROP TABLE IF EXISTS `conf_repo`;
CREATE TABLE `conf_repo` (
  `id` varchar(255) NOT NULL,
  `conference_name` varchar(255) DEFAULT NULL,
  `organizer` varchar(64) DEFAULT NULL,
  `language` varchar(64) DEFAULT NULL,
  `eligibility` varchar(64) DEFAULT NULL,
  `start_date` varchar(64) DEFAULT NULL,
  `end_date` varchar(64) DEFAULT NULL,
  `location` varchar(64) DEFAULT NULL,
  `country_region` varchar(64) DEFAULT NULL,
  `manuscript_last_day` varchar(64) DEFAULT NULL,
  `abstract_last_day` varchar(64) DEFAULT NULL,
  `other_contacts` varchar(255) DEFAULT NULL,
  `broad_theme` varchar(64) DEFAULT NULL,
  `classify` varchar(64) DEFAULT NULL,
  `subject` varchar(64) DEFAULT NULL,
  `range_` varchar(64) DEFAULT NULL,
  `publication_name` varchar(64) DEFAULT NULL,
  `url` varchar(64) DEFAULT NULL,
  `update_` varchar(64) DEFAULT NULL,
  `include_num` varchar(64) DEFAULT NULL,
  `db` varchar(64) DEFAULT NULL,
  `important_date` varchar(64) DEFAULT NULL,
  `created_at` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

