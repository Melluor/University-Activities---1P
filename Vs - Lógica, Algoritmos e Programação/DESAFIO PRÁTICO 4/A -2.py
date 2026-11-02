# 2. O professor de matemática Alan Turing pediu sua ajuda para criar um pequeno sistema para calcular as áreas das figuras planas. Ele pediu que o usuário possa escolher qual figura quer calcular. Para cada cálculo de uma figura faça uma função específica. Utilize a figura abaixo como apoio matemático e das figuras que seu programa deve conter. Dica: utilize a biblioteca math.
from math import pi

def triangulo() -> None:
    base = float(input("Digite o tamanho da base do triâgulo (Em cm): "))
    height = float(input("Digite o tamanho da altura do triâgulo (Em cm): "))

    area_tri = (base * height) / 2
    print(f"ÁREA DO TRIÂNGULO: {area_tri:.2f} centímetros.")

def retangulo() -> None:
    base = float(input("Tamanho da base do retângulo (Em cm): "))
    height = float(input("Tamanho da altura do retângulo (Em cm): "))

    area_ret = base * height
    print(f"ÁREA DO RETÂNGULO: {area_ret:.2f} centímetros.")

def quadrado() -> None:
    side = float(input("Tamanho do lado do quadrado (Em cm): "))

    area_qua = side * side
    print(f"ÁREA DO QUADRADO: {area_qua:.2f} centímetros.")

def trapezio() -> None:
    long_base = float(input("Tamanho da base maior (Em cm): "))
    short_base = float(input("Tamanho da base menor (Em cm): "))
    height = float(input("Tamanho da altura do trapézio (Em cm): "))

    area_tra = ((long_base + short_base) * height) / 2
    print(f"ÁREA DO TRAPÉZIO: {area_tra:.2f}")

def losango() -> None:
    major_diagonal = float(input("Tamanho da diagonal maior (Em cm): "))
    minor_diagonal = float(input("Tamanho da diagonal menor (Em cm): "))

    area_lo = (major_diagonal * minor_diagonal) / 2
    print(f"ÁREA DO LOSANGO: {area_lo:.2f}")

def circulo() -> None:
    radius = float(input("Tamanho do raio do círculo (Em cm): "))

    area_ci = pi * (radius * radius)
    print(f"ÁREA DO CÍRCULO: {area_ci:.2f}")

print("""
== FIGURAS PLANAS ==
1. Triângulo.
2. Retângulo.
3. Quadrado.
4. Trapézio.
5. Losango.
6. Círculo.""")
option = int(input("Escolha qual figura calcular: "))
match option:
    case 1:
        triangulo()
    case 2:
        retangulo()
    case 3:
        quadrado()
    case 4:
        trapezio()
    case 5:
        losango()
    case 6:
        circulo()
    case _:
        print("Opção Inválida!")