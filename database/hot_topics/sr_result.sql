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
-- Table structure for sr_news_result
-- ----------------------------
DROP TABLE IF EXISTS `sr_news_result`;
CREATE TABLE `sr_news_result` (
  `id` varchar(255) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `site_name` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `post_time` varchar(64) DEFAULT NULL,
  `related_topic` varchar(255) DEFAULT NULL, 
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for sr_topics_result
-- ----------------------------
DROP TABLE IF EXISTS `sr_topics_result`;
CREATE TABLE `sr_topics_result` (
  `id` varchar(255) NOT NULL,
  `keywords` varchar(255) DEFAULT NULL,
  `summary` varchar(255) DEFAULT NULL,
  `doc_num` int(32) DEFAULT NULL,
  `topic_time` varchar(64) DEFAULT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
