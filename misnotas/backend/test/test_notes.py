import pytest
import os
import sys 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, notes, next_id   # importa tu app Flask y la “BD” in-memory

@pytest.fixture(autouse=True)
def _reset_state():
    """
    Antes de cada test deja la lista 'notes' vacía
    y reinicia next_id a 1.
    """
    notes.clear()
    global next_id
    next_id = 1
    yield                       # ejecuta el test
    notes.clear()

@pytest.fixture
def client():
    app.config.update(TESTING=True)
    return app.test_client()

def test_empty_list(client):
    rv = client.get("/api/notes")
    assert rv.status_code == 200
    assert rv.get_json() == []

def test_create_note(client):
    payload = {"title": "Pytest", "body": "Demo", "priority": "high"}
    rv = client.post("/api/notes", json=payload)
    assert rv.status_code == 201
    data = rv.get_json()
    assert data["id"] == 1
    assert data["title"] == "Pytest"
    assert data["priority"] == "high"

    # la lista ahora tiene 1 nota
    rv_all = client.get("/api/notes")
    assert len(rv_all.get_json()) == 1

def test_get_single_note(client):
    client.post("/api/notes", json={"title": "One"})
    rv = client.get("/api/notes/1")
    assert rv.status_code == 200
    assert rv.get_json()["title"] == "One"

def test_update_note(client):
    client.post("/api/notes", json={"title": "Old"})
    rv = client.put("/api/notes/1", json={"title": "New"})
    assert rv.status_code == 200
    assert rv.get_json()["title"] == "New"

def test_delete_note(client):
    client.post("/api/notes", json={"title": "Temp"})
    rv_del = client.delete("/api/notes/1")
    assert rv_del.status_code == 204

    rv = client.get("/api/notes")
    assert rv.get_json() == []

def test_not_found(client):
    rv = client.get("/api/notes/999")
    assert rv.status_code == 404
    assert rv.get_json()["error"] == "Nota no encontrada"
