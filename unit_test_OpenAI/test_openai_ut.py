from dotenv import load_dotenv
import os
import ast
from openai import OpenAI  # SDK v1+

# --------------------------------------------------
# Configuración básica
# --------------------------------------------------
load_dotenv()
API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=API_KEY)  # nuevo cliente

color_prefix_by_role = {
    "system": "\033[35m",
    "user": "\033[34m",
    "assistant": "\033[92m",
}

def print_messages(messages, color_prefix_by_role=color_prefix_by_role) -> None:
    for message in messages:
        role = message["role"]
        print(f"{color_prefix_by_role[role]}\n[{role}]\n{message['content']}")

def print_message_delta(delta, color_prefix_by_role=color_prefix_by_role) -> None:
    # Sigue funcionando con la misma firma, por compatibilidad con print_text=True
    print(delta, end="")

# --------------------------------------------------
# Función principal
# --------------------------------------------------
def unit_tests_from_function(
    function_to_test: str,
    unit_test_package: str = "pytest",
    approx_min_cases_to_cover: int = 7,
    print_text: bool = False,
    explain_model: str = "gpt-4o-2024-08-06",
    plan_model: str = "gpt-4o-2024-08-06",
    execute_model: str = "gpt-4o-2024-08-06",
    temperature: float = 0.4,
    reruns_if_fail: int = 1,
) -> str:
    # ---------- Paso 1: Explicación ----------
    explain_system_message = {
        "role": "system",
        "content": "Eres desarrollador de Python de clase mundial con un ojo de águila para errores no deseados y casos extremos. Explica cuidadosamente el código con gran detalle y precisión. Organiza tus explicaciones en listas con viñetas con formato markdown.",
    }
    explain_user_message = {
        "role": "user",
        "content": f"""Explica la siguiente función de Python. Revisa qué está haciendo cada elemento de la función con precisión y cuáles pueden haber sido las intenciones del autor. Organiza tu explicación como una lista con viñetas con formato markdown.

```python
{function_to_test}
```""",
    }
    explain_messages = [explain_system_message, explain_user_message]

    if print_text:
        print_messages(explain_messages)

    completion = client.beta.chat.completions.parse(
        model=explain_model,
        messages=explain_messages,
        temperature=temperature,
    )
    explanation = completion.choices[0].message.content
    if print_text:
        print_message_delta(explanation)

    explain_assistant_message = {"role": "assistant", "content": explanation}

    # ---------- Paso 2: Plan ----------
    plan_user_message = {
        "role": "user",
        "content": f"""Un buen conjunto de pruebas debe apuntar a:

- Probar el comportamiento de la función para una amplia gama de entradas posibles
- Probar casos extremos que el autor puede no haber previsto
- Aprovechar las características o `{unit_test_package}` para que las pruebas sean fáciles de escribir y mantener
- Ser fácil de leer y comprender, con código limpio y nombres descriptivos
- Ser determinista, de modo que las pruebas siempre pasen o fallen de la misma manera

Para ayudar a probar la unidad de la función anterior, enumere diversos escenarios que la función debería poder manejar (y debajo de cada escenario, incluya algunos ejemplos como subviñetas).""",
    }
    plan_messages = [
        explain_system_message,
        explain_user_message,
        explain_assistant_message,
        plan_user_message,
    ]

    if print_text:
        print_messages([plan_user_message])

    completion = client.beta.chat.completions.parse(
        model=plan_model,
        messages=plan_messages,
        temperature=temperature,
    )
    plan = completion.choices[0].message.content
    if print_text:
        print_message_delta(plan)

    plan_assistant_message = {"role": "assistant", "content": plan}

    # ---------- Paso 2b: Elaboración opcional ----------
    num_bullets = max(plan.count("\n-"), plan.count("\n*"))
    elaboration_needed = num_bullets < approx_min_cases_to_cover

    if elaboration_needed:
        elaboration_user_message = {
            "role": "user",
            "content": "Además de los escenarios anteriores, enumera algunos casos extremos raros o inesperados (y como antes, debajo de cada caso extremo, incluye algunos ejemplos como subviñetas).",
        }
        elaboration_messages = (
            plan_messages + [plan_assistant_message, elaboration_user_message]
        )

        if print_text:
            print_messages([elaboration_user_message])

        completion = client.beta.chat.completions.parse(
            model=plan_model,
            messages=elaboration_messages,
            temperature=temperature,
        )
        elaboration = completion.choices[0].message.content
        if print_text:
            print_message_delta(elaboration)

        elaboration_assistant_message = {"role": "assistant", "content": elaboration}

    # ---------- Paso 3: Generar pruebas ----------
    package_comment = ""
    if unit_test_package == "pytest":
        package_comment = "# a continuación, cada caso de prueba está representado por una tupla pasada al decorador @pytest.mark.parametrize"

    execute_system_message = {
        "role": "system",
        "content": "Eres un desarrollador de Python de clase mundial con un ojo de águila para errores no deseados y casos extremos. Escribe pruebas unitarias cuidadosas y precisas. Cuando se te pide que respondas solo con código, escribe todo su código en un solo bloque.",
    }
    execute_user_message = {
        "role": "user",
        "content": f"""Usando Python y el paquete `{unit_test_package}`, escribe un conjunto de pruebas unitarias para la función, siguiendo los casos anteriores. Incluye comentarios útiles para explicar cada línea. Responde solo con código, formateado de la siguiente manera:
```python
# imports
import {unit_test_package}  # utilizado para nuestras pruebas unitarias
{{inserta otras importaciones según sea necesario}}

# función para probar
{function_to_test}

# unit tests
{package_comment}
{{inserta el código de prueba de la unidad aquí}}
```""",
    }
    execute_messages = [
        execute_system_message,
        explain_user_message,
        explain_assistant_message,
        plan_user_message,
        plan_assistant_message,
    ]
    if elaboration_needed:
        execute_messages += [elaboration_user_message, elaboration_assistant_message]
    execute_messages.append(execute_user_message)

    if print_text:
        print_messages([execute_system_message, execute_user_message])

    completion = client.beta.chat.completions.parse(
        model=execute_model,
        messages=execute_messages,
        temperature=temperature,
    )
    execution = completion.choices[0].message.content
    if print_text:
        print_message_delta(execution)

    # ---------- Validación de sintaxis ----------
    try:
        code = execution.split("```python")[1].split("```")[0].strip()
        ast.parse(code)
    except (IndexError, SyntaxError) as e:
        print(f"Error de sintaxis en el código generado: {e}")
        if reruns_if_fail > 0:
            print("Reintentando...")
            return unit_tests_from_function(
                function_to_test=function_to_test,
                unit_test_package=unit_test_package,
                approx_min_cases_to_cover=approx_min_cases_to_cover,
                print_text=print_text,
                explain_model=explain_model,
                plan_model=plan_model,
                execute_model=execute_model,
                temperature=temperature,
                reruns_if_fail=reruns_if_fail - 1,
            )
    return code

# --------------------------------------------------
# Ejemplo rápido
# --------------------------------------------------
example_function = """def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]
"""

unit_tests = unit_tests_from_function(
    example_function,
    approx_min_cases_to_cover=10,
    print_text=True,
)
print("\n\nCódigo de pruebas unitarias generado:\n")
print(unit_tests)
