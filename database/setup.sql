-- ==========================================
-- Library Management System Database Setup
-- ==========================================

DROP DATABASE IF EXISTS library_management;

CREATE DATABASE library_management;

USE library_management;

-- ==========================================
-- Librarians Table
-- ==========================================

CREATE TABLE librarians (
    id INT AUTO_INCREMENT PRIMARY KEY,
    librarian_id VARCHAR(50) UNIQUE NOT NULL,
    librarian_name VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO librarians
(librarian_id, librarian_name, password)
VALUES
('admin', 'Administrator', 'admin123');

-- ==========================================
-- Books Table
-- ==========================================

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    accession_no VARCHAR(50),
    title VARCHAR(255),
    author VARCHAR(255),
    category VARCHAR(100),
    publisher VARCHAR(255),
    year_published INT,
    isbn VARCHAR(50),
    copies INT DEFAULT 1
);