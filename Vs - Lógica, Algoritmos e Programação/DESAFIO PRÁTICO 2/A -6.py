# 6. Probabilidade experimental. Um experimento consiste em lançar um dado 20 vezes. O programa recebe o resultado de cada lançamento e deve contar quantas vezes apareceu um número par. Ao final, deve calcular a probabilidade experimental de obter um número par.
contador_pares = 0
num_lancamentos = 20

for dado in range(1, num_lancamentos + 1):
    lancamento = int(input('Digite o resultado inteiro do lançamento do dado: '))
    
    if lancamento < 1 or lancamento > 6:
        print("Intervalor inválido! Digite um número entre 1 e 6.")
        continue

    if lancamento % 2 == 0:
        contador_pares += 1

print(contador_pares)
prob_experimental = contador_pares / num_lancamentos

print(f"Após 20 lançamentos, a probabilidade experimental de obter um número par é: {prob_experimental}")