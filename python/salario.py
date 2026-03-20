gH = float(input("Digite quanto você ganha por hora: "))
hT = float(input("Digite o número de horas trabalhadas: "))

salarioB = gH * hT

ir = salarioB * 0.11
inss = salarioB * 0.08
sindicato = salarioB * 0.05

VT = ir + inss + sindicato

salarioL = salarioB - VT

print("Valor do IR:", ir)
print("Valor do INSS:", inss)
print("Valor do Sindicato:", sindicato)
print("Salário Líquido:", salarioL)