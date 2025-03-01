# -*- coding: utf-8 -*-
from proof_by_induction import prove_arithmetic_series_formula

# Define los casos de prueba
test_cases = [
    {
        'description': 'Suma de los primeros n números naturales',
        'formula': 'n * (n + 1) / 2',
        'valid_from_n': 1,
        'base_case': 1,
        'next_step': 'n+1'
    },
    {
        "description": "Suma de los cuadrados de los primeros n números impares",
        "formula": "(n * ((2 * n) + 1) * ((2 * n) - 1)) / 3",
        "valid_from_n": 1,
        "base_case": 1,
        "next_step": "(2*(n+1) - 1)**2"
    },
    {
        'description': 'Suma de los primeros n números cuadrados',
        'formula': '(n * (n + 1) * ((2*n) + 1)) / 6',
        'valid_from_n': 1,
        'base_case': 1,
        'next_step': '(n+1) **2'
    },
    {
        'description': 'Suma de los primeros n números cúbicos',
        'formula': '((n*(n+1))/(2))**2',
        'valid_from_n': 1,
        'base_case': 1,
        'next_step': '(n+1)**3'
    },
    {
        'description': 'Suma de los primeros n números de la forma 2^n - 1',
        'formula': '2**(n+1) - n - 2',
        'valid_from_n': 1,
        'base_case': 1,
        'next_step': '(2**(n+1) - 1)'
    }
]

# Itera sobre los casos de prueba y llama a la función
for i, case in enumerate(test_cases):
    result = prove_arithmetic_series_formula(
        case['formula'],
        case['valid_from_n'],
        case['base_case'],
        case['next_step']
    )
    print(f"Resultado del caso de prueba {i+1}: {result}")