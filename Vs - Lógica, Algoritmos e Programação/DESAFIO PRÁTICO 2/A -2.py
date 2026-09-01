# 2. Supondo que a população de um país A seja da ordem de 90.000 habitantes com uma taxa anual de crescimento de 5% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
pais_A = 90000
pais_B = 200000
contador = 0
taxa_pais_A = 0.050
taxa_pais_B = 0.015

while pais_B >= pais_A:
    pais_A = pais_A + (pais_A * taxa_pais_A)
    pais_B = pais_B + (pais_B * taxa_pais_B)
    contador += 1
print(f'País A: {pais_A:.0f} pessoas à uma taxa de 5%.')
print(f'País B: {pais_B:.0f} pessoas à uma taxa de 1.5%.')
print(f'Foram precisos {contador} anos para que o país A ultrapassasse o país B!')