# 4. Essa questão você deve criar seu próprio módulo, ou seja, a questão deverá ter dois arquivos, 1 para o módulo e outro para o código principal. Imagine que você trabalhe na parte de Cibersegurança de uma empresa e precise testar se as senhas criadas pelos usuários estão no padrão da empresa. O seu módulo deverá ter uma função que verifique as senhas pelos critérios:
# ●  Pelo menos 8 caracteres;
# ●  Contém pelo menos uma letra maiúscula;
# ●  Contém pelo menos um número;
# ●  Caso os critérios não sejam seguidos, informar ao usuário.
# Dica: utilize no seu módulo a biblioteca re.
from function_4 import verificar_senha

print(" == VERIFICADOR DE SENHAS ==")
senha_valida = False

while True:
    senha = input("Informe a senha para ser checada: ")
    erros = verificar_senha(senha)

    if len(erros) > 0: # Usa a quantidade de erros armazenados como True ou False.
        print("\nSenha não autorizada! A senha não segue suficientemente os padrões da empresa.")
        for erro in enumerate(erros, start=1):
            print(f"{erro}")
        continue

    senha_valida = True

    if senha_valida == True:
        print("A senha digitada segue os padrões da empresa. Senha autorizada!")
        break