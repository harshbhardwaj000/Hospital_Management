CREATE DATABASE hospital_management;

USE hospital_management;

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    diagnosis VARCHAR(255),
    contact_number VARCHAR(15)
);
