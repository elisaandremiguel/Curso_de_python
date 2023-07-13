"""
1. Escreva um script que peça que o usuário informe o seu salário bruto mensal e calcule.
    O ganho bruto anual.
    O aumento de 20% se o salário bruto mensal for superior a 50.000,00 Kz 
"""

salario_bruto_mensal = float(input("Informe seu salário bruto mensal: "))
ganho_bruto_anual = salario_bruto_mensal * 12
salario_bruto_mensal_final = 0
if salario_bruto_mensal > 50_000:
    aumento_salarial = salario_bruto_mensal * (20 / 100)
    salario_bruto_mensal_final = salario_bruto_mensal + aumento_salarial

print("Salário bruto anual:", ganho_bruto_anual, "Kz")
print("Salário bruto mensal final:", salario_bruto_mensal_final, "Kz")