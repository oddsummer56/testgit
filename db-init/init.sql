-- 데이터베이스와 테이블 생성 예제

CREATE DATABASE IF NOT EXISTS ticket;

USE ticket;

CREATE TABLE IF NOT EXISTS ticket_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    price VARCHAR(100) NOT NULL,
    date VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    available_tickets VARCHAR(100) NOT NULL
);

