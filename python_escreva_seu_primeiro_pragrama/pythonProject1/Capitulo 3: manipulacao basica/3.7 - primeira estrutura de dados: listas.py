####3.7 - primeiro estrutura de dados: listas

lista = [1,2,3,4,5]
print(lista)

lista1 = ["salario","imposto",'renda per capita','banco do brasil']
print(lista1)

lista2 = [1, "salario",2,'imposto',3,'renda per capita',4,'banco do brasil']
print(lista2)

lista4 = [[1,2,3], "salario" ,10]
print(lista4)

lista5 = [1,2]
print(lista5)

####Sequencia de lista em python ou seja podemos perguntar seu tamanho e acessar elementos por indices ou trechos

lista =["impostos","salarios","altos","baixos"]
print(lista[0] , lista[1] , lista[2] , lista[3])

####lista são mutaveis

lista = ["impostos","salarios","altos","baixos"]
(lista[0] ,lista[1] ,lista[2], lista[3])

####ifs e listas

lista = []

if lista:
  print("Nunca sou executado")
else:
  print("Sempre sou executado")