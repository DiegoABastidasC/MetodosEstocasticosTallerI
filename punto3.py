import random

def simular_experimento(num_simulaciones=1000000):
    clases = {
        "Clase 1": {"A": 16, "B": 4},
        "Clase 2": {"A": 14, "B": 6},
        "Clase 3": {"A": 12, "B": 8}
    }
    
    clases_lista = list(clases.keys())
    estudiantes_B = 0
    clase_1_dado_A = 0
    total_A = 0
    
    for _ in range(num_simulaciones):
        clase_elegida = random.choice(clases_lista)
        estudiante_tipo = random.choices(["A", "B"], weights=[clases[clase_elegida]["A"], clases[clase_elegida]["B"]])[0]
        
        if estudiante_tipo == "B":
            estudiantes_B += 1
        if estudiante_tipo == "A":
            total_A += 1
            if clase_elegida == "Clase 1":
                clase_1_dado_A += 1
    
    probabilidad_B = estudiantes_B / num_simulaciones
    probabilidad_clase_1_dado_A = clase_1_dado_A / total_A
    
    return probabilidad_B, probabilidad_clase_1_dado_A

prob_B, prob_clase_1_dado_A = simular_experimento()
print(f"Probabilidad de que el estudiante elegido sea del tipo B: {prob_B:.4f}")
print(f"Probabilidad de que un estudiante del tipo A sea de la Clase 1: {prob_clase_1_dado_A:.4f}")
