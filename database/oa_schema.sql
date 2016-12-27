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
-- Table structure for `oa_repo`
-- ----------------------------
DROP TABLE IF EXISTS `oa_repo`;
CREATE TABLE `oa_repo` (
  `id` varchar(255) NOT NULL,
  `first_subject` varchar(255) DEFAULT NULL,
  `second_subject` varchar(255) DEFAULT NULL,
  `literature_title` varchar(255) DEFAULT NULL,
  `abstract` text DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `journal_title` varchar(255) DEFAULT NULL,
  `journal_volume` varchar(64) DEFAULT NULL,
  `journal_number` varchar(64) DEFAULT NULL,
  `year` int(8) DEFAULT NULL,
  `doi` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
