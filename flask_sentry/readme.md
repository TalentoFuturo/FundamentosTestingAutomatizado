# 🌐 Flask + Sentry – Captura de Errores

Este ejemplo demuestra cómo integrar Sentry en una aplicación **Flask** básica para capturar automáticamente errores de ejecución y enviarlos a la plataforma de monitoreo.

---

## 🚀 Funcionalidad

La aplicación incluye dos rutas:

- `/` → responde con “Hola Mundo Talento Futuro”.
- `/error` → genera un error (división por cero), que es capturado y enviado a Sentry.

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio y acceder a la carpeta

```bash
git clone https://github.com/<tu_usuario>/talentofuturo-ejemplos.git
cd talentofuturo-ejemplos/flask_sentry
```

### 2. Crear un entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Crear el archivo .env
Crea un archivo .env con tu DSN de Sentry:
```bash
SENTRY_DSN=https://<tu_dsn>@sentry.io/<tu_project_id>
APP_ENV=produccion
```
Para lograr lo anterior debes tener previamente creada tu cuenta en [Sentry.io](https://sentry.io/)

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

## ▶️ Ejecutar la aplicación Flask
```bash
python tf_flask.py
```
La aplicación estará disponible en: http://localhost:5000

## 🧪 Probar la integración con Sentry
- Abre tu navegador y visita http://localhost:5000/error
- Se producirá una excepción intencional (ZeroDivisionError).
- Verifica en tu cuenta de Sentry.io que el error fue capturado y registrado correctamente.

# 📚 Aplicaciones

### 🔍 ¿Qué es [Sentry](https://sentry.io/)?

Sentry es una plataforma que permite monitorear errores y excepciones en aplicaciones de software en tiempo real. Proporciona información detallada sobre los fallos, incluyendo:

- Pila de errores (stack trace)
- Variables locales en el momento del error
- Información del entorno (sistema operativo, navegador, etc.)
- Frecuencia de ocurrencia y usuarios afectados

👉 Es ampliamente usado en desarrollo web, móvil, backend y microservicios, ayudando a detectar y resolver errores rápidamente.

---

### 🔍 ¿Qué es [Flask](https://flask.palletsprojects.com/)?

Flask es un framework minimalista y flexible para crear aplicaciones web con Python. Se utiliza para desarrollar APIs, aplicaciones web simples o complejas, y prototipos rápidos.

Características principales:

- Ligero y extensible.
- Fácil de usar y entender.
- Compatible con herramientas modernas como Sentry, SQLAlchemy, Jinja2 y más.

👉 Flask es ideal para aprender desarrollo web en Python y construir aplicaciones escalables de forma incremental.

---







