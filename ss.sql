create database HackerDB1;
use HackerDB1;
CREATE TABLE hackernews_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT NOT NULL,
    link TEXT NOT NULL
);
select * from hackernews_data;