# Loop for
for i in range(1, 6):
    print(i)

# Percorrendo lista
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)

# Loop for com continue (pula o 5)
for j in range(1, 11):
    if j == 5:
        continue
    print(j)

# Loop for com break (para no 5)
for m in range(1, 11):
    if m == 5:
        break
    print(m)

# Usando continue e break juntos
for n in range(1, 11):
    if n == 5:
        # Pula o número 5
        continue

    if n == 8:
        # Para o loop quando chegar no 8
        break

    print(n)

# Loop while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# Loop com condição de saída
texto = ""
while texto != "sair":
    texto = input("Digite algo (ou 'sair' para parar): ")

# Exemplo de loop infinito com condição de parada
while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta.lower() == "sair":
        break

# Loop com try e except
while True:
    try:
        n = int(input("Digite um número: "))
        print(n)
        break
    except ValueError:
        if input("Tentar novamente? (s/n): ").lower() != "s":
            break