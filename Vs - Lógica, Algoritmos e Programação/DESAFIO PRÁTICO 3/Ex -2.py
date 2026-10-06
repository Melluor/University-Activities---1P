'''2. Uma caixa contém: ...
Considerando que uma bola será escolhida ao acaso, crie um programa que: 
A)  conte quantas bolas existem na caixa; 
B)  conte quantas são vermelhas; 
C)  calcule a probabilidade de escolher uma bola vermelha; 
D)  apresente a probabilidade em forma de fração e porcentagem.'''
bolas = ["vermelha", "azul", "verde", "vermelha", "amarela", "azul", "vermelha", "verde", "azul", "vermelha"]

red_balls = 0
for ball in bolas:
    if ball == 'vermelha':
        red_balls += 1

print(f"QUANTIDADE DE BOLAS: {len(bolas)}") # A
print(f"QUANTIDADE BOLAS VERMELHAS: {red_balls}") # B
print(f"PROBABILIDADE DE SER UMA BOLA VERMELHA: {red_balls}/{len(bolas)} ou {(red_balls / len(bolas)) * 100}%") #C e D