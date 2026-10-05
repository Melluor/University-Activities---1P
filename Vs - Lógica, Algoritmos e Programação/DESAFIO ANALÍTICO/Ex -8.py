# 8. Escreva um código que receba números ou palavras. O código deve armazenar cada situação em listas diferentes, ou seja, uma lista só para as palavras e outra só para os números. O programa deve encerrar quando o usuário digitar o x ou X. No fim, mostre o que foi inserido nas duas listas, a quantidade total de coisas digitadas pelo usuário. (Dica: métodos em Python)
numeros = []
palavras = []

while True:
    entrada = input("DIGITE UM NÚMERO OU UMA PALAVRA (x para sair): ")

    if entrada.lower() == 'x':
        break

    if entrada.lstrip('-').isdigit(): #lstrip para tirar o possível sinal (negativo ou positivo) e isdigit para verificar se é um dígito (número).
        numeros.append(float(entrada)) #especificar o tipo de dado a ser inserido na lista (float, nesse caso).
    elif entrada.strip().isalpha():
        palavras.append(entrada)
    else:
        print("Entrada inválida, tente novamente.")
        continue
print(f"PALAVRAS INSERIDAS: {palavras}")
print(f"NÚMEROS INSERIDOS: {numeros}")
print(f"QUANTIDADE TOTAL DE ENTRADAS {len(palavras) + len(numeros)}")