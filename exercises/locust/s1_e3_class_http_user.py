from locust import HttpUser, task, constant


class MyReqRes(HttpUser):
    """
    abstract = True
    client: instance of HttpSession
    """

    host = 'https://reqres.in'
    wait_time = constant(1)

    @task
    def get_users(self):
        res = self.client.get('/api/users?page=2')
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task
    def create_user(self):
        payload = '{"name": "morpheus", "job": "leader"}'

        res = self.client.post('/api/users', data=payload)
        print(res.text)
        print(res.status_code)
        print(res.headers)


# Launch in terminal: locust -f ./exercises/locust/s1_e3_class_http_user.py
# e.g. number: 1, spawn: 1 (don't run too many users to no not damage the site)
# Host can be set as parameter in the class or it can be set during the launching via command line:
# e.g. locust -f ./exercises/locust/s1_e3_class_http_user.py --host=https://reqres.in
