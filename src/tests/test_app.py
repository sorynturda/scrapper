import os
from main import app
from scrap.scraper import get_info
from fastapi.testclient import TestClient
from http import HTTPStatus

client = TestClient(app)


def test_root():
    """
    simple endpoint check
    """
    response = client.get("/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"


def test_post_link_valid():
    """
    test for '/link' endpoint. a valid link is provided
    """
    path = "cluj"
    response = client.post("/link", json={"path": path})
    assert response.status_code == 200
    assert response.json()["saved"] == True
    if os.path.exists("wiki/" + path + ".dat"):
        os.remove("wiki/" + path + ".dat")
    if os.path.exists("wiki/" + path + ".txt"):
        os.remove("wiki/" + path + ".txt")


def test_post_link_invalid():
    """
    test for '/link' endpoint. an invalid link is provided
    """
    path = "inexistent_link dagsdfgdhfgdh"
    response = client.post("/link", json={"path": path})
    assert response.status_code == 200
    assert response.json()["saved"] == False
    assert response.json()["encrypted"] == False


def test_post_link_not_ecrypted():
    """
    test for '/link' endpoint and check if the file is not encrypted
    provided path: categorie:romani, saved as plain text
    """

    path = "categorie:romani"
    text, date = get_info(path)[0:2]
    encrypted = True if date % 2 == 0 else False
    response = client.post("/link", json={"path": path})
    assert response.status_code == 200
    assert response.json()['encrypted'] == encrypted
    assert os.path.exists("wiki/" + path + ".dat") ==  False
    assert os.path.exists("wiki/" + path + ".txt") ==  True

    with open("wiki/" + path + ".txt", 'r') as f:
        content = f.read()
    assert text == content
    if os.path.exists("wiki/" + path + ".txt"):
        os.remove("wiki/" + path + ".txt")
    
def test_post_link_not_ecrypted():
    """
    test for '/link' endpoint and check if the file is not encrypted
    provided path: categorie:romani, saved as plain text
    """

    path = "categorie:romani"
    text, date = get_info(path)[0:2]
    encrypted = True if date % 2 == 0 else False
    response = client.post("/link", json={"path": path})
    assert response.status_code == 200
    assert response.json()['encrypted'] == encrypted
    assert os.path.exists("wiki/" + path + ".dat") ==  False
    assert os.path.exists("wiki/" + path + ".txt") ==  True

    with open("wiki/" + path + ".txt", 'r') as f:
        content = f.read()
    assert text == content
    if os.path.exists("wiki/" + path + ".txt"):
        os.remove("wiki/" + path + ".txt")
def test_post_link_not_ecrypted():
    """
    test for '/link' endpoint and check if the file is not encrypted
    provided path: categorie:romani, saved as plain text
    """

    path = "categorie:romani"
    text, date = get_info(path)[0:2]
    encrypted = True if date % 2 == 0 else False
    response = client.post("/link", json={"path": path})
    assert response.status_code == 200
    assert response.json()['encrypted'] == encrypted
    assert os.path.exists("wiki/" + path + ".dat") ==  False
    assert os.path.exists("wiki/" + path + ".txt") ==  True

    with open("wiki/" + path + ".txt", 'r') as f:
        content = f.read()
    assert text == content
    if os.path.exists("wiki/" + path + ".txt"):
        os.remove("wiki/" + path + ".txt")
    
def test_post_link_not_ecrypted():
    """
    test for '/link' endpoint and check if the file is not encrypted
    provided path: categorie:romani, saved as plain text
    """

    path = "categorie:romani"
    text, date = get_info(path)[0:2]
    encrypted = False
    response = client.post("/link", json={"path": path})
    assert response.status_code == 200
    assert response.json()['encrypted'] == encrypted
    assert os.path.exists("wiki/" + path + ".dat") ==  False
    assert os.path.exists("wiki/" + path + ".txt") ==  True

    with open("wiki/" + path + ".txt", 'r') as f:
        content = f.read()
    assert text == content
    if os.path.exists("wiki/" + path + ".txt"):
        os.remove("wiki/" + path + ".txt")
    
def test_post_link_ecrypted():
    """
    test for '/link' endpoint and check if the file is encrypted
    provided path: Wikipedia:Despre_Wikipedia, must be encrypted
    """

    path = "Wikipedia:Despre_Wikipedia"
    text, date = get_info(path)[0:2]
    encrypted = True
    response = client.post("/link", json={"path": path})
    assert response.status_code == 200
    assert response.json()['encrypted'] == encrypted
    assert os.path.exists("wiki/" + path + ".dat") ==  True
    assert os.path.exists("wiki/" + path + ".txt") ==  False

    with open("wiki/" + path + ".dat", 'r') as f:
        content = f.read()
    assert not text == content
    if os.path.exists("wiki/" + path + ".dat"):
        os.remove("wiki/" + path + ".dat")
    

    
