#calculos
num1 = input('Informe o primeiro número: ') 
num2 = input('Informe o segundo número: ') 

soma = int(num1) + int(num2)
subtracao = int(num1) - int(num2)
divisao = int(num1) / int(num2)
moduloresto = int(num1) % int(num2)
multiplicacao = int(num1) * int(num2)
potenciacao = int(num1) ** int(num2)

print(soma)
print(subtracao)
print(divisao)
print(moduloresto)
print(multiplicacao)
print(potenciacao)

# o comando type retorna o tipo da variável 
print(type(num1)) 
print(type(soma))

#Calcular área
lado1 = input('Informe o primeiro lado: ') 
lado2 = input('Informe o segundo lado: ') 

# o metódo isnumeric valida se uma variável é um numero inteiro  
print('Lado1 é numerico?' , lado1.isnumeric()) 
print('Lado2 é numerico?' , lado2.isdecimal()) 

area = float(lado1) * float(lado2) 
print('A area do quadrado é: {} ' . format(area))

nomecompleto = input('Informe o seu nome completo: ')
#Função LEN retorno a quantidade de caracteres de uma variável
print('1. Quantidade de caracteres:', len(nomecompleto))


# Metodos Utilizados
# Upper = Transforma um texto em maiusculo
# Lower = Transforma um texto em minusculo
# Capitalize = Somente a primeira letra em maiusculo

print ('2. Nome em maiusculo:' , nomecompleto.upper())
print ('3. Nome em minusculo:' , nomecompleto.lower())
print ('4. Primeira letra em maiusculo:' , nomecompleto.capitalize())

