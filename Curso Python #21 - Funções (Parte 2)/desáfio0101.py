

print("Desáfio 0101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.")

from datetime import datetime

currentYear = datetime.now().year

def voto(anoNascimento):
    idade = currentYear - anoNascimento
    if 18 <= idade <= 65:
        return f"Com {idade} anos, você precisa se alistar."
    elif idade >65:
        return f"Com {idade} anos, o voto é opcional."
    else:
        return f"Com {idade} anos, você ainda não precisa se alistar"

ano = int(input("Qual o seu ano de nascimento ? "))

print(voto(ano))



