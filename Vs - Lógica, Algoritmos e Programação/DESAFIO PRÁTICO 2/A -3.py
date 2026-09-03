# 3. Resumo estatístico de notas de um curso. 
# Leia as notas de uma turma até que o usuário digite algo para sair. Para cada nota válida, determine se o estudante foi aprovado, ficou em recuperação ou foi reprovado. Considere aprovado para nota maior ou igual a 7,0, recuperação para nota entre 5,0 e 6,9, e reprovação para nota inferior a 5,0. Ao final, apresente a média da turma, a maior nota, a menor nota, o percentual de aprovação e a situação geral da turma. Classifique a turma como “desempenho satisfatório” quando o percentual de aprovação for igual ou superior a 70%. 
# Requisitos: utilizar while; aceitar notas entre 0 e 10; não encerrar a leitura ao receber um valor inválido; impedir divisão por zero; utilizar decisões para a situação individual e para a classificação geral.
nota = 0
menor_nota = 10
maior_nota = 0
qtd_aprovados = 0
soma_das_notas = 0
qtd_notas_validas = 0

print("Resumo estatístico de notas do curso")
print("Digite '99' para sair do programa!")
while True:
    nota = float(input("Digite a nota: "))

    if nota == 99:
        break

    if not (nota >= 0 and nota <= 10):
        print('Nota inválida! Digite uma nota entre 0 e 10.')
        continue

    soma_das_notas = soma_das_notas + nota
    qtd_notas_validas += 1

    if nota >= 7:
        print("Situação: Aprovado.")
        qtd_aprovados += 1
    elif nota >= 5 and nota <= 6.9:
        print("Situação: Recuperação.")
    else:
        print("Situação: Reprovado.")

    if nota < menor_nota:
            menor_nota = nota
    
    if nota > maior_nota:
        maior_nota = nota

if qtd_notas_validas != 0:
    media_turma = soma_das_notas / qtd_notas_validas
    percentual_aprovados = (qtd_aprovados / qtd_notas_validas) * 100
else:
    print("Quantidade de notas inválida! Não pode haver 0 notas.")

print("=== RESUMO DA TURMA ===")
print(f"""
Média da turma: {media_turma:.2f}
Maior nota: {maior_nota:.2f}
Menor nota: {menor_nota:.2f}
Percentual de aprovação: {percentual_aprovados:.2f}""")

if percentual_aprovados >= 70:
    print("Situação da turma: Desempenho satisfatório.")
else:
    print("Situação da turma: Não satisfatório.")