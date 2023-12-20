print("Desafio 0105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:")
print("- Quantidade de notas.")
print("- A maior nota.")
print("- A média da turma.")
print("- A situação (opcional).")
print(50 * "-=")

def notas(*notas, sit=False):
    """
    Calcula a estatística das notas dos alunos.

    Parameters:
    *notas (float): Uma sequência de valores representando as notas dos alunos.
    sit (bool, optional): Indica se a situação da turma deve ser incluída. Padrão é False.

    Returns:
    dict: Um dicionário contendo a quantidade de notas, a maior nota, a média da turma e a situação (se solicitada).

    Example:
    notas(7, 8, 6, 5, 9, sit=True)
    """
    quantidade_notas = len(notas)
    maior_nota = max(notas)
    media_turma = sum(notas) / quantidade_notas

    resultado = {
        "Quantidade de notas": quantidade_notas,
        "Maior nota": maior_nota,
        "Média da turma": media_turma
    }

    if sit:
        resultado["Situação"] = "BOA" if media_turma >= 6 else "RUIM"

    return resultado

resultado_notas = notas(7, 8, 6, 5, 9, sit=False)
print(resultado_notas)
