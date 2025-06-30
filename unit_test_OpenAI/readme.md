# Generador de Pruebas Unitarias con OpenAI y Multi-Prompt

Este proyecto demuestra cómo generar automáticamente pruebas unitarias para una función de Python utilizando la API de OpenAI y la técnica de **multi-prompt**. El programa ejecuta un flujo de tres pasos (explicar → planificar → generar código) para producir un archivo de test listo para ejecutarse con *pytest*.

---

## Contenido
1. [Características](#características)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Configuración](#configuración)
5. [Ejemplo de uso](#ejemplo-de-uso)
6. [¿Qué es un multi-prompt?](#qué-es-un-multi-prompt)
7. [Cómo lo aplicamos aquí](#cómo-lo-aplicamos-aquí)
8. [Ejecución de pruebas](#ejecución-de-pruebas)

---

## Características
- Utiliza el SDK **openai ≥ 1.0.0** con el modelo `gpt-4o-2024-08-06`.
- Flujo automático en tres etapas para producir casos de prueba extensos y bien documentados.
- Compatibilidad con cualquier paquete de test (por defecto *pytest*).
- Validación sintáctica del código generado antes de devolverlo.

## Requisitos
- Python 3.9 o superior.
- Cuenta de OpenAI con una **API key** activa.

## Instalación
```bash
# Clonar el repositorio
git clone <URL-del-repo>
cd <directorio>

# Crear y activar un entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Configuración
1. Crea un archivo `.env` en la raíz del proyecto.
2. Añade tu clave de OpenAI:
   ```env
   OPENAI_API_KEY="sk-..."
   ```

## Ejemplo de uso
```python
from generator import unit_tests_from_function

funcion = """def suma(a, b):
    return a + b
"""

codigo_tests = unit_tests_from_function(
    funcion,
    approx_min_cases_to_cover=5,
    print_text=True,
)

print(codigo_tests)
```
El script imprimirá en consola el proceso y devolverá un bloque de código listo para guardarse como `test_suma.py`.

---

## ¿Qué es un multi-prompt?
Un **multi-prompt** es una estrategia de *prompt engineering* que divide un problema complejo en varias consultas secuenciales a un modelo de lenguaje. En lugar de solicitar una respuesta completa en un único mensaje, se envían varios prompts encadenados, cada uno especializado en un sub-paso concreto. Esto mejora la calidad, la coherencia y la capacidad de control sobre la salida.

### Beneficios principales
- **Descomposición**: permite aislar distintos objetivos (explicar, planear, ejecutar).
- **Control fino**: facilita ajustar temperatura o instrucciones según la fase.
- **Reutilización**: los resultados de un paso alimentan al siguiente, creando contexto acumulativo.

## Cómo lo aplicamos aquí
1. **Explicación (Prompt 1)**
   - El sistema solicita una explicación detallada de la función objetivo.
2. **Plan de pruebas (Prompt 2)**
   - Con la explicación en contexto, se pide un plan de escenarios y casos.
   - Si el plan es corto, un prompt adicional amplía casos extremos.
3. **Generación de código (Prompt 3)**
   - Se envía el plan y las instrucciones finales para producir el archivo de test.

Cada respuesta alimenta el siguiente prompt mediante la lista `messages`, construyendo así un **hilo conversacional** donde el modelo mantiene el contexto completo.

---

## Ejecución de pruebas
1. Guarda el bloque de código generado como `test_<nombre>.py` dentro de tu proyecto.
2. Ejecuta:
   ```bash
   pytest -v
   ```
3. Revisa los resultados en consola. El script generador ya valida la sintaxis, pero *pytest* confirmará la correcta ejecución lógica.

---

## Código base e idea Original
Código fuente base e idea original basada OpenAI ejemplo de concina: 
- [Unit test writing using a multi-step prompt](https://github.com/openai/openai-cookbook/blob/main/examples/Unit_test_writing_using_a_multi-step_prompt.ipynb)

---

