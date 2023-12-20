import pygame

# Inicialize o pygame
pygame.init()

# Caminho do arquivo de áudio (ajuste o caminho conforme necessário)
caminho_audio = r"C:\Users\art_h\OneDrive\Documentos\Study\Youtube\Tecnologia\Programação\Python\Curso em Vídeo\Curso Python #08 - Utilizando Módulos\for-elevator-jazz-music-124005.mp3"

# Carregue o arquivo de áudio
pygame.mixer.music.load(caminho_audio)

# Reproduza o arquivo de áudio
pygame.mixer.music.play()

# Mantenha o programa rodando até que a música termine
while pygame.mixer.music.get_busy():
    pass
