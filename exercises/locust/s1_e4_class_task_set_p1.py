"""
class TaskSet

Executes a set of tasks
It helps to structure the hierarchical
Picks up a task -> Executes it -> wait_time in TaskSet, else wait in User
TaskSet can be nested

client: instance of HttpSession
interrupt
on_start(): run something on start of instantiating a class
on_stop(): same
parent
tasks: list of tasks
user
wait()
wait_time()
"""

import random

from locust import TaskSet, HttpUser, constant, task


class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        res = self.client.get('/200')
        print(f'Get Status of 200: {res.status_code}')

    @task
    def get_random_status(self):
        status_codes = [100, 101, 102,
                        200, 201, 202,
                        300, 301, 302,
                        400, 401, 403, 404,
                        500, 501, 502, 503, 504]
        random_url = '/' + str(random.choice(status_codes))

        res = self.client.get(random_url)
        print(f'Random http status: {res.status_code}')


class MyLoadTest(HttpUser):
    host = 'https://http.cat'
    tasks = [MyHTTPCat]
    wait_time = constant(1)


# To run the file we need User or HttpUser class and specification of which tasks should be executed:
# locust -f exercises/locust/s1_e4_class_task_set.py
