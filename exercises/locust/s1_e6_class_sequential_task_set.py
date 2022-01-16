"""
class TaskSet

Define the tasks in a sequential order
All tasks executed in an order
Task weight attribute will be ignored

client: instance of HttpSession
interrupt(reschedule=True)
on_start(): run something on start of instantiating a class
on_stop(): same
parent
tasks: list of tasks
schedule_task(task_callable, first=False)
user
wait_time()
"""

from locust import SequentialTaskSet, HttpUser, constant, task


class MySeqTask(SequentialTaskSet):

    @task
    def get_status(self):
        res = self.client.get('/200')
        print(f'Get Status of 200: {res.status_code}')

    @task
    def get_500_status(self):
        res = self.client.get('/500')
        print(f'Get Status of 500: {res.status_code}')


class MyLoadTest(HttpUser):
    host = 'https://http.cat'
    tasks = [MySeqTask]
    wait_time = constant(1)


# Run: locust -f exercises/locust/s1_e6_class_sequential_task_set.py
