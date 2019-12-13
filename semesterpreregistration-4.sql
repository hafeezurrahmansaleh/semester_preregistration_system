-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2019 at 10:41 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `semesterpreregistration`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminpanel_coursepreregistration`
--

CREATE TABLE `adminpanel_coursepreregistration` (
  `id` int(11) NOT NULL,
  `section` varchar(5) NOT NULL,
  `paymentStatus` varchar(20) NOT NULL,
  `course_id` int(11) NOT NULL,
  `semester_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `adminpanel_courses`
--

CREATE TABLE `adminpanel_courses` (
  `id` int(11) NOT NULL,
  `courseCode` varchar(10) NOT NULL,
  `courseTitle` varchar(50) NOT NULL,
  `courseCredit` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  `term` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminpanel_courses`
--

INSERT INTO `adminpanel_courses` (`id`, `courseCode`, `courseTitle`, `courseCredit`, `level`, `term`) VALUES
(1, 'SWE233', 'Project-II (Web based)', 3, 3, 2),
(2, 'SWE333', 'Java Programming', 4, 3, 2),
(3, 'SWE211', 'Data Communication with lab', 4, 4, 1),
(4, 'SWE425', 'Distributive Computing with lab', 4, 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `adminpanel_semesterinfo`
--

CREATE TABLE `adminpanel_semesterinfo` (
  `id` int(11) NOT NULL,
  `semesterCode` int(11) NOT NULL,
  `semesterTitle` varchar(20) NOT NULL,
  `regOpenDate` date NOT NULL,
  `regCloseDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminpanel_semesterinfo`
--

INSERT INTO `adminpanel_semesterinfo` (`id`, `semesterCode`, `semesterTitle`, `regOpenDate`, `regCloseDate`) VALUES
(1, 193, 'Fall 2019', '2019-12-13', '2019-12-20'),
(2, 201, 'Spring 201', '2019-12-13', '2019-12-26'),
(3, 192, 'Summer 2019', '2019-12-13', '2019-12-26');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add teacher info', 7, 'add_teacherinfo'),
(26, 'Can change teacher info', 7, 'change_teacherinfo'),
(27, 'Can delete teacher info', 7, 'delete_teacherinfo'),
(28, 'Can view teacher info', 7, 'view_teacherinfo'),
(29, 'Can add student info', 8, 'add_studentinfo'),
(30, 'Can change student info', 8, 'change_studentinfo'),
(31, 'Can delete student info', 8, 'delete_studentinfo'),
(32, 'Can view student info', 8, 'view_studentinfo'),
(33, 'Can add admin info', 9, 'add_admininfo'),
(34, 'Can change admin info', 9, 'change_admininfo'),
(35, 'Can delete admin info', 9, 'delete_admininfo'),
(36, 'Can view admin info', 9, 'view_admininfo'),
(37, 'Can add course pre registration', 10, 'add_coursepreregistration'),
(38, 'Can change course pre registration', 10, 'change_coursepreregistration'),
(39, 'Can delete course pre registration', 10, 'delete_coursepreregistration'),
(40, 'Can view course pre registration', 10, 'view_coursepreregistration'),
(41, 'Can add courses', 11, 'add_courses'),
(42, 'Can change courses', 11, 'change_courses'),
(43, 'Can delete courses', 11, 'delete_courses'),
(44, 'Can view courses', 11, 'view_courses'),
(45, 'Can add semester info', 12, 'add_semesterinfo'),
(46, 'Can change semester info', 12, 'change_semesterinfo'),
(47, 'Can delete semester info', 12, 'delete_semesterinfo'),
(48, 'Can view semester info', 12, 'view_semesterinfo'),
(49, 'Can add advisor', 13, 'add_advisor'),
(50, 'Can change advisor', 13, 'change_advisor'),
(51, 'Can delete advisor', 13, 'delete_advisor'),
(52, 'Can view advisor', 13, 'view_advisor'),
(53, 'Can add course', 14, 'add_course'),
(54, 'Can change course', 14, 'change_course'),
(55, 'Can delete course', 14, 'delete_course'),
(56, 'Can view course', 14, 'view_course'),
(57, 'Can add course section', 15, 'add_coursesection'),
(58, 'Can change course section', 15, 'change_coursesection'),
(59, 'Can delete course section', 15, 'delete_coursesection'),
(60, 'Can view course section', 15, 'view_coursesection');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$120000$BWx0nui9ZcWJ$Kh/3wXwLaAFEbR7l761uePx2TNyyraXDSfFMU+PDv2w=', '2019-12-03 04:46:16.787039', 1, 'saleh', '', '', '', 1, 1, '2019-12-03 04:46:10.865868');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2019-12-03 06:05:36.794364', '1', 'Courses object (1)', 1, '[{\"added\": {}}]', 11, 1),
(2, '2019-12-03 06:06:09.752260', '2', 'Courses object (2)', 1, '[{\"added\": {}}]', 11, 1),
(3, '2019-12-03 06:06:32.447882', '3', 'Courses object (3)', 1, '[{\"added\": {}}]', 11, 1),
(4, '2019-12-03 06:06:58.147888', '4', 'Courses object (4)', 1, '[{\"added\": {}}]', 11, 1),
(5, '2019-12-03 06:07:23.074286', '5', 'Courses object (5)', 1, '[{\"added\": {}}]', 11, 1),
(6, '2019-12-03 06:07:57.016514', '6', 'Courses object (6)', 1, '[{\"added\": {}}]', 11, 1),
(7, '2019-12-03 06:08:28.678217', '7', 'Courses object (7)', 1, '[{\"added\": {}}]', 11, 1),
(8, '2019-12-03 06:11:58.232739', '1', 'TeacherInfo object (1)', 1, '[{\"added\": {}}]', 7, 1),
(9, '2019-12-03 06:12:36.022763', '1', 'StudentInfo object (1)', 1, '[{\"added\": {}}]', 8, 1),
(10, '2019-12-03 06:12:50.093142', '1', 'StudentInfo object (1)', 2, '[{\"changed\": {\"fields\": [\"stPassword\"]}}]', 8, 1),
(11, '2019-12-05 09:38:57.828223', '1', 'Advisor object (1)', 1, '[{\"added\": {}}]', 13, 1),
(12, '2019-12-05 09:39:35.472713', '2', 'Advisor object (2)', 1, '[{\"added\": {}}]', 13, 1),
(13, '2019-12-05 09:43:05.128049', '1', 'Course object (1)', 1, '[{\"added\": {}}]', 14, 1),
(14, '2019-12-05 09:43:28.035357', '2', 'Course object (2)', 1, '[{\"added\": {}}]', 14, 1),
(15, '2019-12-05 10:08:12.244557', '3', 'Course object (3)', 1, '[{\"added\": {}}]', 14, 1),
(16, '2019-12-11 09:00:06.661834', '1', 'SemesterInfo object (1)', 1, '[{\"added\": {}}]', 12, 1),
(17, '2019-12-11 09:00:49.505261', '2', 'SemesterInfo object (2)', 1, '[{\"added\": {}}]', 12, 1),
(18, '2019-12-11 09:01:03.762137', '3', 'SemesterInfo object (3)', 1, '[{\"added\": {}}]', 12, 1),
(19, '2019-12-11 09:02:54.840153', '4', 'SemesterInfo object (4)', 1, '[{\"added\": {}}]', 12, 1),
(20, '2019-12-11 09:03:31.452248', '3', 'SemesterInfo object (3)', 2, '[{\"changed\": {\"fields\": [\"semesterCode\"]}}]', 12, 1),
(21, '2019-12-11 09:03:51.722048', '4', 'SemesterInfo object (4)', 2, '[{\"changed\": {\"fields\": [\"semesterCode\"]}}]', 12, 1),
(22, '2019-12-11 09:04:19.094851', '5', 'SemesterInfo object (5)', 1, '[{\"added\": {}}]', 12, 1),
(23, '2019-12-11 09:04:28.727092', '6', 'SemesterInfo object (6)', 1, '[{\"added\": {}}]', 12, 1),
(24, '2019-12-11 09:04:38.365319', '7', 'SemesterInfo object (7)', 1, '[{\"added\": {}}]', 12, 1),
(25, '2019-12-11 09:05:01.731833', '8', 'SemesterInfo object (8)', 1, '[{\"added\": {}}]', 12, 1),
(26, '2019-12-11 09:32:43.260794', '4', 'CoursePreRegistration object (4)', 3, '', 10, 1),
(27, '2019-12-11 09:32:43.311940', '3', 'CoursePreRegistration object (3)', 3, '', 10, 1),
(28, '2019-12-11 09:32:43.418372', '2', 'CoursePreRegistration object (2)', 3, '', 10, 1),
(29, '2019-12-11 09:32:43.457312', '1', 'CoursePreRegistration object (1)', 3, '', 10, 1),
(30, '2019-12-11 10:16:31.600926', '11', 'CoursePreRegistration object (11)', 3, '', 10, 1),
(31, '2019-12-11 10:16:31.931591', '10', 'CoursePreRegistration object (10)', 3, '', 10, 1),
(32, '2019-12-11 10:16:31.970485', '9', 'CoursePreRegistration object (9)', 3, '', 10, 1),
(33, '2019-12-11 10:16:32.100145', '8', 'CoursePreRegistration object (8)', 3, '', 10, 1),
(34, '2019-12-11 10:16:32.175936', '7', 'CoursePreRegistration object (7)', 3, '', 10, 1),
(35, '2019-12-11 10:16:32.232785', '6', 'CoursePreRegistration object (6)', 3, '', 10, 1),
(36, '2019-12-11 10:16:32.271682', '5', 'CoursePreRegistration object (5)', 3, '', 10, 1),
(37, '2019-12-12 01:19:08.506282', '15', 'CoursePreRegistration object (15)', 3, '', 10, 1),
(38, '2019-12-12 01:19:08.581128', '14', 'CoursePreRegistration object (14)', 3, '', 10, 1),
(39, '2019-12-12 01:19:08.609011', '13', 'CoursePreRegistration object (13)', 3, '', 10, 1),
(40, '2019-12-12 01:40:51.851982', '25', 'CoursePreRegistration object (25)', 3, '', 10, 1),
(41, '2019-12-12 01:40:51.878910', '24', 'CoursePreRegistration object (24)', 3, '', 10, 1),
(42, '2019-12-12 01:40:51.918803', '23', 'CoursePreRegistration object (23)', 3, '', 10, 1),
(43, '2019-12-12 01:40:51.957701', '22', 'CoursePreRegistration object (22)', 3, '', 10, 1),
(44, '2019-12-12 01:40:51.997594', '21', 'CoursePreRegistration object (21)', 3, '', 10, 1),
(45, '2019-12-12 01:40:52.024847', '20', 'CoursePreRegistration object (20)', 3, '', 10, 1),
(46, '2019-12-12 01:40:52.064413', '19', 'CoursePreRegistration object (19)', 3, '', 10, 1),
(47, '2019-12-12 01:40:52.103310', '18', 'CoursePreRegistration object (18)', 3, '', 10, 1),
(48, '2019-12-12 01:40:52.142207', '17', 'CoursePreRegistration object (17)', 3, '', 10, 1),
(49, '2019-12-12 01:40:52.181358', '16', 'CoursePreRegistration object (16)', 3, '', 10, 1),
(50, '2019-12-12 01:40:52.210035', '12', 'CoursePreRegistration object (12)', 3, '', 10, 1),
(51, '2019-12-12 02:02:35.146046', '31', 'CoursePreRegistration object (31)', 3, '', 10, 1),
(52, '2019-12-12 02:02:35.198905', '30', 'CoursePreRegistration object (30)', 3, '', 10, 1),
(53, '2019-12-12 02:02:35.227831', '29', 'CoursePreRegistration object (29)', 3, '', 10, 1),
(54, '2019-12-12 02:02:35.266726', '28', 'CoursePreRegistration object (28)', 3, '', 10, 1),
(55, '2019-12-12 03:55:53.335574', '27', 'CoursePreRegistration object (27)', 2, '[{\"changed\": {\"fields\": [\"section\"]}}]', 10, 1),
(56, '2019-12-12 03:55:58.464199', '26', 'CoursePreRegistration object (26)', 2, '[]', 10, 1),
(57, '2019-12-12 03:57:10.140030', '27', 'CoursePreRegistration object (27)', 2, '[{\"changed\": {\"fields\": [\"section\"]}}]', 10, 1),
(58, '2019-12-12 04:11:42.000220', '26', 'CoursePreRegistration object (26)', 2, '[{\"changed\": {\"fields\": [\"section\"]}}]', 10, 1),
(59, '2019-12-12 06:17:57.993039', '34', 'CoursePreRegistration object (34)', 3, '', 10, 1),
(60, '2019-12-12 06:17:58.054928', '33', 'CoursePreRegistration object (33)', 3, '', 10, 1),
(61, '2019-12-12 06:17:58.115708', '32', 'CoursePreRegistration object (32)', 3, '', 10, 1),
(62, '2019-12-12 06:17:58.166577', '27', 'CoursePreRegistration object (27)', 3, '', 10, 1),
(63, '2019-12-12 06:17:58.194502', '26', 'CoursePreRegistration object (26)', 3, '', 10, 1),
(64, '2019-12-12 06:37:38.367544', '42', 'CoursePreRegistration object (42)', 1, '[{\"added\": {}}]', 10, 1),
(65, '2019-12-12 06:37:52.906666', '43', 'CoursePreRegistration object (43)', 1, '[{\"added\": {}}]', 10, 1),
(66, '2019-12-12 06:40:18.264031', '44', 'CoursePreRegistration object (44)', 1, '[{\"added\": {}}]', 10, 1),
(67, '2019-12-13 08:36:45.470155', '1', 'Courses object (1)', 1, '[{\"added\": {}}]', 11, 1),
(68, '2019-12-13 08:37:12.785329', '2', 'Courses object (2)', 1, '[{\"added\": {}}]', 11, 1),
(69, '2019-12-13 08:37:30.653684', '3', 'Courses object (3)', 1, '[{\"added\": {}}]', 11, 1),
(70, '2019-12-13 08:37:53.006805', '4', 'Courses object (4)', 1, '[{\"added\": {}}]', 11, 1),
(71, '2019-12-13 08:39:32.108560', '1', 'SemesterInfo object (1)', 1, '[{\"added\": {}}]', 12, 1),
(72, '2019-12-13 08:40:11.757473', '2', 'SemesterInfo object (2)', 1, '[{\"added\": {}}]', 12, 1),
(73, '2019-12-13 08:41:58.373360', '3', 'SemesterInfo object (3)', 1, '[{\"added\": {}}]', 12, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(9, 'adminpanel', 'admininfo'),
(10, 'adminpanel', 'coursepreregistration'),
(11, 'adminpanel', 'courses'),
(15, 'adminpanel', 'coursesection'),
(12, 'adminpanel', 'semesterinfo'),
(13, 'advisor', 'advisor'),
(14, 'advisor', 'course'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(8, 'student', 'studentinfo'),
(7, 'teacher', 'teacherinfo');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-12-03 03:58:13.793752'),
(2, 'auth', '0001_initial', '2019-12-03 03:58:23.671344'),
(3, 'admin', '0001_initial', '2019-12-03 03:58:27.233814'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-12-03 03:58:27.289663'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-12-03 03:58:27.425300'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-12-03 03:58:28.541317'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-12-03 03:58:29.791974'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-12-03 03:58:30.878103'),
(9, 'auth', '0004_alter_user_username_opts', '2019-12-03 03:58:30.985815'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-12-03 03:58:31.562282'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-12-03 03:58:31.601178'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-12-03 03:58:31.697920'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-12-03 03:58:32.569616'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-12-03 03:58:34.411089'),
(15, 'sessions', '0001_initial', '2019-12-03 03:58:35.016029'),
(16, 'teacher', '0001_initial', '2019-12-03 03:58:35.391249'),
(17, 'student', '0001_initial', '2019-12-03 04:00:21.536505'),
(19, 'adminpanel', '0002_auto_20191203_1203', '2019-12-03 06:03:56.892046'),
(20, 'adminpanel', '0003_coursepreregistration_paymentstatus', '2019-12-04 17:52:54.626563'),
(21, 'advisor', '0001_initial', '2019-12-05 09:27:23.295843'),
(22, 'advisor', '0002_course_courseteacher', '2019-12-05 09:41:59.494884'),
(23, 'adminpanel', '0004_auto_20191211_1502', '2019-12-11 09:02:48.975760'),
(24, 'adminpanel', '0005_auto_20191211_1618', '2019-12-11 10:19:06.008089'),
(25, 'adminpanel', '0001_initial', '2019-12-13 08:34:33.565389'),
(26, 'adminpanel', '0002_auto_20191213_1441', '2019-12-13 08:41:19.990003');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('93jazsdmroo0ag483hgv3oq0a4k43a2s', 'OTlmNDg0NzEwNjhmMWU0MjdiYzkwMjY0MzcyZmZkMDZhZmE5NTBmMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1YWZiNjY2NDZjNzA2MzgxYThiYjI5YzEzODNlNWY1Nzc2NjdkNDBiIn0=', '2019-12-17 04:46:16.842891');

-- --------------------------------------------------------

--
-- Table structure for table `student_studentinfo`
--

CREATE TABLE `student_studentinfo` (
  `id` int(11) NOT NULL,
  `stID` varchar(20) NOT NULL,
  `stName` varchar(30) NOT NULL,
  `stEmail` varchar(30) NOT NULL,
  `stGender` varchar(6) NOT NULL,
  `stPhone` varchar(20) NOT NULL,
  `stPassword` varchar(30) DEFAULT NULL,
  `stAdvisor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_studentinfo`
--

INSERT INTO `student_studentinfo` (`id`, `stID`, `stName`, `stEmail`, `stGender`, `stPhone`, `stPassword`, `stAdvisor_id`) VALUES
(1, '163-35-1746', 'Md. Abu Saleh', 'abu@gmail.com', 'male', '01772066066', '1234', 1);

-- --------------------------------------------------------

--
-- Table structure for table `teacher_teacherinfo`
--

CREATE TABLE `teacher_teacherinfo` (
  `id` int(11) NOT NULL,
  `tID` varchar(30) NOT NULL,
  `tName` varchar(30) NOT NULL,
  `tInitial` varchar(10) NOT NULL,
  `tDesignation` varchar(20) NOT NULL,
  `tPhone` varchar(20) NOT NULL,
  `tEmail` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teacher_teacherinfo`
--

INSERT INTO `teacher_teacherinfo` (`id`, `tID`, `tName`, `tInitial`, `tDesignation`, `tPhone`, `tEmail`) VALUES
(1, '170000272', 'Tasnim Rahman Katha', 'TRK', 'Lecturer', '0191111222', 't@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminpanel_coursepreregistration`
--
ALTER TABLE `adminpanel_coursepreregistration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `adminpanel_coursepre_course_id_420f1ff7_fk_adminpane` (`course_id`),
  ADD KEY `adminpanel_coursepre_semester_id_703093b6_fk_adminpane` (`semester_id`),
  ADD KEY `adminpanel_coursepre_student_id_d1f515d7_fk_student_s` (`student_id`);

--
-- Indexes for table `adminpanel_courses`
--
ALTER TABLE `adminpanel_courses`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `courseCode` (`courseCode`);

--
-- Indexes for table `adminpanel_semesterinfo`
--
ALTER TABLE `adminpanel_semesterinfo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `student_studentinfo`
--
ALTER TABLE `student_studentinfo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `stID` (`stID`),
  ADD KEY `student_studentinfo_stAdvisor_id_58889207_fk_teacher_t` (`stAdvisor_id`);

--
-- Indexes for table `teacher_teacherinfo`
--
ALTER TABLE `teacher_teacherinfo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tID` (`tID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminpanel_coursepreregistration`
--
ALTER TABLE `adminpanel_coursepreregistration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `adminpanel_courses`
--
ALTER TABLE `adminpanel_courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `adminpanel_semesterinfo`
--
ALTER TABLE `adminpanel_semesterinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `student_studentinfo`
--
ALTER TABLE `student_studentinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `teacher_teacherinfo`
--
ALTER TABLE `teacher_teacherinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `adminpanel_coursepreregistration`
--
ALTER TABLE `adminpanel_coursepreregistration`
  ADD CONSTRAINT `adminpanel_coursepre_course_id_420f1ff7_fk_adminpane` FOREIGN KEY (`course_id`) REFERENCES `adminpanel_courses` (`id`),
  ADD CONSTRAINT `adminpanel_coursepre_semester_id_703093b6_fk_adminpane` FOREIGN KEY (`semester_id`) REFERENCES `adminpanel_semesterinfo` (`id`),
  ADD CONSTRAINT `adminpanel_coursepre_student_id_d1f515d7_fk_student_s` FOREIGN KEY (`student_id`) REFERENCES `student_studentinfo` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `student_studentinfo`
--
ALTER TABLE `student_studentinfo`
  ADD CONSTRAINT `student_studentinfo_stAdvisor_id_58889207_fk_teacher_t` FOREIGN KEY (`stAdvisor_id`) REFERENCES `teacher_teacherinfo` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
