def aumentar(v, percentual):
    aumento = (percentual / 100) * v
    novo_valor_aumentar = v + aumento
    return novo_valor_aumentar
def diminuir(v, percentual):
    diminuir = (percentual / 100) * v
    novo_valor_diminuir = v - diminuir
    return novo_valor_diminuir

def dobro(v):
    dobro = v * 2
    return dobro

def metade(v):
    metade = v / 2
    return metade

def moeda(v):
    if v < 0:
        vFormatado = "-R$" + format(abs(v), ",.2f")
    else:
        vFormatado = "R$" + format(v, ",.2f")
    return vFormatado
