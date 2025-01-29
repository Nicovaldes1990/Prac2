import random

def player(prev_play: str, opponent_history: list = []):
    # Si es la primera jugada, jugar aleatoriamente
    if prev_play == '':
        return random.choice(['R', 'P', 'S'])
    
    # Guardamos el historial de jugadas del oponente
    opponent_history.append(prev_play)
    
    # Aquí puedes implementar una estrategia simple:
    # Si el oponente jugó 'R' en la última jugada, juega 'P' (para ganarle)
    if prev_play == 'R':
        return 'P'
    # Si el oponente jugó 'P' en la última jugada, juega 'S' (para ganarle)
    elif prev_play == 'P':
        return 'S'
    # Si el oponente jugó 'S' en la última jugada, juega 'R' (para ganarle)
    else:
        return 'R'

