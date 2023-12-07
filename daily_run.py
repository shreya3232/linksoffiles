import schedule
import time
def run_daily_code():
    # Add your code here
    print("Running code at 11:00 AM")
schedule.every().day.at("10:27").do(run_daily_code)
while True:
    schedule.run_pending()
    time.sleep(1)
