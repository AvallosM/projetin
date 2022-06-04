#Função que ira calcular a media de um usuario e dizer se ele tera que fazer a AF
from random import randint
def questao1():

    n1 = (float(input("Digite a nota 1:")))
    n2 = (float(input("Digite a nota 2:")))

    media = (n1+n2)/2

    if(4<= media <7):
        print("Terá que fazer AF")
        print("Uma AF depois")
        af=(float(input("Digite a nota da AF:")))
        media = (media+af)/2
    else:
        print("Parabens voce passou")
    print(f"A média é igual a {media}")


#programa que identifica qual dos dois numeros são maiores
def questao2():
    n1 = (int(input("primeiro numero:")))
    n2 = (int(input("segundo numero:")))

    if(n1 > n2):
        print(f"{n1} > {n2}")
    elif (n1 == n2):
        print("numeros iguais")
    else:
        print(f"{n1} < {n2}")


#questão 2 programa que diz  se o número é par ou ímpar
def questao3():
    numero = int(input("digite um numero:"))
    resto = numero % 2

    if(resto == 0):
        print("O numero é par")
    else:
        print("O numero é impar")

#questão 3 informa se o numero 1 é multiplo do numero dois ou não
def questao4():
    n1 = int(input("Digite um numero:"))
    n2 = int(input("Digite outro numero:"))

    resultado = n1 % n2
    #int(resutado)

    if(resultado == 0):
        print(f"{n1} é multiplo de {n2}")
    else:
        print("Não são multiplos")

def questao5(): # Mostrara todos os numeros inteiros ate o numero que foi digitado
    n = int(input("Digite um numero:"))

    for i in range(0, n, 1):  # (inicio, final, passos)
        print(i + 1)

def questao6(): #tabuada de multiplicação do número dígitado
    n = int(input("digite um numero:"))

    for i in range(1, 10, 1):
        print(f"{n}x{i}={n * i}")

def questao7(): #o programa ira pedir o comprimento de 3 retas e dizer se elas podem formar um triangulo compativel
    n1 = int(input("Primeiro numero:"))
    n2 = int(input("Segundo numero:"))
    n3 = int(input("Terceiro numero:"))

    if n1 + n2 < n3:
        print("Não pode ser um triangulo")
    elif n2 + n3 < n1:
        print("Não pode ser um triangulo")
    elif n3 + n1 < n2:
        print("Não pode ser um triangulo")
    else:
        print("Triangulo compativel")

def questao8(): #O programa em questão ira pedir do usuario uma velocidade, se ultrapassar 80Km/h ira mostrar
# dizendo que ele foi multado, a multa custa R$7,00 por cada Km acima do limite
    v = int(input("Qual a velocidade do carro?"))
    if v > 80:
        print(f"Você foi multado em {(v % 80) * 7} reais")
    else:
        print("Você não foi multado")

def questao9():#O programa ira calcular o preço de uma passagem, cobrando R$0.50 por Km para viagens de 200Km
               # e R$0,45 por viagens mais longas
    d = int(input("Qual a distancia da viagem?"))
    if d <= 200:
        print(d * 0.50)
    elif d > 200:
        print(d * 0.45)

def questao10(): #O programa ira dizer se o ano digitado é bissexto
    ano = int(input("digite um ano:"))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é bissexto")
    else:
        print("não é bissexto")

def questao07(): #o programa ira pedir o comprimento de 3 retas e dizer se elas podem formar um triangulo compativel
    n1 = int(input("Primeiro numero:"))
    n2 = int(input("Segundo numero:"))
    n3 = int(input("Terceiro numero:"))

    if n1 + n2 < n3:
        print("Não pode ser um triangulo")
    elif n2 + n3 < n1:
        print("Não pode ser um triangulo")
    elif n3 + n1 < n2:
        print("Não pode ser um triangulo")
    else:
        print("Triangulo compativel")


'''
def questao11(): #O programa ira selecionar aleatoriamente um numero entre 1 e 5 se o usuario acertar o numero ele ganha
    n = int(input("digite um numero entre 1 e 5:"))
    x = randint(1, 5)
    if x == n:
        print("Parebens! voce acertou")
    else:
        print("O computador venceu!")
print (x)

def questao12():#programa que diz o tipo primitivo e informaçoes sobre o que for digitado
n = input('Digete algo:')
print ('Classe:',type(n))
print ('É numero?', n.isnumeric())
print ('É letra?', n.isalpha())
print ('É letras com numeros?', n.isalnum())
'''


#Código principal
q = int(input("Qual questão vc deseja executar?"))

if(q == 1):
    questao1()
elif(q == 2):
    questao2()
elif(q == 3):
    questao3()
elif(q == 4):
    questao4()
elif(q == 5):
    questao5()
elif(q == 6):
    questao6()
elif(q == 7):
    questao7()
elif(q == 8):
    questao8()
elif(q == 9):
    questao9()
elif(q == 10):
    questao10()
#elif(q == 11):
    #questao11()
#elif(q == 12):
 #   questao12()
else:
    print("essa questão não existe")




