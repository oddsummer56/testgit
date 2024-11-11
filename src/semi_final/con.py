from kafka import KafkaConsumer, TopicPartition
from json import loads
import os
from db import get_conn

consumer = KafkaConsumer(
        "tickets",
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=5000,
        #auto_offset_reset='earliest' if saved_offset is None else 'none',
        group_id="ticket_consumer",
        enable_auto_commit=False,
)

print('[Start] get consumer')


#DB 불러오기
conn = get_conn()

# 데이터 읽기 및 DB 저장
for message in consumer:
    ticket_data = message.value
    print(f"Received: {ticket_data}")

    # DB에 데이터 저장
    cursor.execute(
                    '''
                    INSERT INTO ticket_data (event_name, price, date, location, available_tickets) 
                    VALUES (%s, %s, %s, %s, %s)
                    ''',
                    (ticket_data['event_name'], ticket_data['price'], ticket_data['date'], ticket_data['location'], ticket_data['available_tickets']))
    conn.commit()
    print("Data saved to database.")

# Consumer 종료 후 DB 연결 닫기
consumer.close()
conn.close()


print('[End] get consumer')
