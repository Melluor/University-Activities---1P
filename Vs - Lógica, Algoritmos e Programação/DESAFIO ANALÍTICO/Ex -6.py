# 6. Observe o código a seguir e analise as questões pedidas.

# A -> Código modificado:
L = []
for num in iter(lambda: int(input("Digite um número ou 0 para sair: ")), 0):
    L.append(num)
# iter, com dois argumentos, receberá uma função (poderia usar uma função def já pré-definida) e um "sentinela", onde continuará perguntando até o usuário digitar o mesmo valor do sentinela. Lambida é uma função temporária, onde é chamável sem necessidade de argumentos. Sem ela, o programa perguntaria somente uma única vez. Tive ajuda da IA.
for num in L:
    print(num)

# OUTRA FORMA DE ESCREVER O MESMO PROGRAMA:
'''def ler_numero():
    return int(input("Digite um número ou 0 para sair: "))
for n in iter(ler_numero, 0):
    L.append(n)
for num in L:
    print(num)'''

# B -> Resposta: Sim, mas com alguma ajuda externa por conta de não estar conseguindo encontrar uma forma de modificar a primeira repetição. A segunda é facilmente modificável.