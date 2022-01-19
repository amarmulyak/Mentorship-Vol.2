"""
wait_time

Unit is seconds

between(min, max): simulate random sleep between min and max value
constant(wait_time): inject constant delay between tasks
constant_pacing(wait_time): always injects specified delay, no matter what time execution of the task is;
                            if we take to much time to run the task, than the constant_pacing time would be zero
"""
import time

from locust import User, task, constant, between, constant_pacing


class MyUserConstant(User):
    wait_time = constant(1)

    @task
    def launch(self):
        print('This will inject 1 second delay')


class MyUserBetween(User):
    wait_time = between(2, 5)

    @task
    def launch(self):
        print('This will inject 2-5 seconds delay')


class MyUserConstantPacing_1(User):
    wait_time = constant_pacing(5)

    @task
    def launch(self):
        time.sleep(3)
        print('This will inject 5 seconds delay, even if task will end earlier')


class MyUserConstantPacing_2(User):
    wait_time = constant_pacing(2)

    @task
    def launch(self):
        time.sleep(3)
        print('This will inject 0 seconds delay, as task will execute longer then constant_pacing')


# Run: locust -f exercises/locust/s1_e7_wait_time.py
