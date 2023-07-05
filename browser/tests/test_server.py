from fastapi.testclient import TestClient
from elephant_news.browser.server import app


client = TestClient(app)


def test_hi():
    response = client.get("/hi")
    assert response.status_code == 200
    assert response.json() == {"reply": "hi"}


def test_chat():
    response = client.post("/chat", json={"message": "hello"})
    assert response.status_code == 200
    assert response.json() == {"reply": "Message Received!hello"}


def test_sendpage():
    response = client.post("/sendpage")
    assert response.status_code == 200
    assert response.json() == {"reply": "Analysis Complete!"}
