####3.6 - loops com while

salario7 = float(input("Salario? "))
imposto7 = 27.
while imposto7 > 0:
  imposto7 = (input("Imposto ou (0) para sair: "))
  if not imposto7:
    imposto7 = 27.
  else:
    imposto7 = float(imposto7)
  print("Valor real: {0} ".format(salario7 - (salario7 * (imposto7 * 0.01))))

print("\n")

####o loop pode ser interrompido com um comando o break que é quebrar linha

salario8 = float(input("Salario? ")) #esse linha falar para digitar qualquer valor do salario
imposto8 = 27 #esse imposto tem o valor de 27
while imposto8 > 0:
  imposto8 = input("Imposto ou (s) para sair: ")
  if not imposto8:
    imposto = 27.
  elif imposto8 == 's':
    break
  else:
    imposto8 = float(imposto8)
  print("Valor real: {0} ".format(salario8 - (salario8 * (imposto8 * 0.01))))