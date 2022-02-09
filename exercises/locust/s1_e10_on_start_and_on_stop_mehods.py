"""
Users and TaskSet class has on_start() and on_stop() methods
Don't use @task decorator for these methods
It executes only once
"""

from locust import User, task, constant, SequentialTaskSet, HttpUser, TaskSet


# class MyTest(User):
#     wait_time = constant(1)
#
#     def on_start(self):
#         print('Starting')
#
#     @task
#     def task_1(self):
#         print('My task 1')
#
#     def on_stop(self):
#         print('Stopping')

# Run: locust -f exercises/locust/s1_e10_on_start_and_on_stop_mehods.py -r 1 -u 1 -t 10s --headless --only-summary


# class MyTestSequentialTaskSet(SequentialTaskSet):
#
#     def on_start(self):
#         self.client.get('/', name=self.on_start.__name__)
#         print('Start')
#
#     @task
#     def browse_product(self):
#         self.client.get('/product/OLJCESPC7Z', name=self.browse_product.__name__)
#         print('Browse Product')
#
#     @task
#     def cart_page(self):
#         self.client.get('/cart', name=self.cart_page.__name__)
#         print('Cart Page')
#
#     def on_stop(self):
#         self.client.get('/', name=self.on_stop.__name__)
#         print('Stop')
#
# class LoadTest(HttpUser):
#     host = 'https://onlineboutique.dev'
#     tasks = [MyTestSequentialTaskSet]
#     wait_time = constant(1)

# Run: locust -f exercises/locust/s1_e10_on_start_and_on_stop_mehods.py -r 1 -u 1 -t 10s --headless --only-summary

class MyTestTaskSet(TaskSet):

    def on_start(self):
        self.client.get('/', name=self.on_start.__name__)
        print('Start')

    @task
    def browse_product_1(self):
        self.client.get('/product/OLJCESPC7Z', name=self.browse_product_1.__name__)
        print('Browse Product 1')

    @task
    def browse_product_2(self):
        self.client.get('/product/9SIQT8TOJO', name=self.browse_product_2.__name__)
        print('Browse Product 2')

    @task
    def cart_page(self):
        self.client.get('/cart', name=self.cart_page.__name__)
        print('Cart Page')

    def on_stop(self):
        self.client.get('/', name=self.on_stop.__name__)
        print('Stop')

class LoadTest(HttpUser):
    host = 'https://onlineboutique.dev'
    tasks = [MyTestTaskSet]
    wait_time = constant(1)

# Run: locust -f exercises/locust/s1_e10_on_start_and_on_stop_mehods.py -r 1 -u 1 -t 10s --headless --only-summary
