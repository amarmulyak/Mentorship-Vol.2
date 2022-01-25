"""
locust -h -> list all available commands

locust -f exercises/locust/s1_e9_run_time_options_p2.py -u 1 -r 1 -t 10s --headless --print-stats
--host=https://example.com -L CRITICAL --logfile mylog.log --html Run1

-L CRITICAL-> log the information (DEBUG/INFO/WARNING/ERROR/CRITICAL, INFO - default)
--logfile mylog.log -> store all the information into the log file
--html ThisRun -> generate the HTML Report

locust -f exercises/locust/s1_e9_run_time_options_p2.py -l
-l -> list all the User classes in the locust script

locust -f exercises/locust/s1_e9_run_time_options_p2.py --show-task-ratio
--show-task-ratio -> print the task execution ratio
"""

from locust import HttpUser, task, constant, TaskSet


class FirefoxBrowserTest(TaskSet):

    @task
    def launch(self):
        print('Firefox Browser Tests')
        self.client.get('/', name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class ChromeBrowserTest(TaskSet):

    @task
    def launch(self):
        print('Chrome Browser Tests')
        self.client.get('/', name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class EdgeBrowserTest(TaskSet):

    @task
    def launch(self):
        print('Edge Browser Tests')
        self.client.get('/', name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):

    wait_time = constant(1)
    tasks = [ChromeBrowserTest, FirefoxBrowserTest, EdgeBrowserTest]


# Run: locust -f exercises/locust/s1_e9_run_time_options_p2.py -u 1 -r 1 -t 10s --headless --print-stats --host=https://example.com -L DEBUG --logfile mylog.log --html Run1
# Run: locust -f exercises/locust/s1_e9_run_time_options_p2.py -l
# Run: locust -f exercises/locust/s1_e9_run_time_options_p2.py --show-task-ratio
# Run: locust -f exercises/locust/s1_e9_run_time_options_p2.py --show-task-ratio-json
