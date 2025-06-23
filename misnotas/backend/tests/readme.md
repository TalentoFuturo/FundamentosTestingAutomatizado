# Panorama general de la suite de pruebas

En esta suite estamos verificando todo el ciclo de vida de la API REST `/api/notes`:

| CRUD   | Casos cubiertos                                                   | Éxitos / Errores |
|--------|-------------------------------------------------------------------|------------------|
| Create | 3 prioridades válidas / campos faltantes / prioridad inválida     | **5** | |
| Read   | Obtener 1 nota / “no existe”                                      | **2** | |
| Update | Editar OK / editar ID inexistente                                 | **2** | |
| Delete | Borrar OK / borrar ID inexistente                                 | **2** | |

Total: **11** pruebas atómicas que se ejecutan en un backend “fresco” gracias a los *fixtures*.

- No se consideran variaciones del largo de textos por ejemplo

---

## 1 . Fixtures y aislamiento

### `_reset_state` — fixture autouse
```python
@pytest.fixture(autouse=True)
def _reset_state():
    notes.clear()              # limpia la “base” en memoria
    app_module.next_id = 1     # reinicia el autoincremental
    yield                      # ← aquí corre cada test
    notes.clear()              # limpieza "proactiva" post-test
```
`autouse=True` ⇒ se aplica antes y después de cada test, sin declararlo explícitamente.

Garantiza que ningún caso contamine al siguiente: cada prueba arranca con `[]` y `id = 1`.

### `client` — fixture explícito
```python
@pytest.fixture
def client():
    app.config.update(TESTING=True)
    return app.test_client()
```
Crea el **Flask test client** para lanzar peticiones HTTP internas sin levantar un servidor real.

---

## 2 . Datos de entrada

* **`VALID_NOTES`** contiene los tres payloads “felices” (Camino feliz) (Alta, Media, Baja).  
* **`INVALID_PRIORITY`** payload con prioridad inesperada.

Ventaja: los tests no escriben literales redundantes; un cambio (por ejemplo renombrar “Alta”→“High”) se hace en un solo sitio.

---

## 3 . Caso a caso

| Test | Qué hace | Puntos de verificación |
|------|----------|------------------------|
| `test_create_each_priority` | POST de las 3 notas válidas en un loop. | • 201 Created • id consecutivo esperado • priority devuelta coincide con enviada • al final la lista tiene 3 elementos |
| `test_create_missing_fields` *(parametrizado)* | Repite el POST omitiendo *title*, *body* o *priority*. | • 201 (la API actual no valida) • campo ausente llega como cadena vacía |
| `test_create_invalid_priority` | Envía prioridad “Urgente”. | • 201 • se guarda tal cuál  |
| `test_get_single_note` | Crea 1 nota y hace GET `/api/notes/1`. | • 200 • título correcto |
| `test_get_not_found` | GET `/api/notes/999`. | • 404 • mensaje JSON “Nota no encontrada” |
| `test_update_note` | Crea nota, luego PUT cambia título + prioridad. | • 200 • campos realmente modificados |
| `test_update_not_found` | PUT sobre id 123 inexistente. | • 404 |
| `test_delete_note` | Crea, luego DELETE id 1. | • 204 • GET lista vuelve vacía |
| `test_delete_not_found` | DELETE id 321 inexistente. | • 404 |

---

## 4 . Flujo de ejecución real (ejemplo)

1. Pytest detecta archivos, crea *client* y aplica `_reset_state`.  
2. Corre `test_create_each_priority` — internamente genera ids 1‑3.  
3. Sale del test → `_reset_state` limpia todo (`notes=[]`, `next_id=1`).  
4. Entra al siguiente test (p.ej. `test_get_single_note`) y repite el ciclo.

Esto asegura reproducibilidad: puedes ejecutar los tests en cualquier orden o paralelizarlos y seguirán pasando.

---

## 5 . Cobertura de *error-paths*

* Validamos **404** para `GET` / `PUT` / `DELETE` con IDs inexistentes.  
* Verificamos comportamiento con campos faltantes y prioridad inesperada (la app hoy acepta cualquier string → el test refleja la realidad; si mañana añades validación, estos casos se actualizarán para esperar un **400**).

---

##6 Ejecución
Pruebas exhaustivas para backend/app.py (CRUD de notas)
Ejecutar desde la carpeta Backend:
- ```$ pytest -v```

En caso de funcionar probar con:
- ```$ python -m pytest -v```

---
