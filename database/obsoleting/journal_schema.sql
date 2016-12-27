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
-- Table structure for 'journal_repo'
-- ----------------------------
DROP TABLE IF EXISTS `journal_repo`;
CREATE TABLE `journal_repo` (
  `id` varchar(255) NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  `label` varchar(64) DEFAULT NULL,
  `db_affiliation` varchar(255) DEFAULT NULL,
  `eissn` varchar(64) DEFAULT NULL,
  `pissn` varchar(64) DEFAULT NULL,
  `unified_id` varchar(64) DEFAULT NULL,
  `url` varchar(64) DEFAULT NULL,
  `lib_url` varchar(64) DEFAULT NULL,
  `type` varchar(64) DEFAULT NULL,
  `language` varchar(64) DEFAULT NULL,
  `access_mode` tinyint(4) DEFAULT NULL,
  `discipline_classified` varchar(64) DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  `journal_created` tinyint(4) DEFAULT NULL,
  `keywords` varchar(64) DEFAULT NULL,
  `sponsor` varchar(64) DEFAULT NULL,
  `editor_affiliation` varchar(64) DEFAULT NULL,
  `nationality` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
