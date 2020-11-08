
DROP TABLE IF EXISTS `data`;
CREATE TABLE `data` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `country` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `Lat` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `Lon` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `country_code` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `province` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `city` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `city_code` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `cases` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `stat_date` datetime DEFAULT NULL,
  `active` int(11) DEFAULT NULL,
  `Recovered` int(11) DEFAULT NULL,
  `Deaths` int(11) DEFAULT NULL,
  `Confirmed` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84153 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

SET FOREIGN_KEY_CHECKS = 1;
