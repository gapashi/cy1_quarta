# TUPLAS
dias_da_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
print(dias_da_semana)

# CONJUNTOS
compras = ["macarrão", "molho", "azeite", "alho", "molho"]
compras_unicas = set(compras)
# comprasUnicas

for item in compras_unicas:
    print(f"COMPRAR: {item}")

# DICIONÁRIOS
produto = {
    "nome": "Teclado",
    "preço": 150.0,
    "estoque": 5
}

if produto["estoque"] > 0:
    print(f"O produto {produto['nome']} está disponível por R${produto['preço']}")