# === 1. Observe o código apresentado a seguir e veja outras formas de inserir dados em uma lista. ===

'''numero = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numero[x] = float(input("Digite um número qualquer: "))
    x += 1
y = 0
while y < 5:
    print(f"{numero[y]}")
    y += 1'''

# A
'''numeros = [0, 0, 0, 0, 0]
x = 0
for number in range(0, 5):
    numeros[x] = float(input("Digite um número qualquer: "))
    x += 1
y = 0
for number in range(0, 5):
    print(f"{numeros[y]}")
    y += 1'''

# B -> Resposta: O programa funcionaria da mesma forma, já que ainda seriam necessários 5 itens para o array.

# C -> Resposta: Não, já que o array já possui um tamanho pré-determinado (5 elementos).

# D -> Resposta: A falta de escalabilidade e adaptabilidade para maiores volumes de dados.

# E -> Código refeito:
'''numeros = []
while True:
    numero = float(input("Digite um número qualquer: "))
    numeros.append(numero)
    resposta = input("Deseja parar? (S/N): ").strip().upper()
    if resposta == 'S':
        break
for num in numeros:
    print(f"{num}")'''