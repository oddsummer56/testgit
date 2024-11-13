# 주요 변경사항
0.2/spark_scale 의 주요 변경사항은 다음과 같습니다.

- Apache Spark 공식 이미지(apache/spark:latest)를 사용하도록 변경
- Spark 클러스터의 메모리 및 코어 설정 수정: 과도한 자원 사용을 방지하고, 개발 환경에서의 효율적인 테스트가 가능하게 변경
- Spark 워커의 스케일 조절 : deploy 블록의 replicas 옵션을 추가하여 클러스터의 스케일을 쉽게 조절하게 변경

# Spark Cluster Setup with Docker
![image](https://github.com/user-attachments/assets/69063391-b9b5-4d9d-ba0b-406ba60056f6)

Docker Compose를 사용하여 Apache Spark 클러스터(Master, Worker, Spark-Submit)를 설정하고 관리한다.  
docker-compose.yml 파일을 통해 Spark 클러스터를 실행하고, PySpark 스크립트를 Spark 클러스터에서 자동으로 실행한다.


## 실행 요구사항
- [Docker 설치](https://docs.docker.com/desktop/)
```
docker --version 
```
- [Docker Compose 설치](https://docs.docker.com/compose/install/)
```
docker compose version
```
- app 폴더에 실행할 PySpark 스크립트 (app/pyspark_test.py)

## 사용법

1.  Docker Compose로 Spark 클러스터 빌드 및 시작
```
docker compose up -d --build
```
<br>

2. Spark Web UI 확인
[Spark Master UI](http://localhost:8080) 에서 현재 클러스터 상태, 실행 중인 애플리케이션, 작업의 진행 상황 등을 확인가능
<br>

3. 워커 스케일 조절

```
docker compose up -d --scale spark-worker=<worker N>
```

## 주요명령어
1. 컨테이너 상태 확인
```
docker compose ps
```
2. Spark 클러스터 종료
```
docker compose down
```
3. Spark 클러스터 다시 시작
```
docker compose up -d
```
