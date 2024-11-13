import json
import subprocess
from configparser import ConfigParser
import os
from datetime import datetime


# PDM 프로젝트 PYPI.ORG 배포 및 CMD 형태로 설치 되도록

# CPU 사용율 기록 -> 추후 화면 그래프 표시
# 스케일 인/아웃 이벤트 시점 기록(파일 또는 DB) -> 추후 화면 그래프 표시

pwd = os.path.dirname(os.path.abspath(__file__))

# X 에 대한 값을 설정 파일을 통해 읽어 오기
def get_config():
    cp = ConfigParser()
    cp.read(f"{pwd}/config.ini")

    config=dict()
    for i in cp:
        for j in cp[i]:
            config[j]=float(cp[i][j])

    return config

def get_max_cpu_use():
    cp = ConfigParser()
    cp.read(f"{pwd}/config.ini")

    return float(cp["limit"]["max_cpu_use"])

def get_min_cpu_use():
    cp = ConfigParser()
    cp.read(f"{pwd}/config.ini")

    return float(cp["limit"]["min_cpu_use"])

def get_max_cnt():
    cp = ConfigParser()
    cp.read(f"{pwd}/config.ini")

    return float(cp["scale"]["max_cnt"])

def get_min_cnt():
    cp = ConfigParser()
    cp.read(f"{pwd}/config.ini")

    return float(cp["scale"]["min_cnt"])



# CPU 사용율 10초당 한번씩 확인
# CPU 사용율이 X% 를 기준으로 1분간 이상이면 스케일 아웃
# 1분간 이하 이면 스케일 인
def docker_stats():
    rst = subprocess.run(["docker","stats","--format","json","--no-stream"], capture_output=True)
    rst = rst.stdout.decode("utf-8").strip()

    l = list(map(json.loads,rst.split("\n")))

    return l

def get_stat_dict():
    l = docker_stats()

    return {x["Name"]:x["CPUPerc"] for x in l}

def get_worker():
    rst_d=get_stat_dict()

    return {k:rst_d[k] for k in list(filter(lambda x:"worker" in x, rst_d))}

def get_worker_cnt():
    return len(get_worker())

# 수동 스케일 인/아웃 기능 -> 추후 화면에서 버튼 이벤트 등으로 처리
def do_scale(method,worker_cnt):
    match method:
        case "in":
            if worker_cnt>1:
                print("scale in")
                subprocess.run(["docker","compose","up","--scale",f"spark-worker={worker_cnt-1}"])
            else:
                print(f"최소 worker를 유지합니다.({get_min_cnt()})")
        case "out":
            if worker_cnt<10:
                print("scale out")
                subprocess.run(["docker","compose","up","--scale",f"spark-worker={worker_cnt+1}"])
            else:
                print(f"최대 worker를 유지합니다.({get_max_cnt()})")
        case _:
            raise Exception("NotDefinedParameter")



# 스케일 인/아웃 시 LINE NOTI 발송
def line_notify(msg):
    import requests as reqs
    import os

    headers = {
        'Authorization': f'Bearer {os.getenv("LINE_TOKEN")}',
    }

    message = {
        'message': msg,
    }

    response = reqs.post('https://notify-api.line.me/api/notify', headers=headers, data=message).json()
    return response

def save_log(path, data):
    today=f"{datetime.now().year}{datetime.now().month}{datetime.now().day}"
    log_path=f"{pwd}/{path}"
    log_file_path=f"{log_path}/log_{today}.log"

    os.makedir(log_path, exist_ok=True)

    if os.path.exists(log_file_path)!=True:
        f=open(log_file_path)
        match path:
            case "scale":
                f.write("method,cnt_before,cnt_after,time")
            case "usage":
                f.write("cpu_use,cnt_curr,time,status")
            case _:
                raise Exception("NotDefinedParameter")
        f.close()

    with open(log_file_path,"a") as f:
        f.write(data)
    return "success"
