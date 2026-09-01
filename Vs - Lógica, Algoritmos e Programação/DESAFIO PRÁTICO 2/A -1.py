# 1. Utilizando uma estrutura de repetição, escreva um programa em Python que calcule o fatorial de um número informado pelo usuário.
numero = int(input("Informe um número: "))
# contador = 1
resultado = 1

for num in range(1, numero + 1):
    #Sem o 'numero + 1', o for ou começaria por 0 e todos os resultados seriam 0 ou não multiplicaria pelo último número.
    resultado = resultado * num
    print(resultado)

# while contador <= numero:
#     resultado = resultado * contador
#     contador += 1
#     print(resultado)