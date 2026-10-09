# 7. Uma empresa de construção precisa calcular rapidamente a área de diferentes figuras geométricas. Crie três funções para a área do triângulo, área do trapézio e área do losango.

def triangulo() -> None:
    base = float(input("Digite a medida da base do triângulo (Em cm): "))
    altura = float(input("Digite a medida da altura do triângulo (Em cm): "))
    area_tri = (base * altura) / 2
    
    print(f"Área do triângulo: {area_tri}")

def trapezio() -> None:
    Base_maior = float(input("Digite a medida da Base maior do Trapézio (Em cm): "))
    Base_menor = float(input("Digite a medida da Base menor do Trapézio (Em cm): "))
    altura = float(input("Digite a medida da altura do Trapézio (Em cm): "))

    area_tra = ((Base_maior + Base_menor) * altura) / 2

    print(f"Área do Trapézio: {area_tra}")

def loosango() -> None:
    Diagonal_maior = float(input("Digite a medida da Diagonal maior do Losango (Em cm): "))
    Diagonal_menor = float(input("Digite a medida da Diagonal menor do Losango (Em cm): "))

    area_lo = (Diagonal_maior * Diagonal_menor) / 2

    print(f"Área do Losango: {area_lo}")

escolha = int(input("1. Área do triângulo | 2. Área do Trapézio | 3. Área do Losango\n"))
match escolha:
    case 1:
        triangulo()
    case 2:
        trapezio()
    case 3:
        loosango()
    case _:
        print("Opção inválida.")