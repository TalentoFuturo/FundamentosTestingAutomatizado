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

```bash
pytest -q                           # corre todo
pytest --cov=app --cov-report term  # con cobertura
```
