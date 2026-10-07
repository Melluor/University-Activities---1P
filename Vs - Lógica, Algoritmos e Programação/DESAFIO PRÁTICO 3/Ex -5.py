'''5. Um estacionamento cobra seus clientes de acordo com o tempo que o veículo permaneceu no local: Tempo de permanência  Valor 
Até 1 hora          R$ 5,00
De 1 a 3 horas      R$ 10,00
De 3 a 5 horas      R$ 15,00
Mais de 5 horas     R$ 20,00

Crie um código (principal) que receba as informações relevantes para a situação. Crie uma função para o cálculo do valor final do estacioamento.'''
tempo = int(input("Tempo estacionado (Em minutos): "))

def valor_estacionamento(tempo: int) -> str:
    if tempo <= 60:
        return "Taxa de permanência: R$ 5,00"
    elif tempo <= 180:
        return "Taxa de permanência: R$ 10,00"
    elif tempo <= 300:
        return "Taxa de permanência: R$ 15,00"
    else:
        return "Taxa de permanência: R$ 20,00"

print("== VALOR PARA TEMPO DE ESTACIONAMENTO == ")
print(f"TEMPO ESTACIONADO: {tempo} minutos. | VALOR: {valor_estacionamento(tempo)}")