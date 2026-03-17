-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema LittleLemon
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema LittleLemon
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `LittleLemon`;
CREATE SCHEMA IF NOT EXISTS `LittleLemon` DEFAULT CHARACTER SET utf8 ;
USE `LittleLemon` ;

-- -----------------------------------------------------
-- Table `LittleLemon`.`Bookings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`Bookings` (
  `BookingId` INT NOT NULL AUTO_INCREMENT,
  `Date` DATETIME NOT NULL,
  `TableNo` INT NOT NULL,
  PRIMARY KEY (`BookingId`),
  UNIQUE INDEX `BookingID_UNIQUE` (`BookingId` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemon`.`MenuStarters`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`MenuStarters` (
  `StarterId` INT NOT NULL,
  `StarterName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`StarterId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemon`.`MenuCourses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`MenuCourses` (
  `CourseId` INT NOT NULL,
  `CourseName` VARCHAR(45) NULL,
  PRIMARY KEY (`CourseId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemon`.`MenuDrinks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`MenuDrinks` (
  `DrinkId` INT NOT NULL,
  `DrinkName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`DrinkId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemon`.`MenuDesserts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`MenuDesserts` (
  `DessertId` INT NOT NULL,
  `DessertName` VARCHAR(45) NULL,
  PRIMARY KEY (`DessertId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemon`.`MenuCuisines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`MenuCuisines` (
  `CuisineId` INT NOT NULL,
  `CuisineName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CuisineId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemon`.`Menu`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`Menu` (
  `MenuId` INT NOT NULL AUTO_INCREMENT,
  `StarterId` INT NULL,
  `CourseId` INT NOT NULL,
  `DessertId` INT NULL,
  `DrinkId` INT NULL,
  `CuisineId` INT NULL,
  PRIMARY KEY (`MenuId`),
  CONSTRAINT `StarterId`
    FOREIGN KEY (`StarterId`)
    REFERENCES `LittleLemon`.`MenuStarters` (`StarterId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `CourseId`
    FOREIGN KEY (`CourseId`)
    REFERENCES `LittleLemon`.`MenuCourses` (`CourseId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `DrinkId`
    FOREIGN KEY (`DrinkId`)
    REFERENCES `LittleLemon`.`MenuDrinks` (`DrinkId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `DessertId`
    FOREIGN KEY (`DessertId`)
    REFERENCES `LittleLemon`.`MenuDesserts` (`DessertId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `CuisineId`
    FOREIGN KEY (`CuisineId`)
    REFERENCES `LittleLemon`.`MenuCuisines` (`CuisineId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemon`.`OrderStatus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`OrderStatus` (
  `StatusId` INT NOT NULL AUTO_INCREMENT,
  `DeliveryStatus` VARCHAR(45) NULL,
  PRIMARY KEY (`StatusId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemon`.`Addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`Addresses` (
  `AddressId` INT NOT NULL,
  `Pincode` VARCHAR(25) NULL,
  `City` VARCHAR(45) NULL,
  `State` VARCHAR(45) NULL,
  `Country` VARCHAR(45) NULL,
  PRIMARY KEY (`AddressId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemon`.`Customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`Customer` (
  `CustomerId` INT NOT NULL AUTO_INCREMENT,
  `CustName` VARCHAR(45) NOT NULL,
  `CustPhone` INT NOT NULL,
  `CustEmail` VARCHAR(45) NOT NULL,
  `AddressId` INT NOT NULL,
  PRIMARY KEY (`CustomerId`),
  UNIQUE INDEX `CustomerID_UNIQUE` (`CustomerId` ASC) VISIBLE,
  CONSTRAINT `AddressId`
    FOREIGN KEY (`AddressId`)
    REFERENCES `LittleLemon`.`Addresses` (`AddressId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemon`.`Staff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`Staff` (
  `StaffId` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `PhoneNum` INT NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`StaffId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemon`.`Orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`Orders` (
  `OrderId` INT NOT NULL AUTO_INCREMENT,
  `OrderDate` DATETIME NOT NULL,
  `Quantity` INT NOT NULL,
  `TotalCost` DECIMAL(6) NOT NULL,
  `DeliveryId` INT,
  `StaffId` INT NOT NULL,
  `BookingId` INT NOT NULL,
  `MenuId` INT NOT NULL,
  `CustomerId` INT NOT NULL,
  PRIMARY KEY (`OrderId`),
  CONSTRAINT `CustomerID`
    FOREIGN KEY (`CustomerId`)
    REFERENCES `LittleLemon`.`Customer` (`CustomerId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `MenuId`
    FOREIGN KEY (`MenuId`)
    REFERENCES `LittleLemon`.`Menu` (`MenuId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `BookingID`
    FOREIGN KEY (`BookingId`)
    REFERENCES `LittleLemon`.`Bookings` (`BookingId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `StaffId`
    FOREIGN KEY (`StaffId`)
    REFERENCES `LittleLemon`.`Staff` (`StaffId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `DeliveryId`
    FOREIGN KEY (`DeliveryId`)
    REFERENCES `LittleLemon`.`OrderDeliveryStatus` (`DeliveryId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `LittleLemon`.`OrderDeliveryStatus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemon`.`OrderDeliveryStatus` (
  `DeliveryId` INT NOT NULL AUTO_INCREMENT,
  `OrderId` INT NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  `DeliveryTime` DATETIME NOT NULL,
  PRIMARY KEY (`DeliveryId`),
  CONSTRAINT `fk_delivery_order`
    FOREIGN KEY (`OrderId`)
    REFERENCES `LittleLemon`.`Orders` (`OrderId`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


SHOW DATABASES;

USE LittleLemon;

SHOW TABLES;

