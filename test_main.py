import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_reverse_text_empty():
    response = client.get("/api/reverse?text=")
    assert response.status_code == 200
    assert response.json() == {"reversed": ""}

def test_disemvowel_text_empty():
    response = client.get("/api/disemvowel?text=")
    assert response.status_code == 200
    assert response.json() == {"disemvoweled": ""}
