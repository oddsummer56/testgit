from kafka import KafkaProducer
import time
from json import dumps
from tqdm import tqdm

producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x:json.dumps(x).encode('utf-8')
)

# 예시 크롤링 데이터 (티켓 사이트에서 크롤링했다고 가정)
def fetch_ticket_data():
    return {
        'event_name': 'Concert ham',
        'price': 100,
        'date': '2024-12-01',
        'location': 'City Hall',
        'available_tickets': 50
    }


start = time.time()

for i in tqdm(range(5)):
    ticket_data = fetch_ticket_data()
    producer.send('tickets', value=ticket_data)
    producer.flush()
    time.sleep(1) # 1초 간격으로 전송

end = time.time()
print("[DONE]:", end-start)
