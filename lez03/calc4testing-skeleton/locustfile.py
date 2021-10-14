import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        pass

    @task(3)
    def view_item(self):
        pass
