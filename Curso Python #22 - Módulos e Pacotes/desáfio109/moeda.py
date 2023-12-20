def aumentar(v, percentual,formatar=True):
    aumento = (percentual / 100) * v
    novo_valor_aumentar = v + aumento
    if formatar:
        if novo_valor_aumentar < 0:
            vFormatado = "-R$" + format(abs(novo_valor_aumentar), ",.2f")
        else:
            vFormatado = "R$" + format(novo_valor_aumentar, ",.2f")
        return vFormatado
    return novo_valor_aumentar

def diminuir(v, percentual,formatar=True):
    diminuir = (percentual / 100) * v
    novo_valor_diminuir = v - diminuir
    if formatar:
        if novo_valor_diminuir < 0:
            vFormatado = "-R$" + format(abs(novo_valor_diminuir), ",.2f")
        else:
            vFormatado = "R$" + format(novo_valor_diminuir, ",.2f")
        return vFormatado
    return novo_valor_diminuir

def dobro(v, formatar=True):
    dobro = v * 2
    if formatar:
        if dobro < 0:
            vFormatado = "-R$" + format(abs(dobro), ",.2f")
        else:
            vFormatado = "R$" + format(dobro, ",.2f")
        return vFormatado
    else:
        return dobro

def metade(v,formatar=True):
    metade = v / 2
    if formatar:
        if metade < 0:
            vFormatado = "-R$" + format(abs(metade), ",.2f")
        else:
            vFormatado = "R$" + format(metade, ",.2f")
        return vFormatado
    return metade

def moeda(v,formatar=True):
    if v < 0:
        vFormatado = "-R$" + format(abs(v), ",.2f")
    else:
        vFormatado = "R$" + format(v, ",.2f")
    return vFormatado
