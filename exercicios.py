# EX 1: Crie uma função chamada: 
# verificar_idade / verificarIdade
# que recebe a idade de uma pessoa. 
# Se a idade for MAIOR que 18,
# print("Maior de idade")
# Caso contrário, print("Menor de idade")

def verificar_idade(idade):
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

verificar_idade(30)
verificar_idade(15)