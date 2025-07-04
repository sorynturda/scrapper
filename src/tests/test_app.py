import os
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_post_link():
    path = "cluj"
    response = client.post(
        "/link/",
        json={'path':path}
    )
    assert response.status_code == 200
    if os.path.exists("wiki/" + path + ".dat"):
        os.remove("wiki/" + path + ".dat")
    if os.path.exists("wiki/" + path + ".txt"):
        os.remove("wiki/" + path + ".txt")
    

def test_root():
    response = client.get('/')
    assert response.status_code == 404
