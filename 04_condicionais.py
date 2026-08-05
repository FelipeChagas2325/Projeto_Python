#condicionais
numero = int(input('Informe o número: '))
 
resultado = int(numero % 2)
print('Se o resultado for 0 é par e se for 1 é impar, o resultado é :', resultado)
 
input('Digite ENTER para continuar')
if resultado == 0:
    resultado = 'o numero é par'
else:
    resultado = 'o resultado é impar'
print(resultado)    
 
 
input('Digite Enter para continuar')
from os import system, name
system('cls') if(name == 'nt') else system('clear')
 
# entrada da nota
nota = float (input('Digite a nota do estudante: ' ))


# Verificação da situação
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print ("Recuperação")
else:
    print("Reprovado")