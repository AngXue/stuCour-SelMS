/*
 Navicat Premium Data Transfer

 Source Server         : localMysql
 Source Server Type    : MySQL
 Source Server Version : 80030
 Source Host           : localhost:3306
 Source Schema         : stums

 Target Server Type    : MySQL
 Target Server Version : 80030
 File Encoding         : 65001

 Date: 05/07/2023 11:08:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account`  (
  `ID` int NOT NULL,
  `Password` char(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES (123456, '123456');

-- ----------------------------
-- Table structure for classroom
-- ----------------------------
DROP TABLE IF EXISTS `classroom`;
CREATE TABLE `classroom`  (
  `Name` char(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of classroom
-- ----------------------------
INSERT INTO `classroom` VALUES ('麦一教103');
INSERT INTO `classroom` VALUES ('麦一教102');
INSERT INTO `classroom` VALUES ('麦一教101');

-- ----------------------------
-- Table structure for collegelist
-- ----------------------------
DROP TABLE IF EXISTS `collegelist`;
CREATE TABLE `collegelist`  (
  `CollegeID` int NULL DEFAULT NULL,
  `College` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `MajorID` int NOT NULL,
  `Major` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`MajorID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of collegelist
-- ----------------------------

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `SelectID` int NOT NULL AUTO_INCREMENT,
  `CourseID` int NULL DEFAULT NULL,
  `CourseName` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `score` int NULL DEFAULT NULL,
  `CourseTime` int NULL DEFAULT NULL,
  `CoursePlace` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Num` int NULL DEFAULT NULL,
  `Selectnum` int NULL DEFAULT NULL,
  `Grade` int NULL DEFAULT NULL,
  `Major` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `TeacherName` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Time` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`SelectID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of course
-- ----------------------------

-- ----------------------------
-- Table structure for messegelist
-- ----------------------------
DROP TABLE IF EXISTS `messegelist`;
CREATE TABLE `messegelist`  (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Messege` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of messegelist
-- ----------------------------

-- ----------------------------
-- Table structure for selectresult
-- ----------------------------
DROP TABLE IF EXISTS `selectresult`;
CREATE TABLE `selectresult`  (
  `ID` int NULL DEFAULT NULL,
  `SelectID` int NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of selectresult
-- ----------------------------

-- ----------------------------
-- Table structure for studentlist
-- ----------------------------
DROP TABLE IF EXISTS `studentlist`;
CREATE TABLE `studentlist`  (
  `ID` int NOT NULL,
  `Name` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `College` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Major` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Grade` int NULL DEFAULT NULL,
  `Identify` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of studentlist
-- ----------------------------

-- ----------------------------
-- Table structure for studentscore
-- ----------------------------
DROP TABLE IF EXISTS `studentscore`;
CREATE TABLE `studentscore`  (
  `ID` int NOT NULL,
  `sumscore` int NULL DEFAULT NULL,
  `score` int NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of studentscore
-- ----------------------------
INSERT INTO `studentscore` VALUES (10001, 26, 0);
INSERT INTO `studentscore` VALUES (10002, 26, 0);
INSERT INTO `studentscore` VALUES (10003, 26, 0);
INSERT INTO `studentscore` VALUES (10004, 26, 0);
INSERT INTO `studentscore` VALUES (10005, 26, 0);
INSERT INTO `studentscore` VALUES (10006, 26, 0);
INSERT INTO `studentscore` VALUES (10007, 26, 0);
INSERT INTO `studentscore` VALUES (10008, 26, 0);
INSERT INTO `studentscore` VALUES (10009, 26, 0);
INSERT INTO `studentscore` VALUES (10010, 26, 0);
INSERT INTO `studentscore` VALUES (10011, 26, 0);
INSERT INTO `studentscore` VALUES (10012, 26, 0);

-- ----------------------------
-- Table structure for teacherlist
-- ----------------------------
DROP TABLE IF EXISTS `teacherlist`;
CREATE TABLE `teacherlist`  (
  `ID` int NOT NULL,
  `Name` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Education` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Degree` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `CollegeID` int NULL DEFAULT NULL,
  `College` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Identify` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Major` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of teacherlist
-- ----------------------------

-- ----------------------------
-- Table structure for trainingplan
-- ----------------------------
DROP TABLE IF EXISTS `trainingplan`;
CREATE TABLE `trainingplan`  (
  `CourseID` int NOT NULL,
  `CourseName` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `score` int NULL DEFAULT NULL,
  `Major` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Semester` int NULL DEFAULT NULL,
  PRIMARY KEY (`CourseID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of trainingplan
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
