# test_triangulo.py

import unittest
from triangulo import classify_triangle

class TestClassifyTriangle(unittest.TestCase):

    def test_equilatero(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Triángulo equilátero (todos los lados son iguales)")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Triángulo isósceles (dos lados son iguales)")

    def test_rectangulo(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Triángulo rectángulo (cumple con el teorema de Pitágoras)")

    def test_acutangulo(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Triángulo acutángulo (todos los ángulos son agudos)")

    def test_escaleno(self):
        self.assertEqual(classify_triangle(2, 3, 4), "Triángulo escaleno (todos los lados son diferentes)")

    def test_invalido(self):
        self.assertEqual(classify_triangle(1, 2, 3), "No es un triángulo válido")

if __name__ == '__main__':
    unittest.main()
