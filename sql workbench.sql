CREATE DATABASE library_management;

USE library_management;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    accession_no VARCHAR(50) UNIQUE,
    title VARCHAR(255),
    author VARCHAR(255),
    category VARCHAR(100),
    publisher VARCHAR(255),
    year_published INT,
    isbn VARCHAR(30),
    copies INT
);