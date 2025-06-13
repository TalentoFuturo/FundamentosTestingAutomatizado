
# 💻 Ejemplos de Clases – TalentoFuturo

Este repositorio contiene ejemplos prácticos utilizados durante las sesiones del curso **Fundamentos de Testing Automatizado** y otros contenidos complementarios para los estudiantes de TalentoFuturo.

Cada carpeta representa un ejemplo autocontenible, que puede ser ejecutado, probado y extendido de forma independiente.

---

## 📁 Ejemplos disponibles

| Ejemplo                            | Descripción                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| [`triangulo/`](./Triangulo/)      | Programa en Python que clasifica triángulos, incluye pruebas unitarias y logging. |
| [`flask_sentry/`](./flask_sentry/) | Aplicación mínima en Flask con integración a Sentry para captura de errores.     |

> Nuevos ejemplos se irán agregando a medida que avance el curso.

---

## 🧰 Requisitos comunes

Para ejecutar los ejemplos en Python:

```bash
# Recomendado: crear entorno virtual dentro de cada carpeta
cd triangulo/  # o flask_sentry/, etc.
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
pip install -r requirements.txt
