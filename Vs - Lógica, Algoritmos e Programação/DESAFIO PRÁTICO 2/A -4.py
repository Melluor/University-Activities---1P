# 4. Seleção de atributos para um modelo. Um conjunto de dados possui n atributos disponíveis. O analista deseja selecionar r atributos para uma etapa de modelagem, sem considerar a ordem de seleção. Calcule o número de subconjuntos possíveis usando: 

# C(n, r) = n! / (r! * (n-r)!)

# O programa deve validar 0 <= r <= n e informar se a quantidade de subconjuntos é compatível com uma busca exaustiva. Considere viável a busca quando houver até 10.000 combinações.
# Requisitos: calcular o resultado sem função pronta de fatorial; utilizar repetição; aplicar decisões para validar os parâmetros e classificar a viabilidade; explicar por que a ordem dos atributos não altera uma combinação.