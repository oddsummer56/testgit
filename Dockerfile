FROM python:3.11

# 작업 디렉터리 설정
WORKDIR /app

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y bash && apt-get install -y vim

# requirements.txt 파일 복사 및 패키지 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 코드 파일 복사
COPY src/semi_final /app
COPY kafka-config.yaml /app/kafka-config.yaml

# 기본 명령어 설정 (여기서는 별도로 설정하지 않고 docker-compose에서 설정)

