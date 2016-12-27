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
-- Table structure for 'top_companies_repo'
-- ----------------------------
DROP TABLE IF EXISTS `top_companies_repo`;
CREATE TABLE `top_companies_repo` (
  `id` varchar(255) NOT NULL,
  `id_of_proquest` varchar(20) DEFAULT NULL,
  `summary` text DEFAULT NULL,
  `company_organization` varchar(128) DEFAULT NULL,
  `subject` varchar(256) DEFAULT NULL,
  `location` varchar(256) DEFAULT NULL,
  `publisher` varchar(128) DEFAULT NULL,
  `publication_year` varchar(64) DEFAULT NULL,
  `language_of_publication` varchar(64) DEFAULT NULL,
  `document_type` varchar(64) DEFAULT NULL,
  `fact_sheet` text DEFAULT NULL,
  `overview` text DEFAULT NULL,
  `history` text DEFAULT NULL,
  `people` text DEFAULT NULL,
  `products` text DEFAULT NULL,
  `subsidiaries` text DEFAULT NULL,
  `competitors` text DEFAULT NULL,
  `financials` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

