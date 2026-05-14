#python iniciante

print('Ola python')
print("ola python"," versao ", 3.4)
print("ola python"," versao ", 3.4,".Esse e meu ",1,"teste")
x = 3.75
print(type(x))
y = int(x)
print(dir(type))
print(100 / 2)

dois_x = 39
_dois = 39
idade_joao = 30

idade_joao = 30
x_dois = 30
print(5 + 2 * 3)
print((5 + 2) * 3)
print(3 + 5 * 4 ** 2)
print(((3 + 5) * 4) ** 2)

#calcular qualquer numero usando a formula de baskhara

import cmath

a = float(input("coeficiente de a: "))
b = float(input("coeficiente de b: "))
c = float(input("coeficiente de c: "))

# Calculando o delta
delta = b**2 - 4 * a * c

# Usando cmath.sqrt para suportar números complexos (quando delta < 0)
x1 = (-b + cmath.sqrt(delta)) / (2 * a)
x2 = (-b - cmath.sqrt(delta)) / (2 * a)

print("As raizes da equacao x1 e: ", x1)
print("As raizes da equacao x2 e: ", x2)

#Comando de repetição e comando condicional

####calcular e informa a distancia e depois calcular a distancia percorrida e informa o valor por distancia

distancia = float(input("Informe a distancia por favor: "))
valor = 4

if 0 <= distancia <= 3:
  valor += (distancia * 0.5)
elif 3 < distancia <= 6:
  valor += (distancia * 0.75)
elif distancia > 6:
  valor += (distancia * 1)
print(f"Informe a distancia percorrida: {distancia}")
print(f"Informe a valor a ser pago: {valor}")

####divide o numero qualquer

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

for n in range(num1, num2):
  if ( n % 15 == 0 ):
    print(n)

####calcular a quantidade de numeros maiore que 10

x1 = 21

num1 = float(input("digite sua nota: "))
if num1 > 10:
    x1 = x1 + 1

num2 = float(input("digite a sua nota: "))
if num2 > 10:
    x1 = x1 + 1

num3 = float(input("digite a sua nota: "))
if num3 > 10:
    x1 = x1 + 1


print("quantidade de numeros maiores que 10: ",x1)


####calcular quantidade de comprar e diferente de zero

produto = 7
valor = 2

while(produto >= 0 and produto <= 20):
  produto = int(input("Calcular há quantidade de compra e diferente de 0: "))
  valor = valor * produto
  print("Valor total: ", valor)

####calcular qualquer numero de permutação

import math

for i in range(1,10):
  num = int(input("Calcular qualquer numero: "))
  permutacao = math.perm(num)
  num += permutacao
  print("Permutacao: ", permutacao)
  # print('Numero : ',num)

####calcular a temperatura celsiu

for c in range(32,40):
  print(c, " = ", (c * 1.8) + 32)

####calcular qualquer numero de permutacao

import math

for i in range(1,10):
  num = int(input("Digite um numero: "))
  perm = math.perm(num)
  print(f"A permutacao: {perm}")

####calcular a temperatura newton

for n in range(32,81):
    print(n," = ",(9 * n / 5) + 32)


####numero aleatorio

for a in range(31,90):
    print(a)


####calcular a tabuada de 1 a 10

num = int(input("Digite o numero 1 a 10: "))

for i in range(20,302):
    print(i, ' + ' , num , ' = ', i + num)


####Calcular a media aritmetica:

n = 4
soma = 0
for contador in range(1, n + 1):
  a = int(input('Digite um valor: '))
  soma = soma + a
  print(soma)

####calcular tres nota

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("Media: ",media)

if(media >= 10):
  print("aprovado")
elif(media < 10 and media > 10):
  print("recuperacao")
else:
  print("reprovado")

####calcular quantidade de voto

print("Quantidade total de voto para cada candidato")
print("1 - candidato 1")
print("2 - candidato 2")
print("3 - candidato 3")
print("4 - candidato 4")
print("5 - nulo")
print("6 - branco")
print("0 - sair")

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0

voto = int(input("Digite seu voto: "))

while(voto > 0):
    if (voto == 1):
        candidato1 = candidato1 + 1
    elif (voto == 2):
        candidato2 = candidato2 + 1
    elif (voto == 3):
        candidato3 = candidato3 + 1
    elif (voto == 4):
        candidato4 = candidato4 + 1
    elif (voto == 5):
        nulo = nulo + 1
    elif (voto == 6):
        branco = branco + 1
    else:
        print("Voto inválido. Por favor, digite 1, 2, 3, 4, 5, 6 ou 0 para sair.")
    voto = int(input("Digite seu voto: "))

print("Total de votos para cada candidato: ")
print("Candidato1: ",candidato1)
print("Candidato2: ",candidato2)
print("Candidato3: ",candidato3)
print("Candidato4: ",candidato4)
print("Nulo: ",nulo)
print("Branco: ",branco)


####dividi qualquer numero

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

for n in range(num1, num2):
  if ( n % 7 == 0 ):
    print(n)

####contador de numero

numA = int(input("Digite o primeiro numero: "))
numB = int(input("Digite o segundo numero: "))

contador = numA + 12
resultado = numA

while contador < numB:
  resultado = resultado * contador
  contador += 2

print(f"Resultado {resultado}")
