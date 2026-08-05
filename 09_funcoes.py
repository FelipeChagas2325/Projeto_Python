#Função.

def saudacao():
    print("Olá, tudo bem?")

#Acessando a função.
saudacao()


#Função com parâmetro.
def saudacao (nome):
    print ("Olá,", nome)

saudacao("Felipe")  

#Função de retorno.
def soma(a,b):
    return a+b
resultado = soma(5, 3)
print(resultado)

#Exemplo com tratamento de erro.
try:
    numero = int(input("Digite um número: "))
    print(numero)
except:
    print("Você digitou algo inválido!")    

#Try e except usando Else e Finally.
try:
    numero = float(input('Digite um número: '))
except ValueError:
  print ('Erro: Entrada Inválida: ')   
else:
    print('Você digitou:', numero)
finally:
    print('Programa finalizada') 

#Exemplo de função com try e except.

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"

print(dividir(10, 2))
print(dividir(10, 0))

#Entrada do usuário.

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
print(dividir(a, b))




