"""Demonstra a etapa RED contra o código original sem alterá-lo."""
import importlib.util
from unittest.mock import patch

with patch('builtins.input', return_value='0'):
    spec = importlib.util.spec_from_file_location('original', 'Calculadora_original.py')
    original = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(original)

assert original.adicao(2, 3) == 5, f'Esperado 5, obtido {original.adicao(2, 3)}'
