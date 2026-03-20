valor_emp = float(input("Digite o valor do empréstimo: "))
num_parc = int(input("Digite o número de parcelas: "))
salario = float(input("Digite o valor do salário do solicitante: "))

parcelas = valor_emp / num_parc

if parcelas > (salario * 0.3):
    print("Empréstimo negado. O valor da parcela excede 30% do salário.")
else:
    print("Empréstimo aprovado. O valor da parcela é de %5.2f." % parcelas)

