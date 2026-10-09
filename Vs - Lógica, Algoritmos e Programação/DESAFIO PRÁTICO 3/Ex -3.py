''' 3. Uma escola deseja armazenar as notas de seus alunos utilizando uma lista dentro de outra lista. Cada lista interna representa um aluno e contém suas três notas obtidas durante o semestre. Considere a seguinte estrutura: ...
Cada elemento da lista alunos possui a seguinte estrutura:
[nome, nota1, nota2, nota3]
Sua tarefa é criar um programa em Python que percorra essa lista e apresente um
relatório contendo:
a)  O nome de cada aluno;
b)  A média das três notas de cada aluno;
c)  Se o aluno está aprovado ou reprovado, considerando que a média mínima para aprovação é 7,0;
d)  a média geral da turma;
e)  o nome do aluno com a maior média;
f)  o nome do aluno com a menor média;
g)  quantos alunos foram aprovados;
h)  quantos alunos foram reprovados.'''
alunos = [
    ["Ana", 7.5, 8.0, 9.0],
    ["Bruno", 6.0, 5.5, 7.0],
    ["Carlos", 9.0, 8.5, 10.0],
    ["Daniela", 5.0, 6.0, 4.5],
    ["Eduardo", 8.0, 7.5, 6.5]
]
aprovados = 0
reprovados = 0
maior_media = 0
menor_media = 10

for m in alunos: # A - C & E - F
    media = (m[1] + m[2] + m[3]) / 3
    if media > maior_media:
        maior_media = media
        aluno_maior = m[0]

    if media < menor_media:
        menor_media = media
        aluno_menor = m[0]

    print(f"ALUNO: {m[0]} | MÉDIA: {media:.2f}")
    if media >= 7:
        print("APROVADO.")
        aprovados += 1
    else:
        print("REPROVADO.")
        reprovados += 1

medias = 0
for mg in alunos: # D
    medias += mg[1] 
    medias += mg[2]
    medias += mg[3]
    media_geral = medias / 15
print(f"\nMÉDIA GERAL DA TURMA: {media_geral}\n")

print(f"ALUNO COM MAIOR MÉDIA DA TURMA: {aluno_maior} | MÉDIA: {maior_media:.2f}")
print(f"ALUNO COM MENOR MÉDIA DA TURMA: {aluno_menor} | MÉDIA: {menor_media:.2f}\n")

print(f"QUANTIDADE DE APROVADOS: {aprovados}") #G
print(f"QUANTIDADE DE REPROVADOS: {reprovados}") # H