salario = float(input("Digite o seu salário: "))

if salario <= 128_000:
    valor_do_aumento = salario * 0.20
    novo_salario = salario + valor_do_aumento
elif 280_000 <= salario <= 700_000:
    valor_do_aumento = salario * 0.15
    novo_salario = salario + valor_do_aumento
elif 700_000 <= salario <= 1_500_000:
    valor_do_aumento = salario * 0.10
    novo_salario = salario + valor_do_aumento
else:
    valor_do_aumento = salario * 0.05
    novo_salario = salario + valor_do_aumento
    
print("Salário antes do reajuste:", salario)
print("Percentual aplicado:", (valor_do_aumento / salario) * 100, "%")
print("Valor do aumento:", valor_do_aumento)
print("Novo salário apos o aumento:", novo_salario)
