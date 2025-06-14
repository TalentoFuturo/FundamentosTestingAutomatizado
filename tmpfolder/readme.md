# 🔺 Clasificación de Triángulos

Este ejemplo presenta un programa en Python que clasifica un triángulo según la longitud de sus lados (`a`, `b`, `c`) en una de las siguientes categorías:

- Triángulo equilátero
- Triángulo isósceles
- Triángulo rectángulo
- Triángulo acutángulo
- Triángulo escaleno
- No es un triángulo válido

Incluye pruebas unitarias automatizadas con `unittest`, generación de logs y soporte para ejecución desde la línea de comandos.

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio y acceder a la carpeta

```bash
git clone https://github.com/<tu_usuario>/talentofuturo-ejemplos.git
cd talentofuturo-ejemplos/triangulo
```

### 2. Crear un entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

## 🚀 Ejecutar programa
Desde la línea de comandos:
```bash
python triangulo.py 3 4 5
```
Esto imprimirá la clasificación 
```bash
Resultado: Triángulo rectángulo (cumple con el teorema de Pitágoras)
```
... y generará un log en el archivo triangulo.log.

## 🧪 Ejecutar pruebas unitarias
Para correr las pruebas:
```bash
python test_triangulo.py
```

Deberías ver una salida indicando que todas las pruebas pasaron, por ejemplo:
```bash
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK

```
Resultados en logs:
```bash
2025-06-13 14:26:43,813 - DEBUG - Entradas – a: 3.0, b: 3.0, c: 3.0
2025-06-13 14:26:43,813 - INFO - Triángulo equilátero
2025-06-13 14:33:19,867 - DEBUG - Entradas – a: 3.0, b: 4.0, c: 5.0
2025-06-13 14:33:19,867 - INFO - Triángulo rectángulo
2025-06-14 09:37:01,758 - DEBUG - Entradas – a: 3.0, b: 4.0, c: 5.0
2025-06-14 09:37:01,758 - INFO - Triángulo rectángulo
2025-06-14 09:37:11,911 - DEBUG - Entradas – a: 4, b: 5, c: 6
2025-06-14 09:37:11,911 - INFO - Triángulo acutángulo
2025-06-14 09:37:11,914 - DEBUG - Entradas – a: 3, b: 3, c: 3
2025-06-14 09:37:11,914 - INFO - Triángulo equilátero
2025-06-14 09:37:11,915 - DEBUG - Entradas – a: 2, b: 3, c: 4
2025-06-14 09:37:11,915 - INFO - Triángulo escaleno
2025-06-14 09:37:11,916 - DEBUG - Entradas – a: 1, b: 2, c: 3
2025-06-14 09:37:11,916 - ERROR - No es un triángulo válido
2025-06-14 09:37:11,916 - DEBUG - Entradas – a: 5, b: 5, c: 3
2025-06-14 09:37:11,916 - INFO - Triángulo isósceles
2025-06-14 09:37:11,917 - DEBUG - Entradas – a: 3, b: 4, c: 5
2025-06-14 09:37:11,917 - INFO - Triángulo rectángulo

```
