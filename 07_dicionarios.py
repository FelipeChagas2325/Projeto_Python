# pessoa = {

#     "nome": "Felipe",
#     "idade": 37
# }

# print(pessoa)
# print(pessoa["nome"])

# #alterando valores
# pessoa["idade"] = 37
# print(pessoa)

# #adicionando novo dado
# pessoa["cidade"] = "São Paulo"
# print (pessoa)

# #removendo 
# del pessoa ["idade"]
# print(pessoa)

pessoaNova = {

    "primeironome": "Marta",
    "idade": 70
}
#ver chavaes
print (pessoaNova.keys())

#ver valores
print(pessoaNova.values())

#ver chave e valor
print(pessoaNova.items())

#verificar se chave existe
print ("primeironome" in pessoaNova)
print ("nome" in pessoaNova)

#usar get
print(pessoaNova.get("primeironome"))

#percorrer
for chave, valor in pessoaNova.items():
    print(chave, ".", valor)