-- creates the database hbtn_0d_2 and the user user_0d_2.
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates a user
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant select privileges to a user
GRANT SELECT on hbtn_0d_2.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
