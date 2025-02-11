import numpy as np

def calculate(list):
    # Verifica si la lista tiene 9 elementos
    if len(list) != 9:
        raise ValueError("La lista debe contener nueve números.")

    # Convierte la lista en una matriz de 3x3
    matrix = np.array(list).reshape(3, 3)

    # Calcula las estadísticas requeridas
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }

    return calculations
