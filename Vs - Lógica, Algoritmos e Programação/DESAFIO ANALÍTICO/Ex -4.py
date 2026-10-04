# === 4. Faça um programa que percorra duas listas, A e B, e gere uma terceira sem elementos repetidos. ===

'''A = ['Python', 'Java', 'C', 'PHP', 'JavaScript', 'Dart']
B = ['C++', 'Python', 'Java', 'Julia', 'Go', 'JavaScript']
C = []
# Lista Correta = ['Python', 'Java', 'C', 'PHP', 'JavaScrip', 'Dart', 'C++', 'Julia', 'Go']

for index in A:
    if index not in B:
        C.append(index)
for i in B:
    if i not in C:
        C.append(i)
print(C)'''