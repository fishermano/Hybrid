/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50528
Source Host           : localhost:3306
Source Database       : djangotest

Target Server Type    : MYSQL
Target Server Version : 50528
File Encoding         : 65001

Date: 2016-06-30 17:04:06
*/

use k_base;

grant select, insert, update, delete on k_base.* to 'base-data'@'%' identified by 'base-data';

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sr_post
-- ----------------------------
DROP TABLE IF EXISTS `sr_post`;
CREATE TABLE `sr_post` (
  `id` varchar(255) NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `site_name` varchar(64) DEFAULT NULL,
  `data_type` tinyint(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `content` text,
  `post_time` datetime DEFAULT NULL,
  `language_type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
