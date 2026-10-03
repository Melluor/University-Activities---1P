# ============================================
# ANÁLISE DE DADOS COM LISTAS - HACKATHON
# ============================================

vendas = [
    [1, "Notebook", "Informática", 3500.00, 2, "Norte"],
    [2, "Mouse", "Informática", 80.00, 8, "Nordeste"],
    [3, "Teclado", "Informática", 150.00, 8, "Sul"],
    [4, "Monitor", "Informática", 1200.00, 5, "Sudeste"],
    [5, "Cadeira", "Móveis", 900.00, 5, "Nordeste"],
    [6, "Mesa", "Móveis", 1200.00, 4, "Norte"],
    [7, "Smartphone", "Eletrônicos", 2200.00, 10, "Sudeste"],
    [8, "Tablet", "Eletrônicos", 1600.00, 6, "Sul"],
    [9, "Fone de ouvido", "Eletrônicos", 250.00, 20, "Nordeste"],
    [10, "Webcam", "Informática", 350.00, 7, "Norte"],
    [11, "Impressora", "Informática", 850.00, 4, "Sudeste"],
    [12, "HD Externo", "Informática", 450.00, 9, "Sul"],
    [13, "SSD", "Informática", 600.00, 12, "Nordeste"],
    [14, "Estante", "Móveis", 750.00, 5, "Norte"],
    [15, "Sofá", "Móveis", 2500.00, 2, "Sudeste"],
    [16, "Luminária", "Móveis", 180.00, 11, "Sul"],
    [17, "Smart TV", "Eletrônicos", 3200.00, 3, "Nordeste"],
    [18, "Câmera", "Eletrônicos", 2800.00, 4, "Sudeste"],
    [19, "Microfone", "Eletrônicos", 500.00, 8, "Norte"],
    [20, "Pen Drive", "Informática", 60.00, 25, "Sul"]
]

# a) MOSTRAR O TOTAL DE ITENS (Listas)
def A():
    print(f"Vendas: {len(vendas)} Itens.\n")

# b) PRIMEIRO E ÚLTIMO REGISTRO
def B():
    print(f"Primeiro registro: {vendas[0]} \nÚltimo registro: {vendas[-1]}\n")

# c) TODOS OS NOMES DOS PRODUTOS
def C():
    for prod in vendas:
        print(f"Produto disponível: {prod[1]}\n")
    
# d) MAIOR E MENOR PREÇO
def D():
    maior = vendas[0][3]
    menor = vendas[0][3]

    for item in vendas:
        if item[3] > maior:
            maior = item[3]
        if item[3] < menor:
            menor = item[3]

    print(f"\nMaior preço: {maior} | Menor preço: {menor}\n")

# e) PRODUTO COM MAIOR PREÇO
def E():
    maior = vendas[0][3]
    produto = vendas[0][1]

    for item in vendas:
        if item[3] > maior:
            maior = item[3]
            produto = item[1]
    print(f"Produto {produto} tem o preço {maior}\n")

# f) QUANTIDADE TOTAL DE PRODUTOS VENDIDOS
def F():
    vendidos = vendas[0][4]

    for vendi in vendas:
        vendidos += vendi[4]
    print(f"Produtos vendidos: {vendidos} produtos.\n")

# g) FATURAMENTO DE CADA PRODUTO
def G():
    print(f"== Faturamento dos produtos individualmente ==")
    for item in vendas:
        faturamento_produto = item[3] * item[4]
        produto = item[1]
        print(f"{produto} : {faturamento_produto}\n")

# h) FATURAMENTO TOTAL DA EMPRESA
def H():
    faturamento_total = 0

    print(f"== Faturamento Total da empresa ==")
    for item in vendas:
        faturamento_total += item[3] * item[4]
    print(f"Faturamento Total: {faturamento_total}\n")

