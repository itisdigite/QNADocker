-- init.sql
ALTER USER 'qnauser'@'%' IDENTIFIED WITH mysql_native_password BY 'Pass@000';
GRANT ALL PRIVILEGES ON qna.* TO 'qnauser'@'%';

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS qna;

-- Use the qna database
USE qna;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255),
    password VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    verified TINYINT DEFAULT 0,
    otc VARCHAR(6)
);

-- Create OTC table for storing one-time codes
CREATE TABLE IF NOT EXISTS otc_codes (
    email VARCHAR(255),
    code VARCHAR(6),
    expiry TIMESTAMP
);
