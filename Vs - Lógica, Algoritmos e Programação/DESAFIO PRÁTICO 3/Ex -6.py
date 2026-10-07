'''6. Um sistema de cadastro precisa calcular a idade de uma pessoa a partir do seu ano de nascimento e do ano atual. Para isso você deve criar uma função. A função deve receber os dois anos e retornar a idade da pessoa. Desafio: faça o programa informar se a pessoa é:  menor de idade; maior de idade.'''
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento

def maioridade(idade: int) -> str:
    if idade < 18:
        return "Você é menor de idade."
    else:
        return "Você é maior de idade."

print(f"Você tem {idade} anos. Resultado: {maioridade(idade)}")