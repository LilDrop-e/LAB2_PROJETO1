def cumprimento(nome):
    return f"Olá, {nome}"

print(cumprimento("Pedro Artur Duran Oliveira"))  

import random 
def media_aleatoria():
    numeros = [random.randint(1, 100) for _ in range(7)]
    return sum(numeros) / len(numeros)
media = media_aleatoria()
print(f"Média aleatória: {media:.2f}")