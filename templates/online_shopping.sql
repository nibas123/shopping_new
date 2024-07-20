-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 27, 2020 at 11:10 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `online_shopping`
--

-- --------------------------------------------------------

--
-- Table structure for table `billing_history`
--

CREATE TABLE `billing_history` (
  `billing_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `cost` int(11) NOT NULL,
  `address` text NOT NULL,
  `user_name` varchar(150) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(75) NOT NULL,
  `contact_no` varchar(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `status_details` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billing_history`
--

INSERT INTO `billing_history` (`billing_id`, `user_id`, `product_id`, `quantity`, `cost`, `address`, `user_name`, `city`, `state`, `contact_no`, `status`, `status_details`) VALUES
(2, 1, 2, 3, 360, 'bdgb gdhgf ', '', '', '', '', 'Order Accepted', 'Order Aceepted ffrom Hyd'),
(3, 1, 1, 4, 240, 'dsvdv sdg ', '', '', '', '', 'Order Accepted', 'Order Processing'),
(4, 1, 8, 1, 123, 'afdsafds safdsa', '', '', '', '', 'Order Accepted', 'Order Processing'),
(5, 1, 8, 1, 123, 'afdsafds safdsa', '', '', '', '', 'Order Accepted', 'Order Processing'),
(6, 1, 8, 1, 123, 'afdsafds safdsa', '', '', '', '', 'Order Accepted', 'Order Processing'),
(7, 1, 8, 1, 123, 'afdsafds safdsa', '', '', '', '', 'Order Accepted', 'Order Processing'),
(8, 1, 8, 1, 123, 'afdsafds safdsa', '', '', '', '', 'Order Accepted', 'Order Processing'),
(9, 1, 8, 1, 123, 'afdsafds safdsa', '', '', '', '', 'Order Accepted', 'Order Processing'),
(10, 1, 8, 1, 123, 'afdsafds safdsa', '', '', '', '', 'Order Accepted', 'Order Processing'),
(11, 1, 8, 1, 123, 'afdsafds safdsa', '', '', '', '', 'Order Accepted', 'Order Processing'),
(13, 1, 11, 1, 10000, '   dsvsdvdsvds sdvdsds sdvds asdfads ', '', '', '', '', 'Order Accepted', 'gfd'),
(14, 1, 13, 4, 4600, '    test ', '', '', '', '', 'Order Delivered', ''),
(15, 1, 13, 4, 4600, '    test ', '', '', '', '', 'Order Accepted', 'Order Processing'),
(16, 1, 12, 1, 960, '    test ', '', '', '', '', 'Order Accepted', 'Order Processing'),
(17, 1, 12, 1, 960, '    test ', '', '', '', '', 'Order Accepted', 'Order Processing'),
(18, 1, 12, 1, 960, '    test ', '', '', '', '', 'Order Delivered', ''),
(19, 1, 12, 1, 960, '  Kudsjf', 'Vaisakh', 'Alappuzha', 'Kerala', '8891812159', 'Order Accepted', 'Order Processing'),
(20, 1, 12, 1, 960, '  Kudsjf', 'Vaisakh K', 'Alappuzha', 'Kerala', '8891812159', 'Order Accepted', 'Order Processing'),
(21, 1, 12, 1, 960, '  Kudsjf', 'Vaisakh K', 'Alappuzha', 'Kerala', '8891812159', 'Order Accepted', 'Order Processing'),
(22, 1, 14, 1, 43500, 'dkshvf kajfksa', 'Vaisakh K', 'Alappuzha', 'Kerala', '8891812159', 'Order Accepted', 'Order Processing');

-- --------------------------------------------------------

--
-- Table structure for table `cancel_history`
--

CREATE TABLE `cancel_history` (
  `id` int(11) NOT NULL,
  `bill_no` int(11) NOT NULL,
  `feedback` text NOT NULL,
  `user_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `approval` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cancel_history`
--

INSERT INTO `cancel_history` (`id`, `bill_no`, `feedback`, `user_id`, `date`, `approval`) VALUES
(1, 1, 'asdasdsa', 1, '2020-05-27', 1);

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `cost` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `complaint` text NOT NULL,
  `by_user` int(11) NOT NULL,
  `approval` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`id`, `user_id`, `complaint`, `by_user`, `approval`) VALUES
(1, 2, '1234', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_id` int(11) NOT NULL,
  `product_name` text NOT NULL,
  `description` text NOT NULL,
  `image_path` text NOT NULL,
  `price` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_id`, `product_name`, `description`, `image_path`, `price`, `user_id`) VALUES
(11, 'LAPTOP', 'vfg', '/static/pic_uploads/1589462252.png', 10000, 2),
(12, 'backpack', 'sdsdv sadfdsf', 'static/pic_uploads/1589504277.png', 960, 2),
(13, 'tripod', 'hfj ugug ougou 8yo8', 'static/pic_uploads/1589504298.jfif', 1150, 2),
(14, 'tv', '4k tv', 'static/pic_uploads/1589504319.jfif', 43500, 2),
(15, 'watch', 'watch', 'static/pic_uploads/1589504338.jfif', 11999, 2),
(16, 'hoodie', 'giyf kfyfkhvk', 'static/pic_uploads/1589504358.jfif', 750, 2),
(17, 'camera', 'gfjyv uyfjyuyrfjyfhggpih ', 'static/pic_uploads/1589504377.jfif', 55000, 2);

-- --------------------------------------------------------

--
-- Table structure for table `return_history`
--

CREATE TABLE `return_history` (
  `id` int(11) NOT NULL,
  `bill_no` int(11) NOT NULL,
  `feedback` text NOT NULL,
  `user_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `approval` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `user_id` int(20) NOT NULL,
  `user_name` varchar(60) NOT NULL,
  `address` varchar(500) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `password` varchar(30) NOT NULL,
  `user_type` varchar(30) NOT NULL,
  `banned` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`user_id`, `user_name`, `address`, `phone_number`, `email_id`, `password`, `user_type`, `banned`) VALUES
(1, 'Vaisakh', 'Kudakattu Madom', '8891812159', 'vaishakhnamboothiri@gmail.com', '1234', 'buyer', 0),
(2, 'anand', 'sdfsdfd', '56546', 'anandbabualpy@gmail.com', '9876', 'seller', 0),
(3, 'fsegsrg', 'fsgsr', '8848484', 'aaa@gmail.com', '1234', 'seller', 0),
(4, 'test', 'fsdgs', '89745222', 'aaa@gmail.com', '123456', 'buyer', 0),
(6, 'Kuttan', 'parambathu House\r\n', '789654321', 'kuttan@gmail.com', '123456', 'admin', 0),
(7, 'Police ', 'POLICE HQ', '09876543211', 'police@gqg.com', '12345', 'buyer', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `billing_history`
--
ALTER TABLE `billing_history`
  ADD PRIMARY KEY (`billing_id`);

--
-- Indexes for table `cancel_history`
--
ALTER TABLE `cancel_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cart_id`);

--
-- Indexes for table `complaint`
--
ALTER TABLE `complaint`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `return_history`
--
ALTER TABLE `return_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `billing_history`
--
ALTER TABLE `billing_history`
  MODIFY `billing_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `cancel_history`
--
ALTER TABLE `cancel_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `cart_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `complaint`
--
ALTER TABLE `complaint`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `return_history`
--
ALTER TABLE `return_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_details`
--
ALTER TABLE `user_details`
  MODIFY `user_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
