from time import sleep
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
import io
import sys

def obter_comando():
    """
    Solicita ao usuário um comando para obter ajuda.

    Returns:
    str: O comando fornecido pelo usuário.
    """
    return input("Digite o comando para obter ajuda (ou 'FIM' para encerrar): ")

def exibir_manual(comando):
    """
    Exibe o manual de um comando usando o Interactive Help do Python.

    Parameters:
    comando (str): O comando para o qual obter ajuda.
    """
    # Redireciona a saída padrão para um buffer
    buffer = io.StringIO()
    sys.stdout = buffer
    help(comando)
    sys.stdout = sys.__stdout__  # Restaura a saída padrão

    # Obtém o conteúdo do buffer e destaca
    formatted_code = highlight(buffer.getvalue(), PythonLexer(), TerminalFormatter())
    print(formatted_code)

def encerrar_programa():
    """Encerra o programa."""
    print("Encerrando o programa. Até logo!")

def main():
    print("Desafio 0106: Faça um mini-sistema que utilize o Interactive Help do Python.")
    print("O usuário vai digitar o comando e o manual vai aparecer.")
    print("Quando o usuário digitar a palavra FIM, o programa se encerrará.")
    print(50 * "-=")

    while True:
        comando = obter_comando()

        if comando.upper() == 'FIM':
            encerrar_programa()
            break

        try:
            exibir_manual(comando)
        except NameError as e:
            print(f"Erro: Comando '{comando}' não reconhecido. Certifique-se de que está digitando um comando válido.")

        sleep(1)

if __name__ == "__main__":
    main()
