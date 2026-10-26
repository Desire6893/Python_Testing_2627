from locust import HttpUser, between, task


class SecretaireUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task(3)
    def voir_competitions(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task(2)
    def voir_tableau_points(self):
        self.client.get("/pointsBoard")

    @task(1)
    def reserver_une_place(self):
        self.client.post("/purchasePlaces", data={
            "club": "Simply Lift",
            "competition": "Summer Cup",
            "places": "1",
        })