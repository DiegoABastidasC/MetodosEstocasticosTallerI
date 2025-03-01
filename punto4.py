import time

def rng():
    """Generador de números aleatorios (RNG) entre -1 y 1 basado en la hora del sistema."""
    timestamp = time.time()
    decimal_part = timestamp - int(timestamp)  # Extraemos la parte decimal
    return (decimal_part * 2) - 1  # Escalamos entre -1 y 1

def prng(seed):
    """Generador de números pseudoaleatorios (PRNG) entre -100 y 100 usando congruencia lineal."""
    a = 1664525  # Constante multiplicativa
    c = 1013904223  # Incremento
    m = 2**32  # Módulo
    # X_n+1 =( a ⋅ X_n + c)modm
    seed = (a * seed + c) % m  # Algoritmo de congruencia lineal
    return (seed % 201) - 100  # Escalamos entre -100 y 100

# Ejemplo de uso
seed_value = int(time.time())  # Usamos el tiempo como semilla inicial
print(f"Número RNG entre -1 y 1: {rng()}")
print(f"Número PRNG entre -100 y 100: {prng(seed_value)}")
