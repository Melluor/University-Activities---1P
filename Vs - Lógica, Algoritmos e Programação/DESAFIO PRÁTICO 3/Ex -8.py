# 8. Um sistema precisa verificar se uma senha atende a uma regra básica de segurança. Crie uma função que receba uma senha e retorne: True se a senha possuir pelo menos 8 caracteres; False caso contrário.
# Desafio: modifique a função para exigir também que a senha contenha pelo menos um número.
senha = input("Digite a senha: ")

def seguranca(senha: str) -> bool:
    if len(senha) >= 8:
        print("Senha autorizada.")
        return True
    else:
        print("Senha não autorizada.")
        return False
seguranca(senha)