# 3. Utilizando função e a bilioteca math crie um programa para calcular as possíveis raízes de uma equação do 2º grau. Sabendo que: ax² + bx + c = 0. Determine e mostre o número de raízes reais distintas que a equação possui. Regra: O número de raízes reais depende do discriminante (delta), Δ = b² - 4ac: 

# • Δ > 0: Duas raízes reais distintas. 
# • Δ = 0: Uma raiz real (ou duas raízes reais iguais). 
# • Δ < 0: Nenhuma raiz real (duas raízes complexa.
from math import sqrt

def bhaskara(A: float, B: float, C: float) -> tuple[float, tuple[float]]:
    delta = (B * B) - (4 * A * C) # Delta: b² - 4.a.c

    if delta > 0:
        raiz_1 = (-B + sqrt(delta)) / (2 * A) # '(-b + √b²-4.a.c) / 2.a'
        raiz_2 = (-B - sqrt(delta)) / (2 * A) # '(-b - √b²-4.a.c) / 2.a'

        return delta, (raiz_1, raiz_2)

    elif delta == 0:
        raiz_uni = -B / (2 * A) # Raiz de 0 é 0; '-b / 2.a'.

        return delta, (raiz_uni)

    else:
        return delta, () 

coef_quad = float(input("Insira o Coeficiente Quadrático ('A'): "))
coef_lin = float(input("Insira a Coeficiente Linear ('B'): "))
coef_cons = float(input("Insira o Coeficiente Constante ('C'): "))

if coef_quad == 0:
    print("\nErro! Não é uma equação de 2º grau. ('A' deve ser diferente de 0).")
else:
    delta, raizes = bhaskara(coef_quad, coef_lin, coef_cons) # Atribui a função à essas variáveis; variável delta para o delta dentro da função e raizes para os valores da tupla de raizes da função.

    print(f"\nDelta: {delta}")
    print(f"Número de raízes reais distintas: {len(raizes)}.")

    if len(raizes) == 2:
        print(f"RAÍZES DA EQUAÇÃO: {raizes[0]:.2f} | {raizes[1]:.2f}") # Mostra a posição da dupla retornada na função. 'Raiz 1 | Raiz 2'.

    elif len(raizes) == 1:
        print(f"A equação possui uma única raiz. RAIZ DA EQUAÇÃO: {raizes[0]:.2f}") # Mostra a posição da raiz na tupla. 'Raiz 1'.

    else:
        print("Delta menor que 0. A equação não possui raízes reais.")