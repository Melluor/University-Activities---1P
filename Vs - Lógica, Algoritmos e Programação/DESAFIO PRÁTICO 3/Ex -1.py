'''1. Faça um programa em Python que receba 10 idades, calcule e exiba: 
A) a média das idades;
B) a mediana; 
C) a moda.'''
idades = []

# MÉDIA
soma_age = 0
for age in range(1, 11):
    idade = int(input("Digite as idades: "))
    soma_age += idade
    idades.append(idade)
media = soma_age / len(idades)

# MODA
frequencia_moda = {} # Dicionário para guardar valor e quantidade de aparecimentos.
for mo in idades:
    if mo in frequencia_moda:
        frequencia_moda[mo] += 1 # Se já estiver aparecido antes, soma mais uma frequência.
    else:
        frequencia_moda[mo] = 1
    maior = max(frequencia_moda.values()) # Pega a chave que tiver a maior frequência de aparecimento.

# MEDIANA
lista_ord = sorted(idades) # Ordenará a lista sem alterá-la.
lista_tam = len(lista_ord) # Receberá o tamanho da lista para a dividir no meio.
lista_meio = lista_tam // 2
if lista_tam % 2 == 1: 
    resposta_med = lista_ord[lista_meio] # Se for uma "lista ímpar", vai retornar o valor do meio.
else:
    resposta_med = (lista_ord[lista_meio - 1] + lista_ord[lista_meio]) / 2 # Se for uma "lista par", vai retornar a média dos 2 valores do meio.

print(f"MÉDIA DAS IDADES: {media:.2f}")
print(f"MODA DAS IDADES: {[key for key, freq in frequencia_moda.items() if freq == maior]}") # Percorre os pares 'key, freq' (Chave: Valor) e guarda só as chaves que a frequência for igual a 'maior'.
print(f"MEDIANA DAS IDADES: {resposta_med}")