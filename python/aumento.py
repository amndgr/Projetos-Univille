salario = float(input("Digite o salario: "))
p_aumento = float(input("digite a porcentagem de aumento: "))
aumento = salario * p_aumento / 100
novo_salario = salario + aumento
print("é igual a um aumento de R$ %7.2f" % aumento)
print("Um aumento de %5.2f%% em um salario de R$ %7.2f" % (p_aumento, salario))
print("Resultao em um novo salário de R$ %7.2f" % novo_salario)