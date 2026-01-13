from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

def task_one():
    # Define the first task to be executed
    print("Task One executed at", datetime.datetime.now())

def task_two():
    # Define the second task to be executed
    print("Task Two executed at", datetime.datetime.now())

scheduler = BlockingScheduler()

# Schedule task_one to run at 10-second intervals
scheduler.add_job(task_one, 'interval', seconds=10)

# Schedule task_two to run at 15-second intervals
scheduler.add_job(task_two, 'interval', seconds=15)

try:
    print("Task manager started. Press Ctrl+C to exit.")
    scheduler.start()
except KeyboardInterrupt:
    print("Task manager terminated.")
finally:
    print("end.")
