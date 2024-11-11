import pymysql.cursors
import os

def get_conn():
    conn = pymysql.connect(
                            host="mariadb",            # 컨테이너 이름을 호스트로 사용
                            port=3306,
                            user="tut",
                            password="tut1234",
                            database="ticket",
                            cursorclass=pymysql.cursors.DictCursor)
    return conn
