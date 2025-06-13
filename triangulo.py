# triangulo.py

import logging
import sys
    
logging.basicConfig(
    filename="triangulo.log",
    filemode="a", #acumula logs
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def classify_triangle(a, b, c):
    logging.debug(f"Entradas – a: {a}, b: {b}, c: {c}")
    if not (a + b > c and a + c > b and b + c > a):
        logging.error("No es un triángulo válido")
        return "No es un triángulo válido"

    if a == b == c:
        logging.info("Triángulo equilátero")
        return "Triángulo equilátero (todos los lados son iguales)"
    elif a == b or a == c or b == c:
        logging.info("Triángulo isósceles")
        return "Triángulo isósceles (dos lados son iguales)"
    elif a**2 + b**2 == c**2:
        logging.info("Triángulo rectángulo")
        return "Triángulo rectángulo (cumple con el teorema de Pitágoras)"
    else:
        if a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
            logging.info("Triángulo acutángulo")
            return "Triángulo acutángulo (todos los ángulos son agudos)"
        else:
            logging.info("Triángulo escaleno")
            return "Triángulo escaleno (todos los lados son diferentes)"


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python triangulo.py <lado_a> <lado_b> <lado_c>")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        resultado = classify_triangle(a, b, c)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: los argumentos deben ser números.")
        sys.exit(1)
