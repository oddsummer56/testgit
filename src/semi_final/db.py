import pymysql.cursors
import os

def get_conn():
    conn = pymysql.connect(
                            host="13.124.42.108",            # 컨테이너 이름을 호스트로 사용
                            port=6033,
                            user=os.getenv('DB_USER'),
                            password=os.getenv('DB_PASSWORD'),
                            database="ticket",
                            cursorclass=pymysql.cursors.DictCursor)
    return conn
