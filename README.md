# Spark Cluster Setup with Docker
![image](https://github.com/user-attachments/assets/69063391-b9b5-4d9d-ba0b-406ba60056f6)

Docker Compose를 사용하여 Apache Spark 클러스터(Master, Worker, Spark-Submit)를 설정하고 관리한다.  
docker-compose.yml 파일을 통해 Spark 클러스터를 실행하고, PySpark 스크립트를 Spark 클러스터에서 자동으로 실행한다.
Scale Up

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
1.  Docker Compose로 Spark 클러스터 시작
```
docker compose up -d
```

2. Spark Web UI 확인  
[Spark Master UI](http://localhost:8080) 에서 현재 클러스터 상태, 실행 중인 애플리케이션, 작업의 진행 상황 등을 확인가능

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
dockercompose up -d
```
