from tkinter import *
from datetime import datetime
import time

c = Canvas(width=700, height=300, background='#000')
c.pack()
try:
    while True:
        now = datetime.now()
        s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)
        c.create_rectangle(0, 0, 700, 300, outline='white', fill='white')
        c.create_text(350, 150, text=s, font=('', 100), fill='black')
        c.update()
        time.sleep(0.1)
except:
    pass