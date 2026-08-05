# frutas = ["maça", "banana", "uva"]
# print (frutas)

# #ver primeiro elemento da lista
# print (frutas[0])

# #retornando demais elementos no seu index
# print(frutas[1])
# print (frutas[2])

# #modificando
# frutas[1] = "laranja"
# print (frutas)

# #adicionando itens
# frutas.append("pera")
# print (frutas)

# #adicionar no começo da lista
# frutas.insert(0, "abacaxi")
# print (frutas)

# #removendo itens
# frutas.remove("uva")
# print(frutas)

#tamanho da lista
numeros = [1,2,4,3]
print (len(numeros))

#ordenar
numeros.sort()
print(numeros)

#inverter
numeros.reverse()
print(numeros)

#verificar se existe
print(5 in numeros)
print(2 in numeros)

#adicionando vários elementos
numeros = numeros + [10,20,30] 
print(numeros)

#percorrer com for
for n in numeros:
    print(n)
