# Faça um programa que peça dois
# números e imprima o maior deles.

def maior_numero():
    numero1 = int(input("Digite um número inteiro: "))
    numero2 = int(input("Digite outro número inteiro: "))

    if numero1 > numero2:
        print(f"{numero1} é maior que {numero2}")
    else:
        print(f"{numero2} é maior que {numero1}")

maior_numero()