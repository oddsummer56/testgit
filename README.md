## Kafka yaml 실행
```bash
sudo docker compose up -d --build
```

## Broker Logs 확인
```bash
sudo docker logs kafka1
sudo docker logs kafka2
sudo docker logs kafka3
```

## MariaDB 컨테이너 접속
```bash
sudo docker exec -it mariadb bash
```

## MariaDB 확인
```bash
mariadb -utut -p
use ticket;
select * from ticket_data;
```



