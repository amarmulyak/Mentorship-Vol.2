"""
locust -h -> list all available commands

locust -f exercises/locust/s1_e8_run_time_options.py -u 1 -r 1 -t 10s --headless --print-stats --csv ThisRun.csv
--csv-full-history --host=https://example.com

-u 1 -> number of user you are going to spin up
-r 1 -> spawn rate
-t 10s -> duration time (h - hour, m - minute, s - seconds)
--headless -> you don't get the locust web UI, everything gets printed in the terminal
--print-stats -> print all statistics in the terminal
--csv ThisRun.csv -> storing statistics into the csv file
--csv-full-history -> full history (can be used with --csv command only)
--host=https//example.com -> home page

"""

from locust import HttpUser, task, constant


class MyLoadTest(HttpUser):
    wait_time = constant(1)

    @task
    def launch(self):
        self.client.get('/')
