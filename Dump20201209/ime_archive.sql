-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: ime
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `archive`
--

DROP TABLE IF EXISTS `archive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `archive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentID` varchar(11) NOT NULL,
  `starting_date` datetime NOT NULL,
  `disconnection_date` datetime NOT NULL,
  `disconnection_causeID` int(11) NOT NULL,
  `document_number` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_cause_archieve` (`disconnection_causeID`),
  KEY `fk_archieve_student` (`studentID`),
  CONSTRAINT `fk_archieve_cause` FOREIGN KEY (`disconnection_causeID`) REFERENCES `causes` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_archieve_student` FOREIGN KEY (`studentID`) REFERENCES `students` (`id_number`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `archive`
--

LOCK TABLES `archive` WRITE;
/*!40000 ALTER TABLE `archive` DISABLE KEYS */;
INSERT INTO `archive` VALUES (59,'55555555555','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(60,'33333333333','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(61,'66666666666','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(62,'44444444444','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(63,'22222222222','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(64,'11111111111','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(65,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(66,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'2'),(67,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'2'),(68,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'3'),(69,'55555555555','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'2'),(70,'33333333333','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(71,'66666666666','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(72,'44444444444','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(73,'22222222222','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(74,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(75,'55555555555','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(76,'33333333333','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(77,'66666666666','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(78,'44444444444','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(79,'22222222222','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(80,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(81,'55555555555','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(82,'33333333333','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1');
/*!40000 ALTER TABLE `archive` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-09 11:11:33
