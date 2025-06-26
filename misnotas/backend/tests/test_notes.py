"""
Pruebas exhaustivas para backend/app.py (CRUD de notas)
Ejecutar desde la carpeta Backend:
$ pytest -v
En caso de funcionar probar con:
$ python -m pytest -v    
"""

import os, sys, pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app as app_module           # ← módulo entero (app.py)
from app import app, notes         # ← instancia Flask + lista


# ---------- FIXTURES -------------------------------------------------

@pytest.fixture(autouse=True)
def _reset_state():
    notes.clear()
    app_module.next_id = 1         # ← ahora sí resetea el contador
    yield
    notes.clear()

@pytest.fixture
def client():
    app.config.update(TESTING=True)
    return app.test_client()

# ---------- DATOS DE ENTRADA ----------------------------------------

VALID_NOTES = [
    {"title": "Nota Alta",  "body": "cuerpo A", "priority": "Alta"},
    {"title": "Nota Media", "body": "cuerpo B", "priority": "Media"},
    {"title": "Nota Baja",  "body": "cuerpo C", "priority": "Baja"},
]

INVALID_PRIORITY = {"title": "Sinprio", "body": "bad", "priority": "Urgente"}  # prioridad inválida

# ---------- TESTS ----------------------------------------------------

def test_create_each_priority(client):
    """Se pueden crear notas con cada prioridad válida."""
    for i, payload in enumerate(VALID_NOTES, start=1):
        rv = client.post("/api/notes", json=payload)
        assert rv.status_code == 201
        data = rv.get_json()
        assert data["id"] == i
        assert data["priority"] == payload["priority"]

    # La lista debe tener 3 elementos
    rv_all = client.get("/api/notes")
    assert len(rv_all.get_json()) == 3


@pytest.mark.parametrize(
    "field, invalid_json",
    [
        ("title",    {"body": "x", "priority": "Alta"}),   # falta título
        ("body",     {"title": "y", "priority": "Baja"}),  # falta cuerpo
        ("priority", {"title": "z", "body": "xx"}),        # falta prioridad
    ],
)
def test_create_missing_fields(client, field, invalid_json):
    """Crear con campos faltantes → priority queda '' o campo vacío según app.py."""
    rv = client.post("/api/notes", json=invalid_json)
    assert rv.status_code == 201             # la API actual no valida: debe devolver 201
    data = rv.get_json()
    # campo faltante queda cadena vacía
    assert data.get(field, "") == ""


def test_create_invalid_priority(client):
    """Prioridad inválida se guarda tal cual (la API no valida)."""
    rv = client.post("/api/notes", json=INVALID_PRIORITY)
    assert rv.status_code == 201
    assert rv.get_json()["priority"] == "Urgente"


def test_get_single_note(client):
    client.post("/api/notes", json=VALID_NOTES[0])
    rv = client.get("/api/notes/1")
    assert rv.status_code == 200
    assert rv.get_json()["title"] == "Nota Alta"


def test_get_not_found(client):
    rv = client.get("/api/notes/999")
    assert rv.status_code == 404
    assert rv.get_json()["error"] == "Nota no encontrada"


def test_update_note(client):
    client.post("/api/notes", json=VALID_NOTES[1])
    rv_put = client.put("/api/notes/1", json={"title": "Actualizada", "priority": "Alta"})
    assert rv_put.status_code == 200
    data = rv_put.get_json()
    assert data["title"] == "Actualizada"
    assert data["priority"] == "Alta"


def test_update_not_found(client):
    rv = client.put("/api/notes/123", json={"title": "X"})
    assert rv.status_code == 404


def test_delete_note(client):
    client.post("/api/notes", json=VALID_NOTES[2])
    rv_del = client.delete("/api/notes/1")
    assert rv_del.status_code == 204

    rv_all = client.get("/api/notes")
    assert rv_all.get_json() == []


def test_delete_not_found(client):
    rv = client.delete("/api/notes/321")
    assert rv.status_code == 404
