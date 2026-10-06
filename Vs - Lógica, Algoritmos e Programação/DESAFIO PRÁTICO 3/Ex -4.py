'''4. Uma empresa possui uma lista com os preços de alguns produtos. Antes de apresentar os valores ao cliente, todos os preços precisam receber um acréscimo de 10%. 
 
O programador inicialmente escreveu o código da seguinte maneira: ... 

O código funciona corretamente, mas a equipe deseja torná-lo mais compacto e utilizar List Comprehension. Sua tarefa é reescrever o programa utilizando List Comprehension.'''

precos = [50, 80, 120, 35, 200, 75]
novos_precos = []
for preco in precos:
    novo_preco = preco * 1.10
    novos_precos.append(novo_preco)
print(novos_precos)