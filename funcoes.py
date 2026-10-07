# print() | len() | max()

def boas_vindas(nomeDeUsuario, idDoUsuario):
    print(f"Boas-vindas {nomeDeUsuario} ID: {idDoUsuario}!")

print(boas_vindas("Fulano", 123))

# argumentos nomeados
def velocidade(tempo, distancia=100):
    print(distancia/tempo)

print(velocidade(10))

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(celsius_para_fahrenheit(30))


def membros_familia(nome, sobrenome="Silva"):
    print(f"Boas vindas à {nome} {sobrenome}")

membros_familia("Fulano")
membros_familia("Cicrano")