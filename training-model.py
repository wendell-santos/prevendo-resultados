from sklearn.linear_model import LogisticRegression
import numpy as np
import connector

# Exemplo de coleta de dados históricos
# Para cada partida, coletamos: [casa_fora(1 ou 0), confronto_histórico(1 ou 0), time_desfalcado(1 ou 0)]
partidas = [
    [1, 1, 0],  # Jogo em casa, vitória histórica, sem desfalque
    [0, 0, 1],  # Fora de casa, derrota, com desfalque
    [1, 0, 0],  # Casa, derrota histórica, sem desfalque
]

resultados = [1, 0, 0]  # Vitórias (1) ou Derrotas (0)

# Criando o modelo
modelo = LogisticRegression()
modelo.fit(partidas, resultados)

# Exemplo de previsão para um novo jogo
novo_jogo = np.array([[1, 0, 0]])  # Em casa, derrota histórica, sem desfalque
probabilidade = modelo.predict_proba(novo_jogo)
print("Probabilidade de vitória:", probabilidade[0][1])
