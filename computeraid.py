from emoji import emojize
from time import sleep

mensagem = "Somos a Code Academy: Girls"

print('\033[1;31m*' * 60)
print(mensagem.center(60))
print('*' * 60, "\n")

print("\033[1;34mFormador: João Santos\n")

alunas = [
    "Ana da Costa",
    "Elmira Maurício",
    "Kiesse Canza",
    "Romila Rangel",
    "Samba Bento",
    "Vandra de Almeida",
    "Telma Pascoal"
]

print("Alunas:")
for i, aluna in enumerate(alunas):
    sleep(1.8)
    print(f"\033[1;33m\t{i + 1}ª - ", aluna)

print("\n", "💖", "\033[1;34mComputeraid\033[m", "💖")
print("\033[1;32mObrigado pela doação dos computadores.")
print("Estamos muito felizes pela oportunidade de aprender a programar em Python. 💋💋💋💋💋💋💋")
