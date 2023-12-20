def calcular_estatisticas_notas(*notas, situacao=False):
    """
    Calcula estatísticas das notas dos alunos.

    Parameters:
    *notas (float): Uma sequência de valores representando as notas dos alunos.
    situacao (bool, optional): Indica se a situação da turma deve ser incluída. Padrão é False.

    Returns:
    dict: Um dicionário contendo a quantidade de notas, a maior nota, a média da turma e a situação (se solicitada).

    Example:
    calcular_estatisticas_notas(7, 8, 6, 5, 9, situacao=True)
    """
    try:
        quantidade_notas = len(notas)
        if quantidade_notas == 0:
            raise ValueError("Nenhuma nota foi fornecida.")

        maior_nota = max(notas)
        media_turma = sum(notas) / quantidade_notas

        resultado = {
            "Quantidade de notas": quantidade_notas,
            "Maior nota": maior_nota,
            "Média da turma": media_turma
        }

        if situacao:
            resultado["Situação"] = "BOA" if media_turma >= 6 else "RUIM"

        return resultado

    except ValueError as e:
        return {"Erro": str(e)}

def receber_notas_do_usuario():
    """
    Solicita ao usuário as notas e opção de incluir situação.

    Returns:
    tuple: Uma tupla contendo as notas fornecidas e a opção de incluir situação.
    """
    try:
        notas_usuario = input("Digite as notas dos alunos separadas por espaço: ").split()
        notas = [float(nota) for nota in notas_usuario]
        
        incluir_situacao = input("Deseja incluir a situação da turma? (S/N): ").upper() == 'S'
        
        return tuple(notas), incluir_situacao

    except ValueError:
        print("Por favor, digite notas válidas.")
        return (), False

def main():
    print("Desafio 0105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:")
    print("- Quantidade de notas.")
    print("- A maior nota.")
    print("- A média da turma.")
    print("- A situação (opcional).")
    print(50 * "-=")

    notas_alunos, incluir_situacao = receber_notas_do_usuario()
    resultado_notas = calcular_estatisticas_notas(*notas_alunos, situacao=incluir_situacao)

    print("\nResultado:")
    for chave, valor in resultado_notas.items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    main()
