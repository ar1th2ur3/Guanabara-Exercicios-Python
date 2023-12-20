from time import sleep
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
import io
import sys

print("Desafio 0106: Faça um mini-sistema que utilize o Interactive Help do Python.")
print("O usuário vai digitar o comando e o manual vai aparecer")
print("Quando o usuário digitar a palavra FIM, o programa se encerrará.")

def meu_help(comando):
    # Redireciona a saída padrão para um buffer
    buffer = io.StringIO()
    sys.stdout = buffer
    help(comando)
    sys.stdout = sys.__stdout__  # Restaura a saída padrão

    # Obtém o conteúdo do buffer e destaca
    formatted_code = highlight(buffer.getvalue(), PythonLexer(), TerminalFormatter())
    print(formatted_code)

while True:
    palavra = str(input("O que você gostaria de saber? "))
    
    if palavra.upper() == 'FIM':
        print("Encerrando o programa. Até logo!")
        break
    
    sleep(1)
    meu_help(palavra)
