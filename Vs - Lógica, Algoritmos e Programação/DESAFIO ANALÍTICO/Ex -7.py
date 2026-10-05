# 7. Sabemos que as listas possuem funções que ajudam a construir programas sem escrever muito código. Vimos as funções: max(), min(), sum() e enumerate().
'''T = [-10, -8, 0, 1, 2, 20, -2, -4]
soma = 0
for i in range(len(T)):
    soma += T[i]
print(f"A soma total da lista é {soma}")'''

# === A -> Maior
'''T = [-10, -8, 0, 1, 2, 20, -2, -4]
soma = 0
maior = 0
for i in range(len(T)):
    soma += T[i]
    if T[i] > maior:
        maior = T[i]
print(f"A soma total da lista é {soma}")
print(f"O maior da lista é {maior}")'''

# == B -> Menor
'''T = [-10, -8, 0, 1, 2, 20, -2, -4]
soma = 0
menor = 100
for i in range(len(T)):
    soma += T[i]
    if T[i] < menor:
        menor = T[i]
print(f"A soma total da lista é {soma}")
print(f"O menor da lista é {menor}")'''

# === C -> Endereço e número
'''T = [-10, -8, 0, 1, 2, 20, -2, -4]
soma = 0
for i in range(len(T)):
    soma += T[i]
print(f"A soma total da lista é {soma}")

for elem in range(len(T)):
    print(f"Elemento {elem} no endereço {T[elem]}")'''
# len(T) vai devolver o tamanho da lista (começando em 0 até 8, já que são 8 elementos), então 'elem' assumirá cada posição da lista (elem na posição 0, depois elem na posiç ão 1, ...) e L[elem] vai acessar o elemento (L[elem] receberá -10, depois L[elem] reeberá -8, ...) específico daquela posição.