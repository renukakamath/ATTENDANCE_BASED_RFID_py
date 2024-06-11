/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - attendance_py
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`attendance_py` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `attendance_py`;

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `attendance` */

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `cardstatus` varchar(100) DEFAULT NULL,
  `cardnumber` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `employee` */

insert  into `employee`(`employee_id`,`login_id`,`firstname`,`lastname`,`place`,`phone`,`email`,`status`,`cardstatus`,`cardnumber`,`photo`) values 
(2,3,'employee1','e','ernakulam','1234567890','employee1@gmail.com','accept','pending','1324325','static/image/bc46c3ba-3454-4350-aa2d-cdbe470716a210855406.jpg'),
(3,4,'user','qwerty','ernakulam','5432545','user@gmail.com','reject','pending','12345678','static/image/5aafed6b-b817-4227-b09b-eea5622291924.jfif');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'employee','employee','employee'),
(3,'employee1','employee1','employee'),
(4,'user','user','block');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
