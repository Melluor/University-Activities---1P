# === 2. Observe o código a seguir e analise as questões pedidas. ===

'''L = [1, 2, 3, 8, 9, 10, 11, 12]
x = 0
while x < 3:
    print(L[x])
    x += 1'''

# A -> Resposta: Mostrará os valores "1, 2 , 3".

# B -> Resposta: Sim, já que a lista suporta 3 elementos e foi mostrado somente 3 elementos.

# C -> Resposta: Aumentaria o tamanho da lista e seus valores armazenados, mas não mostraria todos os elementos por conta da condição while ser somente "menor que 3".

# D -> Código reescrito:
'''L = [1, 2, 3, 8, 9, 10, 11, 12]
for x in L:
    print(x)'''