# 3. Resumo estatístico de notas de um curso. 
# Leia as notas de uma turma até que o usuário digite algo para sair. Para cada nota válida, determine se o estudante foi aprovado, ficou em recuperação ou foi reprovado. Considere aprovado para nota maior ou igual a 7,0, recuperação para nota entre 5,0 e 6,9, e reprovação para nota inferior a 5,0. Ao final, apresente a média da turma, a maior nota, a menor nota, o percentual de aprovação e a situação geral da turma. Classifique a turma como “desempenho satisfatório” quando o percentual de aprovação for igual ou superior a 70%. 
# Requisitos: utilizar while; aceitar notas entre 0 e 10; não encerrar a leitura ao receber um valor inválido; impedir divisão por zero; utilizar decisões para a situação individual e para a classificação geral.
lista_aprovados = []
lista_recuperacao = []
lista_reprovados = []

print("\nResumo estatístico de notas de curso!")
print("ATENÇÃO! Digite '99' para sair da leitura de notas!\n")
while True:
    nota = float(input("Digite as notas do curso: "))
    if nota == 99:
        print("Saindo da leitura! Adeus.")
        break
    if nota < 0 or nota > 10:
        print("Digite um valor válido!")
        continue
    # === - ===
    if nota >= 7:
        print("Resultado: APROVADO.")
        lista_aprovados.append(nota)
    elif nota <= 6.9 and nota >= 5:
        print("Resultado: Recuperação.")
        lista_recuperacao.append(nota)
    else:
        print("Resultado: Reprovado.")
        lista_reprovados.append(nota)