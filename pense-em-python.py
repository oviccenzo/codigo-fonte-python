#Capitulo 1: jornada do programa

##1.3 -primeiro programa

print("hello world")

'hello world!'

print('meu nome é viccenzo de oliveira')
print('eu estou cursando o superior chamado ciência da computação')
print('eu sou portador de deficiência audtitiva')
print('eu tenho 23 ano e vou fazer 24 em junho dia 27 desse ano')

##1.4 operadores aritmeticos

40 + 2

43-2

6*7

(6**2) + 6

6 ^ 2

##1.5 - valores e tipos

type(2)

type(42.0)

type('hello world!')

type('2')

type('42.0')

type('hello world!')

type(True)

type(False)

type(229)

type(32*2)

1,000,000,000

2,000,000,000

(222*2,333*2,444*2,555*2,666*2,777*2,888*2,999*2)


###exercicio do capitulo 1

# print('olá)

# print(olá)

# 2++2

# 02

# 5 5

# Capitulo 2: variaveis e tipos

###2.1 instrucao e atribuicao

message = 'and now for something completely different'
n = 17
pi = 3.1415926535897932
print(message)
print(n)
print(pi)

# 76trombones = 'big parede'
#    76trombones = 'big parede'
    #  ^
# SyntaxError: invalid decimal literal

# mora@ = 1000000
          # ^
# SyntaxError: invalid syntax

# class = 'Advanced Theoretical Zymurgy'
#           ^
# SyntaxError: invalid syntax

###2.2 - expressoes e instrucoes

42

n

n + 25

n = 17
print(n)

miles = 26.2
miles * 1.61

miles = 26.2
print(miles * 1.61)

####exemplo do script

print(1)
x = 2
print(x)

print(32)
x = 23
print(x)

####2.2.1-introcoues de atribuicao não produz nenhuma saida

print(5)
x = 5
print(x + 1)

####ordem das operações

expressoes de parentese

2*(3-1)

(1 + 1) ** (5 - 2)

###calcular e gerar o resultado da quantidade de minutos

minuto0 = 20
minutes = (minuto0 * 100) / 60
print(minutes)

minuto1 = 30
minutes = (minuto1 * 100) / 60
print(minutes)

minuto2 = 40
minutes = (minuto2 * 100) / 60
print(minutes)

###exponenciação e a proxima precedencia que possui mais alta da quantidade de numero

import math
int(1 + math.pow (2,3))

###elevar ao cubo + 9

import math
print(int(2 * math.pow(3,2)) )
print(int(2 * math.pow(3,2) + 9))
print(int(2 * math.pow(3,3)))
print(int(2 * math.pow(3,3) + 9))
print(int(2 * math.pow(3,3) + 18))
print(int(2 * math.pow(3,3) + 27))
print(int(2 * math.pow(3,3) + 36))
print(int(2 * math.pow(3,3) + 45))
print(int(2 * math.pow(3,3) + 54))

import math
int(2 * math.pow(3,2))

###multplicação e divisão que tem a alta precedencia do que a adição e da subtração

2*3-1

int(6+4/2)

(6+5/2)

int(6+6/2)

(6+7/2)

int(6+8/2)

###operacoes com strings

# '2'-'1'
# ----> 1 '2'-'1'
# TypeError: unsupported operand type(s) for -: 'str' and 'str'

# 'eggs'/'easy'
# ----> 1 'eggs'/'easy'
# # TypeError: unsupported operand type(s) for /: 'str' and 'str'

# "third" * "a charm"
# ----> 1 "third" * "a charm"
# TypeError: can't multiply sequence by non-int of type 'str'

###mais ha duas expressoes, + e *

first = "throat"
second = "warbler"
first + second

' spam ' * 3

###operador de multiplicacao da string

' spam ' *3

' viccenzo ' * 3

' spam ' + ' spam ' + ' spam ' * 3

print(2**2)
print(3**3)
print(4**4)
print(5**5)
print(6**6)
print(7**7)
print(8**8)
print(9**9)
print(10**10)

2**7

'spam'*3

###comentario da operacoes com a string e operador de matematica + e *

minuto3 = 60
percentage = (minuto3 * 100) / 60 #porcentage de uma hora
# print(int(percentage))

n = 42
n

xy = 1
(xy)

###exercicio do capitulo 2



# Capitulo 3: funcoes

###3.1 - chamada de função

type(42)

# int("hello world")
# ValueError: invalid literal for int() with base 10: 'hello world'

int(3.99999)

int(-2.3)

float(32)

float('3.14159')

str(32)

str(3.14159)

###3.2 funcoes matematica

####primeiro exemplo usa math.log10 para calcular a proporção de sinal ruído decibeis

%%capture
!pip install math

import math

signal_power = 10
noise_power = 20

ratio = signal_power / noise_power
decibel = 10 * math.log10(ratio)
radius = 0.7
height = math.sqrt((radius))

print(f"O valor do decibel é; {decibel}")
print(f"O valor do height é: {height}")

####segundo exemplo encontra o seno de radians.O nome da variável indica sin e outras funções.

import math

degrees1 = 45
radians1 = degrees1 / 180.0 * math.pi
# math.sin(radians1)
print(f"O valor do seno é: {math.sin(radians1)}")

###exercicio do capitulo 3




# Capitulo 4: Estudo de caso: projeto de interface


###4.1 modulo de turtle

%%capture
!pip install ColabTurtle

import ColabTurtle.Turtle as bob


bob.initializeTurtle()
bob.forward(100)
bob.left(90)
bob.forward(200)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(200)
bob.forward(90)
bob.forward(200)
bob.left(90)

%%capture
!pip install ColabTurtle

