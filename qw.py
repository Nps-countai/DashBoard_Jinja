import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
def pp():
    print('df : ',df)
    time.sleep(10)

df = pd.DataFrame()
# Function to load the DataFrame from the CSV file
def load_dataframe():
    df = pd.read_csv('new.csv')  # Replace 'your_data.csv' with your CSV file path
    print("DataFrame loaded at:", pd.Timestamp.now())
    # You can perform any desired operations with the DataFrame here


scheduler = BackgroundScheduler()
scheduler.add_job(load_dataframe, trigger=IntervalTrigger(seconds=10))

# Start the scheduler
scheduler.start()
scheduler1 = BackgroundScheduler()
scheduler1.add_job(pp)

# Start the scheduler
scheduler1.start()

try:
    # Keep the script running
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    # Shut down the scheduler gracefully when exiting the script
    scheduler.shutdown()
