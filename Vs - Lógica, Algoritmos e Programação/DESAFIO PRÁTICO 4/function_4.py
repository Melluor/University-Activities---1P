from re import search

def verificar_senha(senha: str):
    erros = [] # Armazena os erros.

    if len(senha) < 8: # Verifica se o tamanho é 8 ou maior.
        erros.append("Caracteres Insuficientes.")

    if not search(r"[A-Z]", senha): # Verifica se tem letra maiúscula.
        erros.append("Quantidade de letras maiúsculas na senha insuficientes.")

    if not search(r"[0-9]", senha): # Verifica se tem número.
        erros.append("Quantidade de números na senha insuficientes.")

    return erros