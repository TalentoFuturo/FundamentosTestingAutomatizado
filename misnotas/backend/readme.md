## Backend – Notas CRUD (Flask)
---

### 1. Clonar y entrar

```bash
git clone <este-repositorio>.git
cd notas/backend
```

> El backend vive en `misnotas/backend/`.  
> El front está aparte en `misnotas/frontend/` y no es necesario para probar la API.

---

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv          # una sola vez
# Windows
./env/Scripts/ctivate
# macOS / Linux
source venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

`requirements.txt` trae:

* **Flask** – web micro-framework  
* **Flask-CORS** – para que React pueda llamar a la API  
* **pytest** y **pytest-cov** – tests + cobertura (opcional)

---

### 4. Arrancar el servidor

```bash
python app.py
```

* La API queda en `http://localhost:5000/`.
* Todo el estado (notas) se guarda en memoria, así que cada reinicio empieza limpio.

---

### 5. Endpoints rápidos

| Método | Ruta                    | Descripción                                           |
|--------|-------------------------|-------------------------------------------------------|
| GET    | `/api/notes`           | Lista todas las notas                                 |
| POST   | `/api/notes`           | Crea nota – body JSON con `title`, `body`, `priority` |
| GET    | `/api/notes/<id>`      | Devuelve una nota                                     |
| PUT    | `/api/notes/<id>`      | Actualiza una nota                                    |
| DELETE | `/api/notes/<id>`      | Borra una nota                                        |

Ejemplo de **POST**:

```bash
curl -X POST http://localhost:5000/api/notes      -H "Content-Type: application/json"      -d '{"title":"Comprar café", "body":"250 g arábica","priority":"high"}'
```

---

### 6. Tests (opcional pero recomendado)

- **⚠️[Estrategia de pruebas](https://github.com/TalentoFuturo/FundamentosTestingAutomatizado/tree/main/misnotas/backend/tests)**

```bash
pytest -v                           # corre todo ($ python -m pytest -v)
pytest --cov=app --cov-report term  # con cobertura
```
Posible salida:
```
(venv) λ python -m pytest -v

======== test session starts ========
platform 
cachedir: .pytest_cache
rootdir: 
plugins: cov-6.2.1
collected 11 items

tests/test_notes.py::test_create_each_priority PASSED                                                [  9%]
tests/test_notes.py::test_create_missing_fields[title-invalid_json0] PASSED                          [ 18%]
tests/test_notes.py::test_create_missing_fields[body-invalid_json1] PASSED                           [ 27%]
tests/test_notes.py::test_create_missing_fields[priority-invalid_json2] PASSED                       [ 36%]
tests/test_notes.py::test_create_invalid_priority PASSED                                             [ 45%]
tests/test_notes.py::test_get_single_note PASSED                                                     [ 54%]
tests/test_notes.py::test_get_not_found PASSED                                                       [ 63%]
tests/test_notes.py::test_update_note PASSED                                                         [ 72%]
tests/test_notes.py::test_update_not_found PASSED                                                    [ 81%]
tests/test_notes.py::test_delete_note PASSED                                                         [ 90%]
tests/test_notes.py::test_delete_not_found PASSED                                                    [100%]
```
