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
-- Table structure for `crawler_repo`
-- ----------------------------
DROP TABLE IF EXISTS `crawler_repo`;
CREATE TABLE `crawler_repo` (
  `id` varchar(255) NOT NULL,
  `title` varchar(64) DEFAULT NULL,
  `content` text,
  `info_type` varchar(64) DEFAULT NULL,
  `language` varchar(64) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `site_name` varchar(64) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `post_at` datetime DEFAULT NULL,
  `created_at` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
