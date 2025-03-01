def calcular_eventos(espacio_muestral, A, B):
    # Se verifica si A y B son eventos de Ω
    es_A_evento = A.issubset(espacio_muestral)
    es_B_evento = B.issubset(espacio_muestral)
    
    # Complemento de A
    complemento_A = espacio_muestral - A
    
    # Unión de A y B
    union_AB = A | B
    
    # Intersección de A y B
    interseccion_AB = A & B
    
    # Diferencia de A y B (A - B)
    diferencia_AB = A - B
    
    # Diferencia simétrica de A y B (A XOR B)
    diferencia_simetrica_AB = A ^ B
    
    # Imprimir resultados
    print(f"¿Es A un evento de Ω? {'Sí' if es_A_evento else 'No'}")
    print(f"¿Es B un evento de Ω? {'Sí' if es_B_evento else 'No'}")
    print(f"Complemento de A: {complemento_A}")
    print(f"Unión de A y B: {union_AB}")
    print(f"Intersección de A y B: {interseccion_AB}")
    print(f"Diferencia de A y B (A - B): {diferencia_AB}")
    print(f"Diferencia simétrica de A y B: {diferencia_simetrica_AB}")

# Ejemplo de uso
espacio_muestral = {1, 2, 3, 4, 5, 6}
A = {1, 2, 3}
B = {3, 4, 5}

calcular_eventos(espacio_muestral, A, B)
