#coding:UTF-8
import schedule
import time


def jobA():
    #ここにメインの処理を書く
    print("Aが実行されました")


def jobB():
    #ここにメインの処理を書く
    print("Bが実行されました")


schedule.every(1).seconds.do(jobA)
schedule.every(5).seconds.do(jobB)

#10分毎にjobを実行
# schedule.every(10).minutes.do(job)

#毎時間ごとにjobを実行
# schedule.every().hour.do(job)

#AM10:30にjobを実行
# schedule.every().day.at("10:30").do(job)

#月曜日にjobを実行
# schedule.every().monday.do(job)

#水曜日の13:15にjobを実行
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
