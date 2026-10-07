import random

def gerar_senha_numerica(caracteres):
    senha = ""
    for _ in range(caracteres):
        numero = str(random.randint(0, 9))
        senha += numero
    return senha

senha_um = gerar_senha_numerica(8)
senha_dois = gerar_senha_numerica(8)

print(f"Senha 1: {senha_um}")
print(f"Senha 2: {senha_dois}")