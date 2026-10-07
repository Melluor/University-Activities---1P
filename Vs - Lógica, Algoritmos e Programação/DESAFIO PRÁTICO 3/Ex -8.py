# 8. Um sistema precisa verificar se uma senha atende a uma regra básica de segurança. Crie uma função que receba uma senha e retorne: True se a senha possuir pelo menos 8 caracteres; False caso contrário.
# Desafio: modifique a função para exigir também que a senha contenha pelo menos um número.
def senha_valida(senha: str) -> bool:
    return len(senha) >= 8 and any(carac.isdigit() for carac in senha)

def validacao() -> bool:
    if senha_valida(senha):
        print("Autorizada.")
        return True
    else:
        print("Não autorizada.")
        return False

senha = input("Digite a senha: ")

senha_valida(senha)
validacao()