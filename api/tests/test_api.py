import sys
import os

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ✅ Override database for testing BEFORE importing app
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from fastapi.testclient import TestClient
from src.main import app
from src.models import Base
from src.config import engine

# create tables for sqlite test DB
Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_item():
    payload = {
        "name": "pytest-item",
        "description": "testing"
    }

    response = client.post("/items", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == payload["name"]
    assert data["description"] == payload["description"]
    assert "id" in data
    assert "created_at" in data


def test_get_items():
    response = client.get("/items")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
