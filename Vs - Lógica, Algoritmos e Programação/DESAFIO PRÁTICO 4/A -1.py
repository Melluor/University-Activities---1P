# 1. Jogo de Adivinhação. Utilizando a biblioteca random crie um pequeno jogo de adivinhação de números inteiros que deve ir de 1 a 100. As regras do jogo devem ser:
# ●  Todos os palpites do usuário devem ser armazenados.
# ●  O programa deve informar que o usuário errou o palpite e mostrar uma dica se o número a ser descoberto é maior ou menor do que o número do palpite.
# ●  Quando o usuário acertar o palpite o programa deve mostrar: todos os números digitados para o palpite, a quantidade de tentativas.
from random import randint

num_random = randint(1, 100)
palpites = [] # Armazena os palpites.
tentativas = 0 # Armazena as tentativas.

while True:
    num_user = int(input("Adivinhe o número: "))

    if num_user > 100: #Verifica se está na faixa aceitável.
        print("NÚMERO INVÁLIDO! DIGITE UM NÚMERO INTEIRO ENTRE 1 E 100.")
        continue

    if num_user != num_random:
        if num_user > num_random: # Verifica se é diferente e maior.
            print("NÚMERO INCORRETO! " \
            "DICA: O NÚMERO DIGITADO É MAIOR.")
            tentativas += 1
            palpites.append(num_user)

        if num_user < num_random: #Verifica se é diferente e menor.
            print("NÚMERO INCORRETO! " \
            "DICA: O NÚMERO DIGITADO É MENOR.")
            tentativas += 1
            palpites.append(num_user)

    if num_user == num_random: # Mostra os dados necessários.
        print(f"CORRETO! O NÚMERO ALEATÓRIO ERA: {num_random}.")
        print(f"NÚMEROS DIGITADOS: {palpites}")
        tentativas += 1
        print(f"QUANTIDADE DE TENTATIVAS: {tentativas}")
        break