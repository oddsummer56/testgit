-- 모든 사람에게 'ticket' 데이터베이스에 대한 모든 권한 부여
GRANT ALL PRIVILEGES ON ticket.* TO 'tut'@'%' IDENTIFIED BY 'tut1234';
FLUSH PRIVILEGES;

