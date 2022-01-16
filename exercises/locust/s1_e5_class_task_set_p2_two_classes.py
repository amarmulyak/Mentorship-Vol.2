"""
class TaskSet

self.interrupt(reschedule=True)

Two examples:
    - nested TaskSet
    - two classes TaskSet

"""

from locust import TaskSet, HttpUser, constant, task


class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        res = self.client.get('/200')
        print(f'Get Status of 200: {res.status_code}')
        self.interrupt(reschedule=False)


class MyAnotherHTTPCat(TaskSet):

    @task
    def get_500_status(self):
        res = self.client.get('/500')
        print(f'Get Status of 500: {res.status_code}')
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser, MyAnotherHTTPCat):
    host = 'https://http.cat'
    tasks = [MyHTTPCat]
    wait_time = constant(1)


# Run: locust -f exercises/locust/s1_e5_class_task_set_p2_two_classes.py

# Both classes should be specified in tasks
# But it will execute only first task class
# # To leverage this we need to add self.interrupt() in both task classes
