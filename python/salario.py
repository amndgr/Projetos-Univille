# entrada de dados
gH = float(input("Digite quanto você ganha por hora: "))
hT = float(input("Digite o número de horas trabalhadas: "))

# salário bruto
salarioB = gH * hT

# descontos
ir = salarioB * 0.11
inss = salarioB * 0.08
sindicato = salarioB * 0.05

# soma dos descontos
VT = ir + inss + sindicato

# salário líquido
salarioL = salarioB - VT

# saída
print("Valor do IR:", ir)
print("Valor do INSS:", inss)
print("Valor do Sindicato:", sindicato)
print("Salário Líquido:", salarioL)