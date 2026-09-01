# 5. Uma população inicial de 2727 indivíduos cresce a uma taxa de 4% ao ano. Escreva um programa em Python que simule o crescimento dessa população e mostre o tamanho da população ao final de cada ano, durante 5 anos.
pop_inicial = 2727
taxa_crescimento = 0.04
anos = 5

for ano in range(1, anos + 1):
    pop_inicial = pop_inicial + (pop_inicial * taxa_crescimento)
    print(f'População no ano {ano}: {pop_inicial:.0f}')
print(f"População após 5 anos: {pop_inicial:.0f}")