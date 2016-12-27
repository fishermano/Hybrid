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
DROP TABLE IF EXISTS `p_t_repo`;
CREATE TABLE `p_t_repo` (
  `id` varchar(255) NOT NULL,
  `year` int(8) DEFAULT NULL,
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

-- ----------------------------
-- Table structure for 'p_t_field'
-- ----------------------------
DROP TABLE IF EXISTS `p_t_field`;
CREATE TABLE `p_t_field` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `code` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for 'p_t_belong_to'
-- ----------------------------
DROP TABLE IF EXISTS `p_t_belong_to`;
CREATE TABLE `p_t_belong_to` (
  `field_id` varchar(255) NOT NULL,
  `repo_id` varchar(255) NOT NULL,
  PRIMARY KEY (`field_id`,`repo_id`),
  FOREIGN KEY (`field_id`) REFERENCES `p_t_field`(`id`),
  FOREIGN KEY (`repo_id`) REFERENCES `p_t_repo`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

CREATE UNIQUE INDEX repo_index ON p_t_repo (`id`);
CREATE UNIQUE INDEX field_index ON p_t_field (`id`);
