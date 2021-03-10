-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: Class404
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addresses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `addresses_user_id_d930d1dc_fk_users_id` (`user_id`),
  CONSTRAINT `addresses_user_id_d930d1dc_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
INSERT INTO `addresses` VALUES (1,'서울시 강남구 위코드',11),(2,'서울시 강남구 위코드',11),(3,'서울시 강남구 위코드',11),(4,'서울시 강남구 위코드',11),(5,'서울시 강남구 위코드',11),(6,'서울시 강남구 위코드',11),(7,'서울시 강남구 위코드',11);
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ages`
--

DROP TABLE IF EXISTS `ages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ages`
--

LOCK TABLES `ages` WRITE;
/*!40000 ALTER TABLE `ages` DISABLE KEYS */;
INSERT INTO `ages` VALUES (1,'10대'),(2,'20대'),(3,'30대'),(4,'40대'),(5,'50대');
/*!40000 ALTER TABLE `ages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brands`
--

DROP TABLE IF EXISTS `brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brands` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brands`
--

LOCK TABLES `brands` WRITE;
/*!40000 ALTER TABLE `brands` DISABLE KEYS */;
INSERT INTO `brands` VALUES (1,'취미'),(2,'수익창출'),(3,'직무, 자기개발');
/*!40000 ALTER TABLE `brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `brand_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `categories_brand_id_85e86eaa_fk_brands_id` (`brand_id`),
  CONSTRAINT `categories_brand_id_85e86eaa_fk_brands_id` FOREIGN KEY (`brand_id`) REFERENCES `brands` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'미술',1),(2,'디지털드로잉',1),(3,'사진/영상',1),(4,'음악',1),(5,'공예',1),(6,'라이프 스타일',1),(7,'요리/음료',1),(8,'운동',1),(9,'부동산/주식/재테크',2),(10,'SNS/콘텐츠',2),(11,'마인드/자기개발',2),(12,'온라인쇼핑몰',2),(13,'창업',2),(14,'비즈니스/생산성',3),(15,'데이터/개발',3),(16,'어학/외국어',3),(17,'영상/디자인',3),(18,'글쓰기/콘텐츠',3),(19,'기타',3);
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class_levels`
--

DROP TABLE IF EXISTS `class_levels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class_levels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_levels`
--

LOCK TABLES `class_levels` WRITE;
/*!40000 ALTER TABLE `class_levels` DISABLE KEYS */;
INSERT INTO `class_levels` VALUES (1,'입문자'),(2,'초급자'),(3,'중급자'),(4,'준전문가'),(5,'전문가');
/*!40000 ALTER TABLE `class_levels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `creator_info`
--

DROP TABLE IF EXISTS `creator_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `creator_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `creator_info_user_id_48cba633_fk_users_id` (`user_id`),
  CONSTRAINT `creator_info_user_id_48cba633_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creator_info`
--

LOCK TABLES `creator_info` WRITE;
/*!40000 ALTER TABLE `creator_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `creator_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'contenttypes','contenttype'),(17,'order','address'),(19,'order','order'),(18,'order','orderstatus'),(3,'product','age'),(4,'product','brand'),(5,'product','category'),(6,'product','classlevel'),(12,'product','gender'),(7,'product','product'),(11,'product','productage'),(10,'product','productimage'),(9,'product','productuserlike'),(8,'product','review'),(2,'sessions','session'),(16,'user','creatorinfo'),(15,'user','user'),(13,'user','usertier'),(14,'user','usertype');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-03-09 15:29:54.943838'),(2,'contenttypes','0002_remove_content_type_name','2021-03-09 15:29:55.512317'),(3,'user','0001_initial','2021-03-09 15:29:56.465770'),(4,'product','0001_initial','2021-03-09 15:29:59.418610'),(5,'order','0001_initial','2021-03-09 15:30:02.217099'),(6,'sessions','0001_initial','2021-03-09 15:30:03.816337');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genders`
--

DROP TABLE IF EXISTS `genders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `product_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `genders_product_id_d348706d_fk_products_id` (`product_id`),
  CONSTRAINT `genders_product_id_d348706d_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genders`
--

LOCK TABLES `genders` WRITE;
/*!40000 ALTER TABLE `genders` DISABLE KEYS */;
INSERT INTO `genders` VALUES (1,'genderless',19),(2,'men',20),(3,'men',21),(4,'men',22);
/*!40000 ALTER TABLE `genders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_statuses`
--

DROP TABLE IF EXISTS `order_statuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_statuses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_statuses`
--

LOCK TABLES `order_statuses` WRITE;
/*!40000 ALTER TABLE `order_statuses` DISABLE KEYS */;
INSERT INTO `order_statuses` VALUES (1,'결제전'),(2,'결제승인'),(3,'결제실패(돈 내놔)'),(4,'배송 준비중'),(5,'배송 중~~!!'),(6,'배송완료');
/*!40000 ALTER TABLE `order_statuses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `total_cost` decimal(15,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `address_id` int NOT NULL,
  `product_id` int NOT NULL,
  `status_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_address_id_38f528bc_fk_addresses_id` (`address_id`),
  KEY `orders_product_id_410f7af4_fk_products_id` (`product_id`),
  KEY `orders_status_id_e763064e_fk_order_statuses_id` (`status_id`),
  KEY `orders_user_id_7e2523fb_fk_users_id` (`user_id`),
  CONSTRAINT `orders_address_id_38f528bc_fk_addresses_id` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`),
  CONSTRAINT `orders_product_id_410f7af4_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `orders_status_id_e763064e_fk_order_statuses_id` FOREIGN KEY (`status_id`) REFERENCES `order_statuses` (`id`),
  CONSTRAINT `orders_user_id_7e2523fb_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,123.33,'2021-03-09 21:59:24.257136','2021-03-09 21:59:24.257308',2,5,1,11),(2,123.33,'2021-03-09 22:11:50.833021','2021-03-09 22:11:50.833161',3,5,1,11),(3,123.33,'2021-03-09 22:12:15.463146','2021-03-09 22:12:15.463307',4,5,1,11),(4,123.33,'2021-03-09 22:12:47.196805','2021-03-09 22:12:47.196840',5,5,1,11),(5,123.33,'2021-03-10 15:31:53.578817','2021-03-10 15:31:53.578888',6,5,1,11),(6,123.33,'2021-03-10 15:31:59.335085','2021-03-10 15:31:59.335335',7,5,1,11);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_ages`
--

DROP TABLE IF EXISTS `product_ages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_ages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `age_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_ages_age_id_e30204ea_fk_ages_id` (`age_id`),
  KEY `product_ages_product_id_785ac31e_fk_products_id` (`product_id`),
  CONSTRAINT `product_ages_age_id_e30204ea_fk_ages_id` FOREIGN KEY (`age_id`) REFERENCES `ages` (`id`),
  CONSTRAINT `product_ages_product_id_785ac31e_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_ages`
--

LOCK TABLES `product_ages` WRITE;
/*!40000 ALTER TABLE `product_ages` DISABLE KEYS */;
INSERT INTO `product_ages` VALUES (1,1,1),(2,2,2),(3,3,3),(4,1,4),(5,2,5),(6,3,6),(7,3,7),(8,1,8),(9,2,9),(10,1,10),(11,2,11),(12,1,12),(13,2,13),(14,1,14),(15,2,15),(16,1,16),(17,2,17),(18,1,18),(19,4,19),(20,3,20),(21,4,21),(22,4,22);
/*!40000 ALTER TABLE `product_ages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_images`
--

DROP TABLE IF EXISTS `product_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_images` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(2000) NOT NULL,
  `product_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_images_product_id_28ebf5f0_fk_products_id` (`product_id`),
  CONSTRAINT `product_images_product_id_28ebf5f0_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_images`
--

LOCK TABLES `product_images` WRITE;
/*!40000 ALTER TABLE `product_images` DISABLE KEYS */;
INSERT INTO `product_images` VALUES (1,'C:\\fakepath\\productCreateLogo.png',19),(2,'C:\\fakepath\\productCreateLogo.png',19),(3,'C:\\fakepath\\productCreateLogo.png',19),(4,'C:\\fakepath\\productCreateLogo.png',19),(5,'C:\\fakepath\\productCreateLogo.png',19),(6,'C:\\fakepath\\productCreateLogo.png',19),(7,'C:\\fakepath\\productCreateLogo.png',19),(8,'C:\\fakepath\\productCreateLogo.png',19),(9,'C:\\fakepath\\productCreateLogo.png',19),(10,'C:\\fakepath\\productCreateLogo.png',19),(11,'C:\\fakepath\\productCreateLogo.png',19),(12,'C:\\fakepath\\productCreateLogo.png',19),(13,'C:\\fakepath\\productCreateLogo.png',19),(14,'C:\\fakepath\\productCreateLogo.png',19),(15,'C:\\fakepath\\productCreateLogo.png',19),(16,'C:\\fakepath\\productCreateLogo.png',19),(17,'C:\\fakepath\\productCreateLogo.png',19),(18,'C:\\fakepath\\productCreateLogo.png',19),(19,'C:\\fakepath\\productCreateLogo.png',19),(20,'C:\\fakepath\\productCreateLogo.png',19),(21,'C:\\fakepath\\productCreateLogo.png',19),(22,'C:\\fakepath\\productCreateLogo.png',19),(23,'C:\\fakepath\\productCreateLogo.png',19),(24,'C:\\fakepath\\productCreateLogo.png',19),(25,'C:\\fakepath\\productCreateLogo.png',19),(26,'C:\\fakepath\\productCreateLogo.png',19),(27,'C:\\fakepath\\productCreateLogo.png',19),(28,'C:\\fakepath\\productCreateLogo.png',19),(29,'C:\\fakepath\\productCreateLogo.png',19),(30,'C:\\fakepath\\productCreateLogo.png',19),(31,'C:\\fakepath\\productCreateLogo.png',19),(32,'C:\\fakepath\\productCreateLogo.png',19),(33,'C:\\fakepath\\productCreateLogo.png',19),(34,'C:\\fakepath\\productCreateLogo.png',20),(35,'C:\\fakepath\\productCreateLogo.png',20),(36,'C:\\fakepath\\productCreateLogo.png',20),(37,'C:\\fakepath\\productCreateLogo.png',20),(38,'C:\\fakepath\\productCreateLogo.png',20),(39,'C:\\fakepath\\productCreateLogo.png',20),(40,'C:\\fakepath\\productCreateLogo.png',20),(41,'C:\\fakepath\\productCreateLogo.png',20),(42,'C:\\fakepath\\productCreateLogo.png',20),(43,'C:\\fakepath\\productCreateLogo.png',20),(44,'C:\\fakepath\\productCreateLogo.png',20),(45,'C:\\fakepath\\productCreateLogo.png',20),(46,'C:\\fakepath\\productCreateLogo.png',20),(47,'C:\\fakepath\\productCreateLogo.png',20),(48,'C:\\fakepath\\productCreateLogo.png',20),(49,'C:\\fakepath\\productCreateLogo.png',20),(50,'C:\\fakepath\\productCreateLogo.png',20),(51,'C:\\fakepath\\productCreateLogo.png',20),(52,'C:\\fakepath\\productCreateLogo.png',20),(53,'C:\\fakepath\\productCreateLogo.png',20),(54,'C:\\fakepath\\productCreateLogo.png',20),(55,'C:\\fakepath\\productCreateLogo.png',20),(56,'C:\\fakepath\\productCreateLogo.png',20),(57,'C:\\fakepath\\productCreateLogo.png',20),(58,'C:\\fakepath\\productCreateLogo.png',20),(59,'C:\\fakepath\\productCreateLogo.png',20),(60,'C:\\fakepath\\productCreateLogo.png',20),(61,'C:\\fakepath\\productCreateLogo.png',20),(62,'C:\\fakepath\\productCreateLogo.png',20),(63,'C:\\fakepath\\productCreateLogo.png',20),(64,'C:\\fakepath\\productCreateLogo.png',20),(65,'C:\\fakepath\\productCreateLogo.png',20),(66,'C:\\fakepath\\productCreateLogo.png',20),(67,'C:\\fakepath\\productCreateLogo.png',21),(68,'C:\\fakepath\\productCreateLogo.png',21),(69,'C:\\fakepath\\productCreateLogo.png',21),(70,'C:\\fakepath\\productCreateLogo.png',21),(71,'C:\\fakepath\\productCreateLogo.png',21),(72,'C:\\fakepath\\productCreateLogo.png',21),(73,'C:\\fakepath\\productCreateLogo.png',21),(74,'C:\\fakepath\\productCreateLogo.png',21),(75,'C:\\fakepath\\productCreateLogo.png',21),(76,'C:\\fakepath\\productCreateLogo.png',21),(77,'C:\\fakepath\\productCreateLogo.png',21),(78,'C:\\fakepath\\productCreateLogo.png',21),(79,'C:\\fakepath\\productCreateLogo.png',21),(80,'C:\\fakepath\\productCreateLogo.png',21),(81,'C:\\fakepath\\productCreateLogo.png',21),(82,'C:\\fakepath\\productCreateLogo.png',21),(83,'C:\\fakepath\\productCreateLogo.png',21),(84,'C:\\fakepath\\productCreateLogo.png',21),(85,'C:\\fakepath\\productCreateLogo.png',21),(86,'C:\\fakepath\\productCreateLogo.png',21),(87,'C:\\fakepath\\productCreateLogo.png',21),(88,'C:\\fakepath\\productCreateLogo.png',21),(89,'C:\\fakepath\\productCreateLogo.png',21),(90,'C:\\fakepath\\productCreateLogo.png',21),(91,'C:\\fakepath\\productCreateLogo.png',21),(92,'C:\\fakepath\\productCreateLogo.png',21),(93,'C:\\fakepath\\productCreateLogo.png',21),(94,'C:\\fakepath\\productCreateLogo.png',21),(95,'C:\\fakepath\\productCreateLogo.png',21),(96,'C:\\fakepath\\productCreateLogo.png',21),(97,'C:\\fakepath\\productCreateLogo.png',21),(98,'C:\\fakepath\\productCreateLogo.png',21),(99,'C:\\fakepath\\productCreateLogo.png',21),(100,'C:\\fakepath\\productCreateLogo.png',22),(101,'C:\\fakepath\\productCreateLogo.png',22),(102,'C:\\fakepath\\productCreateLogo.png',22),(103,'C:\\fakepath\\productCreateLogo.png',22),(104,'C:\\fakepath\\productCreateLogo.png',22),(105,'C:\\fakepath\\productCreateLogo.png',22),(106,'C:\\fakepath\\productCreateLogo.png',22),(107,'C:\\fakepath\\productCreateLogo.png',22),(108,'C:\\fakepath\\productCreateLogo.png',22),(109,'C:\\fakepath\\productCreateLogo.png',22),(110,'C:\\fakepath\\productCreateLogo.png',22),(111,'C:\\fakepath\\productCreateLogo.png',22),(112,'C:\\fakepath\\productCreateLogo.png',22),(113,'C:\\fakepath\\productCreateLogo.png',22),(114,'C:\\fakepath\\productCreateLogo.png',22),(115,'C:\\fakepath\\productCreateLogo.png',22),(116,'C:\\fakepath\\productCreateLogo.png',22),(117,'C:\\fakepath\\productCreateLogo.png',22),(118,'C:\\fakepath\\productCreateLogo.png',22),(119,'C:\\fakepath\\productCreateLogo.png',22),(120,'C:\\fakepath\\productCreateLogo.png',22),(121,'C:\\fakepath\\productCreateLogo.png',22),(122,'C:\\fakepath\\productCreateLogo.png',22),(123,'C:\\fakepath\\productCreateLogo.png',22),(124,'C:\\fakepath\\productCreateLogo.png',22),(125,'C:\\fakepath\\productCreateLogo.png',22),(126,'C:\\fakepath\\productCreateLogo.png',22),(127,'C:\\fakepath\\productCreateLogo.png',22),(128,'C:\\fakepath\\productCreateLogo.png',22),(129,'C:\\fakepath\\productCreateLogo.png',22),(130,'C:\\fakepath\\productCreateLogo.png',22),(131,'C:\\fakepath\\productCreateLogo.png',22),(132,'C:\\fakepath\\productCreateLogo.png',22);
/*!40000 ALTER TABLE `product_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_productuserlike`
--

DROP TABLE IF EXISTS `product_productuserlike`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_productuserlike` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_productuserlike_product_id_a94a95bf_fk_products_id` (`product_id`),
  KEY `product_productuserlike_user_id_34ba7bed_fk_users_id` (`user_id`),
  CONSTRAINT `product_productuserlike_product_id_a94a95bf_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `product_productuserlike_user_id_34ba7bed_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_productuserlike`
--

LOCK TABLES `product_productuserlike` WRITE;
/*!40000 ALTER TABLE `product_productuserlike` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_productuserlike` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `price` decimal(12,2) NOT NULL,
  `gift` tinyint(1) NOT NULL,
  `available_now` tinyint(1) NOT NULL,
  `introduction` longtext NOT NULL,
  `thumbnail_url` varchar(2000) NOT NULL,
  `satisfaction` int NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `category_id` int NOT NULL,
  `class_level_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_category_id_a7a3a156_fk_categories_id` (`category_id`),
  KEY `products_class_level_id_1b38e930_fk_class_levels_id` (`class_level_id`),
  KEY `products_user_id_0be7171c_fk_users_id` (`user_id`),
  CONSTRAINT `products_category_id_a7a3a156_fk_categories_id` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `products_class_level_id_1b38e930_fk_class_levels_id` FOREIGN KEY (`class_level_id`) REFERENCES `class_levels` (`id`),
  CONSTRAINT `products_user_id_0be7171c_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'아따맘마',50000.00,0,1,'안녕하세요','https://images.unsplash.com/photo-1554260570-9140fd3b7614?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿1','2021-03-09 15:31:32.566934','2021-03-09 15:31:32.567221',1,1,1),(2,'원피스',50000.00,0,1,'반갑습니다.','https://images.unsplash.com/photo-1612161330631-9186c513de7f?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Nnx8dGh1bWJuYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',0,'굿2','2021-03-09 15:31:32.635319','2021-03-09 15:31:32.635473',2,2,2),(3,'나루토',50000.00,0,1,'다시만나요','https://images.unsplash.com/photo-1519549735396-e5f6f8ee578c?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTB8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',0,'굿3','2021-03-09 15:31:32.678256','2021-03-09 15:31:32.678295',3,3,3),(4,'다다다',50000.00,1,1,'잘가요','https://images.unsplash.com/photo-1583039721278-2e67fe5f757e?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTJ8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',0,'굿4','2021-03-09 15:31:32.715947','2021-03-09 15:31:32.715977',4,4,4),(5,'안녕하세요',50000.00,1,0,'굿뜨','https://images.unsplash.com/photo-1528119472819-fa0cf45dbdd2?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTV8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿5','2021-03-09 15:31:32.778395','2021-03-09 15:31:32.778444',5,1,5),(6,'아주베리굿1',50000.00,1,0,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿6','2021-03-09 15:31:32.828221','2021-03-09 15:31:32.828268',6,2,6),(7,'아주베리굿2',50000.00,0,0,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿7','2021-03-09 15:31:32.879477','2021-03-09 15:31:32.879657',7,3,6),(8,'아주베리굿3',50000.00,1,0,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿8','2021-03-09 15:31:32.938677','2021-03-09 15:31:32.938796',8,4,6),(9,'아주베리굿4',50000.00,0,1,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿9','2021-03-09 15:31:32.990978','2021-03-09 15:31:32.991085',9,1,6),(10,'아주베리굿5',50000.00,1,1,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿10','2021-03-09 15:31:33.044107','2021-03-09 15:31:33.044223',10,2,6),(11,'아주베리굿6',50000.00,0,0,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿11','2021-03-09 15:31:33.104711','2021-03-09 15:31:33.104812',11,3,6),(12,'아주베리굿7',50000.00,1,0,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿12','2021-03-09 15:31:33.152852','2021-03-09 15:31:33.152900',12,4,6),(13,'아주베리굿8',50000.00,0,0,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿13','2021-03-09 15:31:33.224008','2021-03-09 15:31:33.224126',13,1,6),(14,'아주베리굿9',50000.00,1,0,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿14','2021-03-09 15:31:33.279558','2021-03-09 15:31:33.279624',14,2,6),(15,'아주베리굿10',50000.00,0,1,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿15','2021-03-09 15:31:33.327566','2021-03-09 15:31:33.327605',15,3,6),(16,'아주베리굿11',50000.00,1,1,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿16','2021-03-09 15:31:33.391750','2021-03-09 15:31:33.391834',16,4,6),(17,'아주베리굿12',50000.00,0,1,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿17','2021-03-09 15:31:33.453113','2021-03-09 15:31:33.453186',17,1,6),(18,'아주베리굿13',50000.00,1,0,'호호호히히히히','https://images.unsplash.com/photo-1581997328000-7eba22a89b45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHRodW1ibmFpbHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',1,'굿18','2021-03-09 15:31:33.504352','2021-03-09 15:31:33.504404',18,2,6),(19,'asfdㅓ호',345.00,0,0,'','C:\\fakepath\\productCreateLogo.png',90,'','2021-03-10 12:26:52.829352','2021-03-10 12:26:52.829399',17,4,11),(20,'ㅣㅏㅓㅣㅏㅓㅁㄴㅇㄹ',98798723.00,0,0,'','C:\\fakepath\\productCreateLogo.png',90,'','2021-03-10 12:29:06.308226','2021-03-10 12:29:06.308307',13,4,11),(21,'ㅁㄴㅇㄹ',980.00,0,0,'','C:\\fakepath\\productCreateLogo.png',90,'','2021-03-10 12:30:53.220582','2021-03-10 12:30:53.220768',15,5,11),(22,'ㅁㄴㅇㄹ',345983.00,0,0,'','C:\\fakepath\\productCreateLogo.png',90,'','2021-03-10 12:32:05.509638','2021-03-10 12:32:05.509677',16,3,11);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image_url` varchar(2000) NOT NULL,
  `description` longtext NOT NULL,
  `product_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reviews_product_id_d4b78cfe_fk_products_id` (`product_id`),
  KEY `reviews_user_id_c23b0903_fk_users_id` (`user_id`),
  CONSTRAINT `reviews_product_id_d4b78cfe_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `reviews_user_id_c23b0903_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_tiers`
--

DROP TABLE IF EXISTS `user_tiers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_tiers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_tiers`
--

LOCK TABLES `user_tiers` WRITE;
/*!40000 ALTER TABLE `user_tiers` DISABLE KEYS */;
INSERT INTO `user_tiers` VALUES (1,'Amateur'),(2,'Professional'),(3,'Master');
/*!40000 ALTER TABLE `user_tiers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_types`
--

DROP TABLE IF EXISTS `user_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_types` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_types`
--

LOCK TABLES `user_types` WRITE;
/*!40000 ALTER TABLE `user_types` DISABLE KEYS */;
INSERT INTO `user_types` VALUES (1,'user'),(2,'creator');
/*!40000 ALTER TABLE `user_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `email` varchar(500) NOT NULL,
  `password` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `image_url` varchar(2000) NOT NULL,
  `social_login` varchar(50) DEFAULT NULL,
  `tier_id` int NOT NULL,
  `user_type_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `users_tier_id_4396e64b_fk_user_tiers_id` (`tier_id`),
  KEY `users_user_type_id_c594293d_fk_user_types_id` (`user_type_id`),
  CONSTRAINT `users_tier_id_4396e64b_fk_user_tiers_id` FOREIGN KEY (`tier_id`) REFERENCES `user_tiers` (`id`),
  CONSTRAINT `users_user_type_id_c594293d_fk_user_types_id` FOREIGN KEY (`user_type_id`) REFERENCES `user_types` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'이동근','12345676@gmail.com','123456789','2021-03-09 15:31:32.260846','2021-03-09 15:31:32.261002','https://images.unsplash.com/photo-1546820389-44d77e1f3b31?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80','카카오',1,2),(2,'데이비드','22222222@gamil.com','123456789','2021-03-09 15:31:32.287201','2021-03-09 15:31:32.287289','https://images.unsplash.com/photo-1597586124394-fbd6ef244026?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MzF8fGh1bWFufGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60','카카오',2,2),(3,'노아','33333333@gamil.com','123456789','2021-03-09 15:31:32.310608','2021-03-09 15:31:32.310696','https://unsplash.com/photos/tFkbdCf-l10','카카오',3,2),(4,'미호크','44444444@gamil.com','123456789','2021-03-09 15:31:32.335717','2021-03-09 15:31:32.335804','https://unsplash.com/photos/ZGznJjRPi_c','카카오',1,2),(5,'루피','55555555@gamil.com','123456789','2021-03-09 15:31:32.357833','2021-03-09 15:31:32.357896','https://images.unsplash.com/photo-1599140782241-144735f5949a?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NDZ8fGh1bWFufGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60','카카오',2,2),(6,'나미','66666666@gamil.com','123456789','2021-03-09 15:31:32.376208','2021-03-09 15:31:32.376270','https://images.unsplash.com/photo-1610882587765-f0439630a659?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NTB8fGh1bWFufGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60','카카오',3,2),(7,'조로','77777777@gmail.com','123456789','2021-03-09 15:31:32.393831','2021-03-09 15:31:32.393917','https://unsplash.com/photos/pZTVa_Gt1f8','카카오',1,2),(8,'상디','11111111@gamil.com','123456789','2021-03-09 15:31:32.416345','2021-03-09 15:31:32.416445','https://images.unsplash.com/photo-1610780757769-d46802dc2675?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NTd8fGh1bWFufGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60','카카오',2,2),(9,'로빈','88888888@gamil.com','123456789','2021-03-09 15:31:32.442932','2021-03-09 15:31:32.443122','https://images.unsplash.com/photo-1574784618880-a1036d310e7c?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Njh8fGh1bWFufGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60','카카오',3,2),(10,'쵸파','qqqqqqqq@gamil.com','123456789','2021-03-09 15:31:32.463882','2021-03-09 15:31:32.463964','https://images.unsplash.com/photo-1595803471186-8816059f097a?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTEwfHxodW1hbnxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60','카카오',1,2),(11,'이동근','eagle5424@naver.com','$2b$12$kcyiDvZXwbaVoLSJrD.md.YaasuaZ3yz3cNajG8V81oc2Cb4Db5yy','2021-03-09 15:43:17.023446','2021-03-09 15:43:17.023484','https://media.vlpt.us/images/c_hyun403/post/7b35d3bb-44be-41bf-8192-0ccc426b465c/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-02-26%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.53.02.png',NULL,1,1),(12,'이동근','eagle5424@gmail.com','$2b$12$rHwL6NWUy5D.0HD4jGyBHONHsclueG4h7jh5kNimd.8KNu8wo0FZq','2021-03-09 15:45:51.571955','2021-03-09 15:45:51.571992','https://media.vlpt.us/images/c_hyun403/post/7b35d3bb-44be-41bf-8192-0ccc426b465c/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-02-26%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.53.02.png',NULL,1,1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-11  1:08:13
