# Kafka 클러스터 및 프로듀서, 컨슈머 설정
이 프로젝트에서는 Docker Compose를 사용하여 Kafka 브로커 3개, Zookeeper 3개, Kafka 프로듀서 및 Kafka 컨슈머를 설정합니다. 이 구성은 분산 메시징 시스템인 Kafka를 여러 브로커와 Zookeeper 인스턴스에서 실행하며, 데이터를 생성하고 소비할 수 있는 프로듀서와 컨슈머를 포함합니다.
<b></b>

## 프로젝트 구성
1. Kafka 브로커 3개 (`kafka1`, `kafka2`, `kafka3`)
2. Zookeeper 3개 (`zookeeper1`, `zookeeper2`, `zookeeper3`)
3. Kafka 프로듀서 (메시지를 생성하는 역할)
4. Kafka 컨슈머 (메시지를 소비하는 역할)
<b></b>

## 카프카 클러스터 구성
<img width="1118" alt="스크린샷 2024-11-13 17 43 10" src="https://github.com/user-attachments/assets/efc0e822-e3a8-42a0-a8ef-acf3088b7792">
<b></b>

## 요구사항
- docker
- docker compose
- mariaDB (외부서버에서 실행)
<b></b>

## 실행
```bash
git clone https://github.com/Team1-TU-tech/semi_final.git
git checkout -t origin/0.4.1/kafka
```

```bash
sudo docker compose up -d --build
```
<b></b>

## 브로커 로그 확인
```bash
sudo docker logs kafka1
sudo docker logs kafka2
sudo docker logs kafka3
```
<b></b>

## 프로듀서와 컨슈머
Kafka 프로듀서와 Kafka 컨슈머는 기본적으로 `Dockerfile`을 빌드하여 실행합니다.
프로듀서는 tickets라는 주제로 메시지를 보내고, 컨슈머는 이 메시지를 소비합니다.

## 종료
```bash
sudo docker compose down
```
로그와 상태를 확인한 후 필요에 따라 클러스터를 종료하고, 모든 리소스를 정리할 수 있습니다.
