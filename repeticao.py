# for: percorre itens em uma sequência
# e retorna os dados desses itens

# while: repete uma estrutura de código
# enquanto uma determinada condição for
# verdadeira

# numeros = list(range(1, 1000))
# resultados = []

# for numero in numeros:
#     resultados.append(numero * 2)
#     #print(numero * 2)
# print(resultados)

# for numeros in range(1, 11):
#     if(numeros %2 == 1):
#         print(numeros)

# while condição:
#     executar bloco de código

# soma = 0
# numeros = range(1, 1000)
# i = 0

# while soma < 100:
#     soma += numeros[i]
#     i += 1
# print(soma)

# x = 0
# while x < 5:
#     print("Valor de X: ", x)
#     print("X ainda é menor que 5, some 1")
#     x += 1
# else:
#     print("FIM")

# soma = 0
# x = 0

# while x < 1000:
#     x += 1
#     if x %3 == 0:
#         print(x)
#         soma += x
#     else:
#         if x %5 == 0:
#             pass
#         else:
#             print("buscando...")
#             continue

#     if soma > 300:
#         print(soma)
#         break

numero = int(input("Digite um número de 1 a 10: "))

if 1 <= numero <= 10:
    print("Tabuada do número: ", numero)
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")
else:
    print("Número inválido! Digite um número de 1 a 10.")