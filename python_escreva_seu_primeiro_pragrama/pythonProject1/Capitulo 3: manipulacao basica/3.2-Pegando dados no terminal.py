####3.2-Pegando dados no terminal

salario = int(input("Digite o salário: "))
imposto = float(input("Imposto em % (exemplo: 27.5)? "))
print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))
