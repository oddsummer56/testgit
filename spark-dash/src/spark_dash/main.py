import streamlit as st
from time import time
from time import sleep
import pandas as pd

from spark_dash.utils import *

def list2df():
    l = docker_stats()
    df = pd.DataFrame(l)

    return df


t=time()

st.title("Dashboard")

row1 = st.empty()
row2 = st.empty()
row3 = st.empty()
l,r = row3.columns([1,2])
row4 = st.empty()

if l.button("scale in"):
    do_scale("in",get_worker_cnt())
    line_notify(f"worker의 수를 {get_worker_cnt()}개로 scale in하였습니다.")
    st.rerun()
if r.button("scale out"):
    do_scale("out",get_worker_cnt())
    print(line_notify(f"worker의 수를 {get_worker_cnt()}개로 scale out하였습니다."))

    st.rerun()

highTime,lowTime=0,0

while 1:
    #if (t+10)//10 == time()//10:
    #t=time()
    cpu_use=max(map(lambda x:float(x.replace("%","")),get_worker().values()))

    row1.table(list2df()[["Name","CPUPerc","MemUsage","MemPerc"]])

    if cpu_use > get_max_cpu_use():
        highTime+=10
    else:
        highTime=0

    if (get_worker_cnt() > 1) and (cpu_use < get_min_cpu_use()):
        lowTime+=10
    else:
        lowTime=0

    row4.write([highTime, lowTime, cpu_use , get_min_cpu_use()])

    if highTime==60:
        do_scale("out",get_worker_cnt())
        print(line_notify(f"worker의 수를 {get_worker_cnt()}개로 scale out하였습니다."))
        highTime=0
        st.rerun()
    elif lowTime==60:
        do_scale("in",get_worker_cnt())
        line_notify(f"worker의 수를 {get_worker_cnt()}개로 scale in하였습니다.")
        lowTime=0
        st.rerun()

    #row2.progress(int(time()-t)*10)
    row2.progress(max(lowTime,highTime)*100//60)
    sleep(10)