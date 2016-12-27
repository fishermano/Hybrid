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
-- Table structure for 'ebook_repo'
-- ----------------------------
DROP TABLE IF EXISTS `ebook_repo`;
CREATE TABLE `ebook_repo` (
  `id` varchar(255) NOT NULL,
  `isbn` varchar(64) DEFAULT NULL,
  `eisbn` varchar(64) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `page_counter` varchar(64) DEFAULT NULL,
  `place_published` varchar(64) DEFAULT NULL,
  `publisher` varchar(64) DEFAULT NULL,
  `year` int(8) DEFAULT NULL,
  `series_identification` varchar(64) DEFAULT NULL,
  `series_name` varchar(64) DEFAULT NULL,
  `series_id` varchar(64) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `img_url` varchar(255) DEFAULT NULL,
  `summary` text DEFAULT NULL,
  `keys_or_subjects` varchar(255) DEFAULT NULL,
  `language` varchar(64) DEFAULT NULL,
  `class_num` varchar(64) DEFAULT NULL,
  `nation` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
