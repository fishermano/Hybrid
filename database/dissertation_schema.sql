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
-- Table structure for 'dissertation_repo'
-- ----------------------------
DROP TABLE IF EXISTS `dissertation_repo`;
CREATE TABLE `dissertation_repo` (
  `id` varchar(255) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `title_spelling` varchar(255) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  `name_spelling` varchar(64) DEFAULT NULL,
  `student_id` varchar(64) DEFAULT NULL,
  `university` varchar(64) DEFAULT NULL,
  `school` varchar(64) DEFAULT NULL,
  `discipline` varchar(64) DEFAULT NULL,
  `major` varchar(64) DEFAULT NULL,
  `degree` varchar(64) DEFAULT NULL,
  `degree_type` varchar(64) DEFAULT NULL,
  `oral_defense_date` datetime DEFAULT NULL,
  `secret_level` varchar(64) DEFAULT NULL,
  `submitting_date` varchar(64) DEFAULT NULL,
  `foreign_title` varchar(255) DEFAULT NULL,
  `mentor_name` varchar(64) DEFAULT NULL,
  `mentor_work_unit` varchar(64) DEFAULT NULL,
  `chinese_keywords` varchar(64) DEFAULT NULL,
  `english_keywords` varchar(64) DEFAULT NULL,
  `total_pages` int(16) DEFAULT NULL,
  `num_of_bibliography` int(16) DEFAULT NULL,
  `chinese_abstract` varchar(1024) DEFAULT NULL,
  `english_abstract` varchar(1024) DEFAULT NULL,
  `nationality` varchar(64) DEFAULT NULL,
  `discipline_code` varchar(64) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `call_num` varchar(64) DEFAULT NULL,
  `full_text` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
