/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50528
Source Host           : localhost:3306
Source Database       : djangotest

Target Server Type    : MYSQL
Target Server Version : 50528
File Encoding         : 65001

Date: 2016-06-30 17:04:27
*/

use k_base;

grant select, insert, update, delete on k_base.* to 'base-data'@'%' identified by 'base-data';

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sr_topic
-- ----------------------------
DROP TABLE IF EXISTS `sr_topic`;
CREATE TABLE `sr_topic` (
  `topic_id` int(11) DEFAULT NULL,
  `topic_name` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `topic_keywords` char(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `language_type` int(11) DEFAULT NULL,
  `summary` text COLLATE utf8_unicode_ci,
  `doc_num` int(11) DEFAULT NULL,
  `duration_time` int(11) DEFAULT NULL,
  `median_time` varchar(255) DEFAULT NULL,
  `mean_time` varchar(255) DEFAULT NULL,
  `sen` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
