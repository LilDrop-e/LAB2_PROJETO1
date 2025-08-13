def cumprimento(nome):
    return f"Olá, {nome}"

print(cumprimento("Pedro Artur Duran Oliveira"))  

import random
def numero_aleatorio():
    numeros = [random.randint(1, 100) for _ in range(7)]
    return sum(numeros) / len(numeros)
media = numero_aleatorio()
print(f"Média dos 7 números aleatórios: {media:.2f}")