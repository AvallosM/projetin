
from random import randint
def desafio1():  #sera jogado um jogo em que sera sorteado um numero aleatorio e vc tem que acertar
    n = int(input("digite um numero entre 1 e 5:"))
    x = randint(1, 5)
    if x == n:
        print("Parebens! voce acertou")
    else:
        print("O computador venceu!")

    print(x)

def desafio2():  #sera checado se o usuario foi multado, caso seja ira mostrar em quanto foi, de acordo com a velocidade
    v = int(input("Qual a velocidade do carro?"))
    if v > 80:
        print(f"Você foi multado em {(v % 80) * 7} reais")
    else:
        print("Você não foi multado")

def desafio3():  #ira checar se o numero é par ou impar
    n = int(input("digite um numero:"))

    if n % 2 == 0:
        print("O numero é par")
    else:
        print("O numero é impar!")

def desafio4():  #ira calcular o valor de uma passagem de acordo com a distancia
    d = int(input("Qual a distancia da viagem?"))
    if d <= 200:
        print(d * 0.50)
    elif d > 200:
        print(d * 0.45)

def desafio5():  #ira checar se o ano é bissexto
    ano = int(input("digite um ano:"))
    if ano%4==0 and ano%100 != 0 or ano%400 == 0 :
        print(f"O ano {ano} é bissexto")
    else:
        print("não é bissexto")

def desafio6():  #função recebe 3 valores e fala se esses valores pode formar um triangulo
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


def desafio7():  #/leia dois numeros e diga a soma entre eles

    n1 = int(input('Digite um numero:'))
    n2 = int(input('Deigite outro numero:'))
    s = n1 + n2
    print(f'A soma é {s}')

def desafio8(): #programa que diga o tipo primitivo e informaçoes sobre ele

    n = input('Digete algo:')
    print ('Classe:',type(n))
    print ('É numero?', n.isnumeric())
    print ('É letra?', n.isalpha())
    print ('É letras com numeros?', n.isalnum())


q = int(input("Qual desafio vc deseja executar?"))

if(q == 1):
    desafio1()
elif(q == 2):
    desafio2()
elif(q == 3):
    desafio3()
elif(q == 4):
    desafio4()
elif(q == 5):
    desafio5()
elif(q == 6):
    desafio6()
elif(q == 7):
    desafio7()
elif(q == 8):
    desafio8()
else:
    print("Desafio inexistente")



