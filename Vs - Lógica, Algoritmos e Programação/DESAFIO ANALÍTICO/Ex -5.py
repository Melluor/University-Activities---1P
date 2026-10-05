# 5. Observe o código a seguir e analise as questões pedidas.

# A -> Resposta:
'''
Linha 20: Variável usada para verificar se foi encontrado o valor.
Linha 24: Variável mudou para verdadeira após ter encontrado o valor digitado na lista.
Linha 25: Vai quebrar o Loop While quando a condição for verdadeira.
Linhas 27: Condicional para verificar se foi ou não encontrado o valor na lista.
'''

# B -> Código reefeito:
'''L = [15, 7, 27, 29]
p = int(input("Digite o valor a procurar: "))
x = 0
while x < len(L):
    if L[x] == p:
        print(f"{p} achado na posição {x}")
        break
    x += 1
print(f"{p} não encontrado")'''