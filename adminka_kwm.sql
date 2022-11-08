-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: db:3306
-- Время создания: Ноя 08 2022 г., 17:08
-- Версия сервера: 5.7.40
-- Версия PHP: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `adminka_kwm`
--

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `auth_permission`
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
(25, 'Can add Ящик', 7, 'add_korob'),
(26, 'Can change Ящик', 7, 'change_korob'),
(27, 'Can delete Ящик', 7, 'delete_korob'),
(28, 'Can view Ящик', 7, 'view_korob'),
(29, 'Can add Страна', 8, 'add_country'),
(30, 'Can change Страна', 8, 'change_country'),
(31, 'Can delete Страна', 8, 'delete_country'),
(32, 'Can view Страна', 8, 'view_country'),
(33, 'Can add Код коробки', 9, 'add_donwload_codes_korob'),
(34, 'Can change Код коробки', 9, 'change_donwload_codes_korob'),
(35, 'Can delete Код коробки', 9, 'delete_donwload_codes_korob'),
(36, 'Can view Код коробки', 9, 'view_donwload_codes_korob'),
(37, 'Can add Продукт', 10, 'add_product'),
(38, 'Can change Продукт', 10, 'change_product'),
(39, 'Can delete Продукт', 10, 'delete_product'),
(40, 'Can view Продукт', 10, 'view_product'),
(41, 'Can add Код потребительский', 11, 'add_donwload_codes'),
(42, 'Can change Код потребительский', 11, 'change_donwload_codes'),
(43, 'Can delete Код потребительский', 11, 'delete_donwload_codes'),
(44, 'Can view Код потребительский', 11, 'view_donwload_codes'),
(45, 'Can add Тара', 12, 'add_tara'),
(46, 'Can change Тара', 12, 'change_tara'),
(47, 'Can delete Тара', 12, 'delete_tara'),
(48, 'Can view Тара', 12, 'view_tara');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$HfnbWUqJBng4fFJH2WwByk$LFTV1Gne5VP66533hDkzgpTzrBopo19OGvL3EsVxoQs=', '2022-11-08 16:54:26.032952', 1, 'liofan', '', '', 'lefiofan21@gmail.com', 1, 1, '2022-11-08 16:15:45.918411');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-11-08 16:19:33.919789', '1', 'Казахстан', 1, '[{\"added\": {}}]', 8, 1),
(2, '2022-11-08 16:19:36.796083', '2', 'Россия', 1, '[{\"added\": {}}]', 8, 1),
(3, '2022-11-08 16:19:44.875172', '1', '0.25', 1, '[{\"added\": {}}]', 12, 1),
(4, '2022-11-08 16:19:45.951758', '2', '1', 1, '[{\"added\": {}}]', 12, 1),
(5, '2022-11-08 16:19:48.266147', '3', '1.5', 1, '[{\"added\": {}}]', 12, 1),
(6, '2022-11-08 16:19:49.875776', '4', '5', 1, '[{\"added\": {}}]', 12, 1),
(7, '2022-11-08 16:40:18.016505', '1', 'Voda', 1, '[{\"added\": {}}]', 10, 1),
(8, '2022-11-08 16:47:39.437269', '1', '234234234', 1, '[{\"added\": {}}]', 11, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'markirovka', 'country'),
(11, 'markirovka', 'donwload_codes'),
(9, 'markirovka', 'donwload_codes_korob'),
(7, 'markirovka', 'korob'),
(10, 'markirovka', 'product'),
(12, 'markirovka', 'tara'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Структура таблицы `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-11-08 16:12:08.732769'),
(2, 'auth', '0001_initial', '2022-11-08 16:12:08.877157'),
(3, 'admin', '0001_initial', '2022-11-08 16:12:08.911763'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-11-08 16:12:08.916543'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-11-08 16:12:08.921862'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-11-08 16:12:08.949862'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-11-08 16:12:08.966981'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-11-08 16:12:08.984585'),
(9, 'auth', '0004_alter_user_username_opts', '2022-11-08 16:12:08.995755'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-11-08 16:12:09.013659'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-11-08 16:12:09.015893'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-11-08 16:12:09.021322'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-11-08 16:12:09.037154'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-11-08 16:12:09.052260'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-11-08 16:12:09.068482'),
(16, 'auth', '0011_update_proxy_permissions', '2022-11-08 16:12:09.073983'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-11-08 16:12:09.089787'),
(18, 'sessions', '0001_initial', '2022-11-08 16:12:09.101489'),
(19, 'markirovka', '0001_initial', '2022-11-08 16:19:18.882018');

-- --------------------------------------------------------

--
-- Структура таблицы `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('rvk7ycgsbnrl19md2jfne5ri22ohixxr', '.eJxVjEEOwiAQRe_C2hCmtAPj0r1naIAZbNXQpLQr492VpAtd_M1_L--lxrBv07hXWceZ1VmBOv1-MaSHlAb4Hspt0Wkp2zpH3RR90KqvC8vzcrh_gSnUqWU9DIAWyfQev7PWkQw5G3S995SJQBDZxojgTCdgODnHMgB0HTlW7w-N8DYR:1osRrm:GZGty4gOP5OFMQF9wOmIQIx54ZMvt-0ulLJvBHptiPg', '2022-11-22 16:54:26.035216');

-- --------------------------------------------------------

--
-- Структура таблицы `markirovka_country`
--

CREATE TABLE `markirovka_country` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `markirovka_country`
--

INSERT INTO `markirovka_country` (`id`, `name`) VALUES
(1, 'Казахстан'),
(2, 'Россия');

-- --------------------------------------------------------

--
-- Структура таблицы `markirovka_donwload_codes`
--

CREATE TABLE `markirovka_donwload_codes` (
  `id` bigint(20) NOT NULL,
  `code` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `aggr` tinyint(1) DEFAULT NULL,
  `nanes` tinyint(1) DEFAULT NULL,
  `country_id` bigint(20) NOT NULL,
  `products_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `markirovka_donwload_codes`
--

INSERT INTO `markirovka_donwload_codes` (`id`, `code`, `aggr`, `nanes`, `country_id`, `products_id`) VALUES
(1, '234234234', 0, 0, 2, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `markirovka_donwload_codes_korob`
--

CREATE TABLE `markirovka_donwload_codes_korob` (
  `id` bigint(20) NOT NULL,
  `code` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `aggr` tinyint(1) DEFAULT NULL,
  `nanes` tinyint(1) DEFAULT NULL,
  `country_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `markirovka_korob`
--

CREATE TABLE `markirovka_korob` (
  `id` bigint(20) NOT NULL,
  `products_code` longtext COLLATE utf8_unicode_ci NOT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `aggr` varchar(1000) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nanes` varchar(1000) COLLATE utf8_unicode_ci DEFAULT NULL,
  `korob_code_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `markirovka_product`
--

CREATE TABLE `markirovka_product` (
  `id` bigint(20) NOT NULL,
  `title` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `img` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `gtin` varchar(28) COLLATE utf8_unicode_ci NOT NULL,
  `created` date NOT NULL,
  `tara_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `markirovka_product`
--

INSERT INTO `markirovka_product` (`id`, `title`, `img`, `gtin`, `created`, `tara_id`) VALUES
(1, 'Voda', 'images/Voda.png', '123213123', '2022-11-08', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `markirovka_tara`
--

CREATE TABLE `markirovka_tara` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `markirovka_tara`
--

INSERT INTO `markirovka_tara` (`id`, `name`) VALUES
(1, '0.25'),
(2, '1'),
(3, '1.5'),
(4, '5');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Индексы таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Индексы таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Индексы таблицы `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Индексы таблицы `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Индексы таблицы `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Индексы таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Индексы таблицы `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Индексы таблицы `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Индексы таблицы `markirovka_country`
--
ALTER TABLE `markirovka_country`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Индексы таблицы `markirovka_donwload_codes`
--
ALTER TABLE `markirovka_donwload_codes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `markirovka_donwload__country_id_ca7ead2c_fk_markirovk` (`country_id`),
  ADD KEY `markirovka_donwload__products_id_9574f0f9_fk_markirovk` (`products_id`);

--
-- Индексы таблицы `markirovka_donwload_codes_korob`
--
ALTER TABLE `markirovka_donwload_codes_korob`
  ADD PRIMARY KEY (`id`),
  ADD KEY `markirovka_donwload__country_id_8defa03a_fk_markirovk` (`country_id`);

--
-- Индексы таблицы `markirovka_korob`
--
ALTER TABLE `markirovka_korob`
  ADD PRIMARY KEY (`id`),
  ADD KEY `markirovka_korob_korob_code_id_dbb1e29b_fk_markirovk` (`korob_code_id`);

--
-- Индексы таблицы `markirovka_product`
--
ALTER TABLE `markirovka_product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `markirovka_product_tara_id_45656a47_fk_markirovka_tara_id` (`tara_id`),
  ADD KEY `markirovka_product_created_8370c27d` (`created`);

--
-- Индексы таблицы `markirovka_tara`
--
ALTER TABLE `markirovka_tara`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT для таблицы `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT для таблицы `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT для таблицы `markirovka_country`
--
ALTER TABLE `markirovka_country`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `markirovka_donwload_codes`
--
ALTER TABLE `markirovka_donwload_codes`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `markirovka_donwload_codes_korob`
--
ALTER TABLE `markirovka_donwload_codes_korob`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `markirovka_korob`
--
ALTER TABLE `markirovka_korob`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `markirovka_product`
--
ALTER TABLE `markirovka_product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `markirovka_tara`
--
ALTER TABLE `markirovka_tara`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `markirovka_donwload_codes`
--
ALTER TABLE `markirovka_donwload_codes`
  ADD CONSTRAINT `markirovka_donwload__country_id_ca7ead2c_fk_markirovk` FOREIGN KEY (`country_id`) REFERENCES `markirovka_country` (`id`),
  ADD CONSTRAINT `markirovka_donwload__products_id_9574f0f9_fk_markirovk` FOREIGN KEY (`products_id`) REFERENCES `markirovka_product` (`id`);

--
-- Ограничения внешнего ключа таблицы `markirovka_donwload_codes_korob`
--
ALTER TABLE `markirovka_donwload_codes_korob`
  ADD CONSTRAINT `markirovka_donwload__country_id_8defa03a_fk_markirovk` FOREIGN KEY (`country_id`) REFERENCES `markirovka_country` (`id`);

--
-- Ограничения внешнего ключа таблицы `markirovka_korob`
--
ALTER TABLE `markirovka_korob`
  ADD CONSTRAINT `markirovka_korob_korob_code_id_dbb1e29b_fk_markirovk` FOREIGN KEY (`korob_code_id`) REFERENCES `markirovka_donwload_codes_korob` (`id`);

--
-- Ограничения внешнего ключа таблицы `markirovka_product`
--
ALTER TABLE `markirovka_product`
  ADD CONSTRAINT `markirovka_product_tara_id_45656a47_fk_markirovka_tara_id` FOREIGN KEY (`tara_id`) REFERENCES `markirovka_tara` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
