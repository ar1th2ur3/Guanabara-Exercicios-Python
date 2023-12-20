def calcularMedia(notas):
    if len(notas) == 0:
        return "Não é possível calcular a média, pois nenhuma nota foi fornecida."
    
    media = sum(notas) / len(notas)

    if media < 5:
        return "REPROVADO"
    elif 5 <= media < 7:
        return "RECUPERAÇÃO"
    else:
        return "APROVADO"

def analisarNotas(notas):
    if len(notas) == 0:
        return "Nenhuma nota foi fornecida."

    media = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)

    mensagem = f"Análise das notas:\n"
    mensagem += f"Notas: {', '.join(map(str, notas))}\n"
    mensagem += f"Número de notas: {len(notas)}\n"
    mensagem += f"Média: {media:.2f}\n"
    mensagem += f"Nota Máxima: {nota_maxima}\n"
    mensagem += f"Nota Mínima: {nota_minima}\n"
    mensagem += f"Situação: {calcularMedia(notas)}"

    return mensagem

def main():
    print("Bem-vindo ao sistema de análise de notas.")
    print("Este programa permite calcular a situação do aluno com base em suas notas.")
    
    notas = []
    while True:
        try:
            nota = float(input("Digite uma nota (ou digite 0 para calcular a média e encerrar): "))
            if nota == 0:
                break
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. As notas devem estar no intervalo de 0 a 10.")
        except ValueError:
            print("Erro: Insira uma nota válida.")

    mensagem = analisarNotas(notas)
    print(mensagem)

if __name__ == "__main__":
    main()
