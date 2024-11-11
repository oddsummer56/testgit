import pymysql.cursors
import os

def get_conn():
    conn = pymysql.connect(host=os.getenv("DB", "127.0.0.1"),
                            user='tut',
                            password=os.getenv("PWD", "tut1234"),
                            database='ticket',
                            port= int(os.getenv('DB_PORT', 53306)),
                            cursorclass=pymysql.cursors.DictCursor)
    return conn
