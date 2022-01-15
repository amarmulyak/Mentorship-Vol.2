from locust import User, task, constant


class MyFirstScript(User):
    """
    abstract = True
    on_start(): run something on start of instantiating a class
    on_stop(): same
    tasks: list of tasks
    wait()
    wait_time()
    weight = 10
    """

    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print('Launching the URL')

    @task
    def search(self):
        print('Searching')


# launch in terminal: locust -f ./exercises/locust/s1_e2_class_user.py
# e.g. number: 2, spawn: 1
# it will spawn 1 user per second, total number of users will be 2
# take a look at the PyCharm terminal to see what happens


class MySecondUser(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch2(self):
        print('Second Test')

    @task
    def search2(self):
        print('Searching 2')


# in case of launching, the test will pick up only the first class
# wee need to add parameter 'weight' e.g. = 2 to make run of two classes (weight is a priority ot pick up the task)
# to wait between running the task wee need to add parameter 'wait_time' e.g = constant(1)
# run the test with number: 4 (it will mean the priority will be 50% for each task), spawn: 4
