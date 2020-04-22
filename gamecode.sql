-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 22, 2020 at 09:31 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gamecode`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `BIRTH_DATE` date DEFAULT NULL,
  `register_date` date DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `zipcode` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `firstname`, `lastname`, `BIRTH_DATE`, `register_date`, `address`, `zipcode`, `city`, `phone_number`) VALUES
(1, 'Lisa', 'WILLIAMS', '1987-01-15', '1987-01-15', NULL, NULL, 'Tokyo', '03-6487-3260'),
(2, 'John', 'WILLIAMS', NULL, NULL, '144 avenue de l\'europe', '34000', 'Montpellier', '+33768234821'),
(3, 'Mary', 'BROWN', '1991-05-29', '1991-05-29', NULL, '00129', 'Moscow', NULL),
(4, 'Paul', 'HARRIS', '1995-08-24', '1995-08-24', NULL, '00501', 'New York', '(718) 555-5987'),
(5, 'Elizabeth', 'JACKSON', '1950-05-13', '1950-05-13', '23, Istiklal Avenue', '34000', 'Istanbul', NULL),
(6, 'Matthew', 'WHITE', '1966-11-21', '1966-11-21', NULL, NULL, 'Beijing', NULL),
(7, 'Jean-Claude', 'DUCE', '1963-09-26', '1963-09-26', NULL, '34000', 'Montpellier', NULL),
(8, 'James', 'POTTER', '1975-01-17', '1975-01-17', NULL, '34000', 'Montpellier', NULL),
(9, 'Roger', 'POULTON', '1991-07-04', '1991-07-04', NULL, '00554', 'New York', NULL),
(10, 'James', 'SMITH', '1985-07-18', '1985-07-18', '16 rue de l\'eglise', '75000', 'Pariss', '+33648516794'),
(12, '5cvbcvb', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(13, '5rtyfgh', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `order_product`
--

CREATE TABLE `order_product` (
  `Id` int(11) NOT NULL,
  `order_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_product`
--

INSERT INTO `order_product` (`Id`, `order_id`, `product_id`) VALUES
(1, 1, 19),
(2, 2, 4),
(3, 2, 20),
(4, 2, 10),
(5, 3, 10),
(6, 3, 13),
(7, 4, 2),
(8, 4, 18),
(9, 5, 7),
(10, 6, 5),
(11, 7, 15),
(12, 7, 8),
(13, 7, 17),
(14, 7, 18),
(15, 7, 14),
(16, 8, 14),
(17, 9, 17),
(18, 9, 11),
(19, 10, 16),
(20, 11, 18),
(21, 11, 1),
(22, 12, 8),
(23, 12, 1);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL,
  `product_category_id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `price` decimal(5,2) DEFAULT NULL,
  `available_stock` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `product_category_id`, `name`, `description`, `price`, `available_stock`) VALUES
(1, 6, 'Leap motion', NULL, '94.00', 864),
(2, 6, 'Chromecast', 'Google Chromecast HDMI Streaming Media Player', '589.99', 65),
(3, 6, 'Samsung UE46F6100', 'Samsung UE46F6100 TV LCD 46 (117 cm) LED 3D HD', '90.20', 21),
(4, 6, 'TomTom XL Classic Europe 23', NULL, '9.57', 15),
(5, 1, 'The Orphan Master\'s Son: A Novel', 'Pulitzer Prize for Fiction', '18.34', 53),
(6, 1, 'War of the Whales: A True Story', NULL, '13.80', 3287),
(7, 1, 'The Fracking King: A Novel', NULL, '18.09', 150),
(8, 1, 'California: A Novel', NULL, '301.22', 1237),
(9, 2, 'DuroStar DS4000S', '4-Cycle Gas Powered Portable Generator', '299.00', 3287),
(10, 2, 'Weber 781001', 'Gold One-Touch 26-1/2-Inch Kettle Grill, Black', '999.99', 58),
(11, 2, 'Intex Rectangular Ultra Frame Pool Set', '24-Feet by 12-Feet by 52-Inch', '172.73', 7),
(12, 2, 'GreenWorks 25022', '12 Amp 20-in 3-in-1 Electric Lawn Mower', '251.49', 20),
(13, 2, 'VIFAH V501', 'Outdoor Wood Serving Cart', '251.49', 12),
(14, 3, 'ProForm 6.0 RT', 'Treadmills ', '499.99', 12),
(15, 3, 'Weider 190 RX', 'Weight Bench', '100.90', 28),
(16, 3, 'Ab Wheel', 'Abdominal Exercise Roller', '17.99', 98),
(17, 5, 'ACDelco CF178', 'Cabin Air Filter', '23.13', 12),
(18, 5, 'Wilwood 260-11179', 'Proportioning Valve', '67.99', 89),
(19, NULL, 'Electrical PVC Insulation Adhesive Tape', 'Yellow', '2.68', 654),
(20, NULL, 'HC-SR04', 'Ultrasonic Sensor Distance Measuring Module', '2.71', 145);

-- --------------------------------------------------------

--
-- Table structure for table `product_category`
--

CREATE TABLE `product_category` (
  `product_category_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product_category`
--

INSERT INTO `product_category` (`product_category_id`, `name`, `description`) VALUES
(1, 'Books', NULL),
(2, 'Garden', 'All for your sweet home'),
(3, 'Fitness', NULL),
(4, 'Video Games', NULL),
(5, 'Automotive', NULL),
(6, 'High-tech', 'All the best devices');

-- --------------------------------------------------------

--
-- Table structure for table `purchase_order`
--

CREATE TABLE `purchase_order` (
  `order_id` int(11) NOT NULL,
  `customer_id` int(255) DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `purchase_order`
--

INSERT INTO `purchase_order` (`order_id`, `customer_id`, `date`) VALUES
(1, 1, '2013-11-02'),
(2, 10, '2012-10-03'),
(3, 4, '2003-04-08'),
(4, 4, '1999-12-29'),
(5, 5, '2011-11-01'),
(6, 1, '2014-01-07'),
(7, 4, '2002-04-25'),
(8, 3, '2003-04-14'),
(9, 4, '2005-08-14'),
(10, 1, '2010-12-29'),
(11, 5, '2009-01-03'),
(12, 1, '2011-12-29');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `order_product`
--
ALTER TABLE `order_product`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `product_category_id` (`product_category_id`);

--
-- Indexes for table `product_category`
--
ALTER TABLE `product_category`
  ADD PRIMARY KEY (`product_category_id`);

--
-- Indexes for table `purchase_order`
--
ALTER TABLE `purchase_order`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `order_product`
--
ALTER TABLE `order_product`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `product_category`
--
ALTER TABLE `product_category`
  MODIFY `product_category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `purchase_order`
--
ALTER TABLE `purchase_order`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `order_product`
--
ALTER TABLE `order_product`
  ADD CONSTRAINT `order_product_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `purchase_order` (`order_id`),
  ADD CONSTRAINT `order_product_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`);

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_category_id` FOREIGN KEY (`product_category_id`) REFERENCES `product_category` (`product_category_id`);

--
-- Constraints for table `purchase_order`
--
ALTER TABLE `purchase_order`
  ADD CONSTRAINT `purchase_order_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
