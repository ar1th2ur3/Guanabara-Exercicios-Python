import pygame

def reproduzir_musica(caminho_audio, loop=False):
    pygame.init()
    pygame.mixer.init()

    # Carrega o arquivo de áudio
    pygame.mixer.music.load(caminho_audio)

    # Reproduz o arquivo de áudio de acordo com a opção de loop
    if loop:
        pygame.mixer.music.play(-1)  # -1 reproduz em loop
    else:
        pygame.mixer.music.play()

    # Mantém o programa rodando até que a música termine ou o usuário pressione uma tecla
    while pygame.mixer.music.get_busy():
        if input("Pressione qualquer tecla para interromper a reprodução: "):
            pygame.mixer.music.stop()
            break

def main():
    print("Reprodução de Música com Opção de Loop")

    # Caminho do arquivo de áudio (ajuste o caminho conforme necessário)
    caminho_audio = r"C:\Users\art_h\OneDrive\Documentos\Study\Youtube\Tecnologia\Programação\Python\Curso em Vídeo\Curso Python #08 - Utilizando Módulos\for-elevator-jazz-music-124005.mp3"

    # Solicita ao usuário a opção de loop
    loop_option = input("Reproduzir em loop? (S/N): ").strip().lower()

    if loop_option == 's':
        reproduzir_musica(caminho_audio, loop=True)
    else:
        reproduzir_musica(caminho_audio)

if __name__ == "__main__":
    main()
