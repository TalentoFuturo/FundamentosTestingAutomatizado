# 📘 Clasificador de Notas Académicas

## 🎯 Objetivo

Crear un programa en Python llamado `notas.py` que clasifique una **nota académica** según su valor numérico. La nota debe estar entre **1.0 y 7.0**. Si el valor es inválido (fuera de rango o no numérico), debe lanzar un error y capturarlo con Sentry.

---

## 🧠 Reglas de clasificación

| Nota             | Clasificación                  |
|------------------|-------------------------------|
| menor a 4.0      | "Reprobado"                    |
| 4.0 a 5.4        | "Suficiente"                   |
| 5.5 a 6.4        | "Bueno"                        |
| 6.5 o más        | "Excelente"                    |

---

## ✅ Requisitos funcionales

1. La función principal se llamará: `clasificar_nota(nota)`
2. Si la nota es inválida, debe lanzar una excepción y capturarla con Sentry.
3. Debe registrar cada clasificación (o error) en un archivo de log `notas.log`
4. El programa debe poder ejecutarse desde la línea de comandos:

```bash
python notas.py 5.8
# Resultado: Nota 5.8 -> Bueno
```

---

## 🧪 Requisitos técnicos

1. Crear un entorno virtual dentro de la carpeta `clasificador_notas/`.
2. Archivo `notas.py` con la función y lógica.
3. Archivo `test_notas.py` con al menos **5 pruebas unitarias** usando `unittest`.
4. Uso de `logging` para guardar logs en `notas.log`.
5. Integración con **Sentry**, leyendo el DSN desde `.env` con `python-dotenv`.

---

## 📝 Archivos esperados

```
clasificador_notas/
├── notas.py
├── test_notas.py
├── .env.example
├── notas.log          # generado automáticamente
├── requirements.txt   # sentry-sdk, python-dotenv
```

---

## 💡 Bonus (opcional)

- Agrega un mensaje de bienvenida si no se pasa ningún argumento.
- Permite ejecutar en modo interactivo si no se pasa nota por línea de comandos.

---

**Autor:** osrehe – TalentoFuturo
