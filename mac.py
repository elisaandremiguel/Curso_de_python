"""
1. Escreva um script que peça 5 notas de avaliação contínua ao usuário, em seguida calcule o MAC - Média de Avaliação Contínua e se o valor for superior a 14.00 informe o bom desempenho do estudante se não informe que o estudante precisa se dedicar mais.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
nota5 = float(input("Digite a quinta nota: "))

mac = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if mac > 14:
    print("Aluno (a):", round(mac, 2), "tem um bom desempenho")
else:
    print("Aluno (a):", round(mac, 2), "tem um mal desempenho")
