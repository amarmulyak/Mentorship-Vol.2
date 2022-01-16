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

    @task
    class MyAnotherHTTPCat(TaskSet):

        @task
        def get_500_status(self):
            res = self.client.get('/500')
            print(f'Get Status of 500: {res.status_code}')
            self.interrupt(reschedule=False)

class MyLoadTest(HttpUser):
    host = 'https://http.cat'
    tasks = [MyHTTPCat]
    wait_time = constant(1)


# Run: locust -f exercises/locust/s1_e5_class_task_set_p2_nested.py

# If locust gets into nested class it never comes out
# To leverage this we need to use self.interrupt()

# self.interrupt() has parameter 'reschedule' which is set to True by default
# it means that task immediately goes to parent class without any wait time
# in case of reschedule=False both task will have the same wait time of execution
