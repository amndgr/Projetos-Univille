def salario_liquido(valor_hora, horas, desconto_inss_pct):
    salario_bruto = valor_hora * horas
    desconto_inss = salario_bruto * desconto_inss_pct / 100
    return {
        'salario_bruto': salario_bruto,
        'desconto_inss': desconto_inss,
        'salario_liquido': salario_bruto - desconto_inss,
    }
