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
-- Table structure for 'patent_repo'
-- ----------------------------
DROP TABLE IF EXISTS `patent_repo`;
CREATE TABLE `patent_repo` (
  `id` varchar(255) NOT NULL,
  `patent_number` varchar(64) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `inventor` varchar(64) DEFAULT NULL,
  `assignee_name_or_code` varchar(64) DEFAULT NULL,
  `pan` varchar(255) DEFAULT NULL,
  `summary` varchar(255) DEFAULT NULL,
  `extension_summary` varchar(255) DEFAULT NULL,
  `euivalent_summary` varchar(255) DEFAULT NULL,
  `class_code` varchar(64) DEFAULT NULL,
  `manual_code` varchar(64) DEFAULT NULL,
  `ipc` varchar(64) DEFAULT NULL,
  `patent_details` varchar(255) DEFAULT NULL,
  `app_details` varchar(64) DEFAULT NULL,
  `further_app_details` varchar(64) DEFAULT NULL,
  `priority_app_info_date` varchar(64) DEFAULT NULL,
  `designated_states` varchar(64) DEFAULT NULL,
  `field_of_search` varchar(64) DEFAULT NULL,
  `citing_patents` varchar(255) DEFAULT NULL,
  `citing_reference` varchar(255) DEFAULT NULL,
  `dn` varchar(64) DEFAULT NULL,
  `mn` varchar(64) DEFAULT NULL,
  `ring_index_nums` varchar(64) DEFAULT NULL,
  `cited_inventor` varchar(255) DEFAULT NULL,
  `derwent_registry_nums` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
