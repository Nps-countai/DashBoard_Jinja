import pandas as pd
from datetime import datetime, timedelta

last_hour_date_time = datetime.now() - timedelta(hours = 1)
lh_time = last_hour_date_time.strftime('%Y-%m-%d %H:%M:%S')

from h import add 
df = pd.read_csv('new.csv')
for index, row in df.iterrows():
    if row['lastuv_inspectionOn'] >= lh_time:
        print(row)
    
print(add(3,2))

import datetime

x = datetime.datetime.now() 
print(x)
print(last_hour_date_time.strftime('%Y-%m-%d %H:%M:%S'))


import threading

def my_function():
    # put your code here
    print("Function called every minute")

def run_function():
    thread = threading.Timer(2.0, run_function) # 60 seconds = 1 minute
    thread.start()
    my_function()

run_function() # start the timer