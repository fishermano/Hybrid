/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50528
Source Host           : localhost:3306
Source Database       : djangotest

Target Server Type    : MYSQL
Target Server Version : 50528
File Encoding         : 65001

Date: 2016-06-30 17:04:15
*/

use k_base;

grant select, insert, update, delete on k_base.* to 'base-data'@'%' identified by 'base-data';

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sr_post_topic
-- ----------------------------
DROP TABLE IF EXISTS `sr_post_topic`;
CREATE TABLE `sr_post_topic` (
  `post_id` varchar(255) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `similarity` double DEFAULT NULL,
  `post_time` datetime DEFAULT NULL,
  PRIMARY KEY (`post_id`,`topic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
