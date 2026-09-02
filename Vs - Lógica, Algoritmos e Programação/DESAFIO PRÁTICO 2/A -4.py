# 4. Seleção de atributos para um modelo. Um conjunto de dados possui n atributos disponíveis. O analista deseja selecionar r atributos para uma etapa de modelagem, sem considerar a ordem de seleção. Calcule o número de subconjuntos possíveis usando: 

# C(n, r) = n! / (r! * (n-r)!)

# O programa deve validar 0 <= r <= n e informar se a quantidade de subconjuntos é compatível com uma busca exaustiva. Considere viável a busca quando houver até 10.000 combinações.
# Requisitos: calcular o resultado sem função pronta de fatorial; utilizar repetição; aplicar decisões para validar os parâmetros e classificar a viabilidade; explicar por que a ordem dos atributos não altera uma combinação.
atributos_disponiveis = int(input("Quantidade total de atributos disponíveis: ")) #N
atributos_escolhidos = int(input("Quantidade de atributos que serão escolhidos: ")) #R

#"Tratamento de erro" simples.
if not (atributos_disponiveis >= 0 and atributos_disponiveis >= atributos_escolhidos):
    print("\nValores inválidos para o cálculo!")
else:
    atri_disp_result = 1
    atri_esc_result = 1

    #Fatorial de N (Atributos Disponíveis).
    for num in range(1, atributos_disponiveis + 1): 
        atri_disp_result = atri_disp_result * num

    #Fatorial de R (Atributos Escolhidos).
    for num in range(1, atributos_escolhidos + 1): 
        atri_esc_result = atri_esc_result * num

    atributos_subtraidos = atributos_disponiveis - atributos_escolhidos
    atri_sub_result = 1

    #Fatorial de N - R
    for num in range(1, atributos_subtraidos + 1): 
        atri_sub_result = atri_sub_result * num

    #Resultado da combinação.
    combinacao = atri_disp_result / (atri_esc_result * (atri_sub_result))
    print(f"\nA quantidade de subconjuntos para a combinação dos valores é: {combinacao:.2f}")

    #Declaração se é viável ou inviável a busca.
    if combinacao <= 10000:
        print("BUSCA EXAUSTIVA É VIÁVEL.")
    else:
        print("BUSCA EXAUSTIVA É INVIÁVEL.")