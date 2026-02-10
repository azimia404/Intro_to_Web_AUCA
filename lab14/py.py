import time
from datetime import datetime, timedelta

now = datetime.now()

formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", formatted_now)


today = datetime.now()

new_years_eve = datetime(today.year, 12, 31)

if today > new_years_eve:
    new_years_eve = datetime(today.year + 1, 12, 31)

time_until_new_year = new_years_eve - today

print("Days until New Year's Eve:", time_until_new_year.days)


def countdown_timer(seconds):
    end_time = datetime.now() + timedelta(seconds=seconds)
    while True:
        remaining = end_time - datetime.now()
        total_seconds = int(remaining.total_seconds())

        if total_seconds <= 0:
            print("Time remaining: 0 seconds")
            break
        
        print(f"Time remaining: {total_seconds} seconds", end="\r")
        time.sleep(1)
    print("\nTimer finished!")

countdown_timer(10)