import requests
import time

def test_status_endpoint():
    # wait for the server to start
    time.sleep(2)

    response = requests.get("http://localhost:8000/status")

    assert response.status_code == 200
    assert response.json()["service"] == "running"