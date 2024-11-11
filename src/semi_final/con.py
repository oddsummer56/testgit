from kafka import KafkaConsumer, TopicPartition
from json import loads
import os
from db import get_conn

consumer = KafkaConsumer(
        "tickets",
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=30000,
        auto_offset_reset='earliest',
        group_id="ticket",
        enable_auto_commit=False,
)

print('[Start] get consumer')

# DB 연결 및 커서 생성
conn = get_conn()
cursor = conn.cursor()

try:
    # Kafka 메시지 수신 및 데이터베이스 저장 루프
    for message in consumer:
        ticket_data = message.value
        print(f"Received: {ticket_data}")

        # 데이터베이스에 데이터 저장
        try:
            # 연결이 열려 있는지 확인하고, 닫혀 있으면 재연결
            if not conn.open:
                print("Database connection is closed. Reconnecting...")
                conn = get_conn()
                cursor = conn.cursor()

            cursor.execute(
                '''
                INSERT INTO ticket_data (event_name, price, date, location, available_tickets)
                VALUES (%s, %s, %s, %s, %s)
                ''',
                (ticket_data['event_name'], ticket_data['price'], ticket_data['date'], ticket_data['location'], ticket_data['available_tickets'])
            )
            conn.commit()  # 각 메시지 처리 후 커밋하여 DB에 반영
            print("Data saved to database.")
            # 오프셋 수동 커밋
            consumer.commit()

        except Exception as e:
            print(f"Error occurred while inserting data: {e}")
            conn.rollback()  # 오류 시 롤백하여 데이터 정합성 유지

finally:
    # Consumer와 DB 연결 닫기
    consumer.close()
    if conn.open:  # 연결이 열린 경우에만 닫기
        cursor.close()
        conn.close()
        print("Database connection closed.")

print('[End] get consumer')