import ColabTurtle.Turtle as bob

# Inicializa a tela do Turtle no Colab
bob.initializeTurtle()

# Comandos de movimento
bob.forward(100)
bob.left(90)
bob.forward(100)

###4.2 - repetição simples


import ColabTurtle.Turtle as bob

bob.initializeTurtle()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

for i in range(4):
  print("Hello world")

for i in range(4):
  bob.forward(100)
  bob.left(90)

##exercicio do capitulo 4

###4.3 - exercicio
A seguir, uma série de exercícios usando TurtleWorld. Eles servem para divertir, mas
também têm outro objetivo. Enquanto trabalha neles, pense que objetivo pode ser.
As seções seguintes têm as soluções para os exercícios, mas não olhe até que tenha
terminado (ou, pelo menos, tentado).
1. Escreva uma função chamada square que receba um parâmetro chamado t, que é um
turtle. Ela deve usar o turtle para desenhar um quadrado.
Escreva uma chamada de função que passe bob como um argumento para o square e
então execute o programa novamente.
2. Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o
comprimento dos lados seja length e então altere a chamada da função para fornecer
um segundo argumento. Execute o programa novamente. Teste o seu programa com
uma variedade de valores para length.
3. Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro
chamado n e altere o corpo para que desenhe um polígono regular de n lados.
Dica: os ângulos exteriores de um polígono regular de n lados são 360/n graus.
4. Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e
desenhe um círculo aproximado ao chamar polygon com um comprimento e número
de lados adequados. Teste a sua função com uma série de valores de r.Dica: descubra a circunferência do círculo e certifique-se de que length * n =
circumference.
5. Faça uma versão mais geral do circle chamada arc, que receba um parâmetro
adicional de angle, para determinar qual fração do círculo deve ser desenhada. angle
está em unidades de graus, então quando angle=360, o arc deve desenhar um círculo
completo.

#Exercicio 1

#Exercicio 2

#Exercicio 3

#Exercicio 4

#Exercicio 5

#Capitulo 5: Condicionais e recursividade

def print_n(s,n):
  if n <= 0:
    return
  print(s)
  # print_n(s,n-1) 

resultado1 = print_n('viccenzo',2)

###exercicio do capitulo 5

#exercicio 5.1:
import time

time.time()

#exercicio 5.2:


#exercicio 5.4:
def recurse(n,s):
  if n == 0:
    print(s)
  else:
    recurse(n-1,n+2)
recurse(3,0)

%%capture
!pip install ColabTurtle
import ColabTurtle.Turtle as bob

#exercicio 5.6:
def draw(t,length,n):
  if n == 0:
    return
  angle = 50
  t.forward(length*n)
  t.left(angle)
  draw(t,length,n-1)
  t.right(2*angle)
  draw(t,length,n-1)

bob.initializeTurtle() # Initialize the turtle display
resultado4 = draw(bob,5,5)

# Capitulo 6 Funções com resultado

#####A função que gera o retorno do valor

radius1 = 2
radians2 = 3

e = math.exp(1.0)
height1 = radius1 * math.sin(radians2)
print(e)
print(height1)

#####calcular o valor da funcao da area

def area(radius2 ):
  a = math.pi * radius2 ** 2
  return a
  print(a)


print(area(10))
print(area(11))
print(area(12))
print(area(13))
print(area(14))

#####é a mesma coisa só que usa o return que calcular direto o que eu quero dizer que é a mesma só que possui o mesmo resultado do programa anterior que usa a = math.pi * radius2 ** 2 e depois usa o return

def area1(radius4):
  return math.pi * radius4 ** 2

print(area1(10)) 

####Calcular o valor absoluto do retorno

def absolute_value(x):
  if x < 0:
    return -x
  else:
    return x

print(absolute_value(0))
print(absolute_value(1))
print(absolute_value(-1))

####calcular o valor absoluto do retorno

def absolute_value1(x1):
  if x1 < 0:
    return -x1
  if x1 > 0:
    return x1

print(absolute_value1(0))
print(absolute_value1(1))

####valor absoluto é none

absolute_value2 = None
print(absolute_value2) 

####calcular a distancia

def distance(x1,y1,x2,y2):
  return 0.0

print(f"A distancia eh: {distance(1,2,3,4)} cm")

####calcular distancia e encontra a diferença x2 - x1 e y2 - y1

def distance1(x1,y1,x2,y2):
  dx = x2 - x1
  dy = y2 - y1
  print(f"A diferenca de x eh: {dx}")
  print(f"A diferenca de y eh: {dy}")
  return 0.0

print(distance1(4,2,6,8))

# Capitulo 7: Iteração

# Capitulo 8: Strings


# Capitulo 9 estudos de caso: jogos de palavras

# Capitulo 10: Lista

# Capitulo 11: Dicionarios

# Capitulo 12: Tuplas

# Capitulo 13: estudos de caso: selecao de estrutura de dados

# Capitulo 14: arquivos

# Capitulos 15: Classes e objetos

# Capitulo 16: Classes e funcoes

# Capitulo 17: Classes e metodos

# Capitulo 18: Herança

# Capitulo 19: Extra

#capitulo 20:


#capitulo 21:

#nova secao:

numeros = [1,2,3,4,5,6,7,8,9]
numeros1 = [10,11,12,13,14,15,16,17,18]
resultado = []
x = 3

for numero in numeros:
  resultado.append(numero * x)

for numero1 in numeros1:
  resultado.append(numero1 * x)

print(resultado)

minute = float(input("Digite qualquer numero minuto: "))

porcentagem = (minute * 100) / 60 #% minute

print(f"A porcentagem de minuto eh: {porcentagem:.4f} %")
