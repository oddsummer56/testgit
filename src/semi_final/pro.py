from kafka import KafkaProducer
import time
import json
import yaml

# YAML 설정 파일 불러오기
with open("/app/kafka-config.yaml", 'r') as f:
    config = yaml.safe_load(f)

producer_config = config['kafka']['producer']


def create_kafka_producer(retries=5, delay=5):
    for attempt in range(retries):
        try:
            producer = KafkaProducer(
                    bootstrap_servers=producer_config['bootstrap_servers'],
                    value_serializer=lambda x:json.dumps(x).encode('utf-8')
                    )
            print("Kafka Producer 연결 성공")
            return producer
        except Exception as e:
            print(f"Kafka 브로커가 준비되지 않음. {delay}초 후 다시 시도 ({attempt+1}/{retries})")
            time.sleep(delay)

    print("Kafka 브로커에 연결할 수 없습니다.")
    return None

# 프로듀서 생성 시도
producer = create_kafka_producer()


# 예시 크롤링 데이터 (티켓 사이트에서 크롤링했다고 가정)
def fetch_ticket_data():
    return {
        'event_name': 'Concert ham test',
        'price': 100,
        'date': '2024-12-01',
        'location': 'City Hall',
        'available_tickets': 50
    }


start = time.time()

ticket_data = fetch_ticket_data()

if producer:
    producer.send(producer_config['topic'], value=ticket_data)
    producer.flush()
    time.sleep(1) # 1초 간격으로 전송
    end = time.time()
    print("[DONE]:", end-start)
else:
    print("프로듀서 연결 실패로 종료")

