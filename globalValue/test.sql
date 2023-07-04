/*
 Navicat Premium Data Transfer

 Source Server         : jiejie
 Source Server Type    : MySQL
 Source Server Version : 80033
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 80033
 File Encoding         : 65001

 Date: 04/07/2023 20:02:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account`  (
  `ID` int(0) NOT NULL,
  `Password` char(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES (1002, '123456');
INSERT INTO `account` VALUES (1003, '123456');
INSERT INTO `account` VALUES (10001, '123456');
INSERT INTO `account` VALUES (10002, '123456');
INSERT INTO `account` VALUES (123456, '123456');

-- ----------------------------
-- Table structure for classroom
-- ----------------------------
DROP TABLE IF EXISTS `classroom`;
CREATE TABLE `classroom`  (
  `ID` int(0) NOT NULL,
  `Name` char(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Time` int(0) NULL DEFAULT NULL,
  `flag` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classroom
-- ----------------------------
INSERT INTO `classroom` VALUES (1, '麦一教101', 1, 0);
INSERT INTO `classroom` VALUES (2, '麦一教101', 2, 0);
INSERT INTO `classroom` VALUES (3, '麦一教101', 3, 0);
INSERT INTO `classroom` VALUES (4, '麦一教101', 4, 0);
INSERT INTO `classroom` VALUES (5, '麦一教101', 5, 0);
INSERT INTO `classroom` VALUES (6, '麦一教101', 6, 0);
INSERT INTO `classroom` VALUES (7, '麦一教101', 7, 0);
INSERT INTO `classroom` VALUES (8, '麦一教101', 8, 0);

-- ----------------------------
-- Table structure for collegelist
-- ----------------------------
DROP TABLE IF EXISTS `collegelist`;
CREATE TABLE `collegelist`  (
  `CollegeID` int(0) NULL DEFAULT NULL,
  `College` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `MajorID` int(0) NOT NULL,
  `Major` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`MajorID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of collegelist
-- ----------------------------
INSERT INTO `collegelist` VALUES (101, '软件与物联网工程学院', 1001, '软件工程');
INSERT INTO `collegelist` VALUES (101, '软件与物联网工程学院', 1002, '物联网工程');
INSERT INTO `collegelist` VALUES (102, '统计学院', 1003, '经济统计学');
INSERT INTO `collegelist` VALUES (102, '统计学院', 1004, '应用统计学');
INSERT INTO `collegelist` VALUES (102, '统计学院', 1005, '精算学');
INSERT INTO `collegelist` VALUES (103, '外国语学院', 1006, '商务英语');
INSERT INTO `collegelist` VALUES (103, '外国语学院', 1007, '日语');
INSERT INTO `collegelist` VALUES (104, '艺术学院', 1008, '音乐学');
INSERT INTO `collegelist` VALUES (104, '艺术学院', 1009, '环境设计');
INSERT INTO `collegelist` VALUES (105, '法学院', 1010, '法务会计');
INSERT INTO `collegelist` VALUES (105, '法学院', 1011, '数据法学');
INSERT INTO `collegelist` VALUES (106, '人文学院', 1012, '社会工作');
INSERT INTO `collegelist` VALUES (106, '人文学院', 1013, '新闻学');
INSERT INTO `collegelist` VALUES (107, '体育学院', 1014, '社会体育指导');
INSERT INTO `collegelist` VALUES (108, '会计学院', 1015, '财务管理');
INSERT INTO `collegelist` VALUES (108, '会计学院', 1016, '注册会计师');
INSERT INTO `collegelist` VALUES (109, '机械学院', 1017, '机器维修');
INSERT INTO `collegelist` VALUES (109, '机械学院', 1018, '机器制造');

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `SelectID` int(0) NOT NULL AUTO_INCREMENT,
  `CourseID` int(0) NULL DEFAULT NULL,
  `CourseName` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `score` int(0) NULL DEFAULT NULL,
  `CourseTime` int(0) NULL DEFAULT NULL,
  `CoursePlace` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Num` int(0) NULL DEFAULT NULL,
  `Selectnum` int(0) NULL DEFAULT NULL,
  `Grade` int(0) NULL DEFAULT NULL,
  `Major` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `TeacherName` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Time` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`SelectID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES (1, 2001, 'java', 4, 12, '一教101', 30, 0, 2, '软件工程', '老王', '周二');
INSERT INTO `course` VALUES (2, 2002, 'java', 4, 12, '一教101', 30, 7, 2, '软件工程', '老王', '周三');
INSERT INTO `course` VALUES (3, 2002, 'java', 4, 67, '一教101', 30, 0, 2, '软件工程', '老王', '周三');
INSERT INTO `course` VALUES (4, 2002, 'java', 4, 67, '一教101', 30, 0, 2, '软件工程', '老王', '周二');

-- ----------------------------
-- Table structure for messegelist
-- ----------------------------
DROP TABLE IF EXISTS `messegelist`;
CREATE TABLE `messegelist`  (
  `ID` int(0) NOT NULL AUTO_INCREMENT,
  `Name` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Messege` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of messegelist
-- ----------------------------
INSERT INTO `messegelist` VALUES (3, '老王', '你好，我要换课');

-- ----------------------------
-- Table structure for selectresult
-- ----------------------------
DROP TABLE IF EXISTS `selectresult`;
CREATE TABLE `selectresult`  (
  `ID` int(0) NULL DEFAULT NULL,
  `SelectID` int(0) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of selectresult
-- ----------------------------
INSERT INTO `selectresult` VALUES (10002, 2);

-- ----------------------------
-- Table structure for studentlist
-- ----------------------------
DROP TABLE IF EXISTS `studentlist`;
CREATE TABLE `studentlist`  (
  `ID` int(0) NOT NULL,
  `Name` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `College` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Major` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Grade` int(0) NULL DEFAULT NULL,
  `Identify` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentlist
-- ----------------------------
INSERT INTO `studentlist` VALUES (10001, '杰杰', '软件与物联网工程学院', '软件工程', 2, 'student');
INSERT INTO `studentlist` VALUES (10002, '小沐', '软件与物联网工程学院', '软件工程', 1, 'student');

-- ----------------------------
-- Table structure for studentscore
-- ----------------------------
DROP TABLE IF EXISTS `studentscore`;
CREATE TABLE `studentscore`  (
  `ID` int(0) NOT NULL,
  `sumscore` int(0) NULL DEFAULT NULL,
  `score` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentscore
-- ----------------------------
INSERT INTO `studentscore` VALUES (10001, 26, 0);
INSERT INTO `studentscore` VALUES (10002, 26, 4);

-- ----------------------------
-- Table structure for teacherlist
-- ----------------------------
DROP TABLE IF EXISTS `teacherlist`;
CREATE TABLE `teacherlist`  (
  `ID` int(0) NOT NULL,
  `Name` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Education` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Degree` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `CollegeID` int(0) NULL DEFAULT NULL,
  `College` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Identify` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacherlist
-- ----------------------------
INSERT INTO `teacherlist` VALUES (1002, '老王', '博士研究生', '博士学位', 101, '软件与物联网工程学院', 'teacher');
INSERT INTO `teacherlist` VALUES (1003, '小杰', '博士研究生', '博士学位', 101, '软件与物联网工程学院', 'teacher');

-- ----------------------------
-- Table structure for trainingplan
-- ----------------------------
DROP TABLE IF EXISTS `trainingplan`;
CREATE TABLE `trainingplan`  (
  `CourseID` int(0) NOT NULL,
  `CourseName` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `score` int(0) NULL DEFAULT NULL,
  `Major` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Semester` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`CourseID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of trainingplan
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
