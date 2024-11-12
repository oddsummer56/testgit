import pymysql.cursors
import os

def get_conn():
    conn = pymysql.connect(
                            host="13.124.42.108",            # 컨테이너 이름을 호스트로 사용
                            port=6033,
                            user="tut",
                            password="tut1234",
                            database="ticket",
                            cursorclass=pymysql.cursors.DictCursor)
    return conn
