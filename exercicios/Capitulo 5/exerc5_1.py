"""Precisei de uma colinha para resolver esse exercício."""

import time

def current_time():
    current = time.time()
    t_sec = current % 86400  
    c_hours = int(t_sec / 3600)
    t_minutes = int(t_sec / 60)
    c_mins = t_minutes % 60
    c_sec = int(t_sec % 60)

    days = int(current / 86400)
   
    print("The Current time is", c_hours, ':', c_mins, ':', c_sec)
    print("Days Since epoch:", days)

current_time()
