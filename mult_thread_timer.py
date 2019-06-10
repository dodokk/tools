from time import sleep
from threading import Thread

target_time = int(input("time(s) = "))

def up_timer(secs):
    for i in range(0,secs+1):
        print(i, end="")
        sleep(1)
    print("カウントアップ終了！")

def down_timer(secs):
    for i in range(secs, -1, -1):
        print(" ",i)
        sleep(1)
    print("カウントダウン終了！")

thread_1 = Thread(target=up_timer,args=(target_time,))
thread_2 = Thread(target=down_timer,args=(target_time,))

thread_1.start()
sleep(0.001)
thread_2.start()
