import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/simple-json")
        self.client.get("/sqlite-json")
        self.client.get("/paused-json")
