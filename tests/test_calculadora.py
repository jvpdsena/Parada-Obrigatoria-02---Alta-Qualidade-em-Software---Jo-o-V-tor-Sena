import math
import unittest
from unittest.mock import patch
from io import StringIO
import Calculadora as c


class TestCalculadora(unittest.TestCase):
    def test_adicao(self):
        self.assertEqual(c.adicao(2, 3), 5)

    def test_adicao_negativos(self):
        self.assertEqual(c.adicao(-2, -3), -5)

    def test_subtracao(self):
        self.assertEqual(c.subtracao(8, 3), 5)

    def test_multiplicacao(self):
        self.assertEqual(c.multiplicacao(4, 5), 20)

    def test_divisao(self):
        self.assertEqual(c.divisao(10, 2), 5)

    def test_divisao_zero(self):
        with self.assertRaises(ValueError):
            c.divisao(10, 0)

    def test_potencia(self):
        self.assertEqual(c.potencia(2, 3), 8)

    def test_raiz(self):
        self.assertEqual(c.raiz_quadrada(9), 3)

    def test_raiz_negativa(self):
        with self.assertRaises(ValueError):
            c.raiz_quadrada(-1)

    def test_fatorial_zero(self):
        self.assertEqual(c.fatorial(0), 1)

    def test_fatorial_cinco(self):
        self.assertEqual(c.fatorial(5), 120)

    def test_fatorial_negativo(self):
        with self.assertRaises(ValueError):
            c.fatorial(-1)

    def test_ln(self):
        self.assertAlmostEqual(c.logaritmo_natural(math.e), 1)

    def test_ln_invalido(self):
        with self.assertRaises(ValueError):
            c.logaritmo_natural(0)

    def test_log10(self):
        self.assertAlmostEqual(c.logaritmo_base10(100), 2)

    def test_log10_zero(self):
        with self.assertRaises(ValueError):
            c.logaritmo_base10(0)

    def test_seno(self):
        self.assertAlmostEqual(c.seno(90), 1)

    def test_cosseno(self):
        self.assertAlmostEqual(c.cosseno(180), -1)

    def test_tangente(self):
        self.assertAlmostEqual(c.tangente(45), 1)

    def test_tangente_indefinida(self):
        with self.assertRaises(ValueError):
            c.tangente(90)

    def test_menu_seno(self):
        with patch('builtins.input', side_effect=['10', '90', 'n']), patch('sys.stdout', new_callable=StringIO) as saida:
            c.calculadora_cientifica()
        self.assertIn('Resultado: 1.0', saida.getvalue())

    def test_menu_sair(self):
        with patch('builtins.input', side_effect=['0']), patch('sys.stdout', new_callable=StringIO) as saida:
            c.calculadora_cientifica()
        self.assertIn('Calculadora encerrada.', saida.getvalue())


if __name__ == '__main__':
    unittest.main()