# i) MAIOR E MENOR FATURAMENTO
def I():
    maior_faturamento = vendas[0][3]
    menor_faturamento = vendas[0][3]

    for item in vendas:
        faturamento_produto = item[3] * item[4]

        if faturamento_produto > maior_faturamento:
            maior_faturamento = faturamento_produto

        if faturamento_produto < maior_faturamento and faturamento_produto < menor_faturamento:
            menor_faturamento = faturamento_produto
    print(f"Maior faturamento: {maior_faturamento} | Menor faturamento: {menor_faturamento}\n")

# j) PRODUTOS DE UMA DETERMINADA CATEGORIA
def J():
    Cat_Info = []
    Cat_Ele = []
    Cat_Mov = []

    for cat in vendas:
        if cat[2] == "Informática":
            Cat_Info.append(cat[1])
        if cat[2] == "Eletrônicos":
            Cat_Ele.append(cat[1])
        if cat[2] == "Móveis":
            Cat_Mov.append(cat[1])

    print(f"Produtos de informática: {Cat_Info}")
    print(f"Produtos de Eletrônicos: {Cat_Ele}")
    print(f"Produtos de Móveis: {Cat_Mov}\n")

# k) QUANTIDADE DE PRODUTOS EM CADA CATEGORIA
def K():
    Info_v = 0
    Ele_v = 0
    Mov_v = 0

    for cat in vendas:
        if cat[2] == "Informática":
            Info_v += cat[4]
        if cat[2] == "Eletrônicos":
            Ele_v += cat[4]
        if cat[2] == "Móveis":
            Mov_v += cat[4]

    print(f"Quantidade de produtos de informática: {Info_v}")
    print(f"Quantidade de produtos de Eletrônicos: {Ele_v}")
    print(f"Quantidade de pProdutos de Móveis: {Mov_v}\n")

# l) QUANTIDADE DE REGISTROS POR REGIÃO
def L():
    R_norte = 0
    R_nordeste = 0
    R_sul = 0
    R_sudeste = 0

    for reg in vendas:
        if reg[5] == 'Norte':
            R_norte += 1
        elif reg[5] == 'Nordeste':
            R_nordeste += 1
        elif reg[5] == 'Sul':
            R_sul += 1
        else:
            R_sudeste += 1
    print(f"Norte: {R_norte} registros. | Nordeste: {R_nordeste} registros. | Sul: {R_sul} registros. | Sudeste: {R_sudeste} registros.\n")

# m) PRODUTO MAIS VENDIDO
def M():
    mais_Vendido = vendas[0][4]
    produto = vendas[0][1]

    for mais_v in vendas:
        if mais_v[4] > mais_Vendido:
            mais_Vendido = mais_v[4]
            produto = mais_v[1]
    print(f"Produtos mais vendido: {produto} | Quatidade de vezes: {mais_Vendido}\n")

def menu():
    while True:
        print(
"""\n=== MENU DE ANÁLISE DE VENDAS ===
"1 - Total de itens"
"2 - Primeiro e último registro"
"3 - Nomes dos produtos"
"4 - Maior e menor preço"
"5 - Produto com maior preço"
"6 - Quantidade total de produtos vendidos"
"7 - Faturamento de cada produto"
"8 - Faturamento total da empresa"
"9 - Maior e menor faturamento"
"10 - Produtos por categoria"
"11 - Quantidade por categoria"
"12 - Registros por região"
"13 - Produto mais vendido"
"14 - Executar todas as funções em ordem\n""")

        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                A()
            case 2:
                B()
            case 3:
                C()
            case 4:
                D()
            case 5:
                E()
            case 6:
                F()
            case 7:
                G()
            case 8:
                H()
            case 9:
                I()
            case 10:
                J()
            case 11:
                K()
            case 12:
                L()
            case 13:
                M()
            case 14:
                A()
                B()
                C()
                D()
                E()
                F()
                G()
                H()
                I()
                J()
                K()
                L()
                M()
            case _:
                print("Opção inválida. Escolha uma opção do menu.")
                resposta = input("Deseja sair?: ").strip().upper()
                if resposta == "S":
                    print("Adeus, volte sempre.")
                    break
menu()