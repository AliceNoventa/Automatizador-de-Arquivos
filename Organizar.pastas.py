import os
import shutil
from tkinter.filedialog import askdirectory

# Selecionar a pasta
caminho = askdirectory(title="Selecione uma pasta")
lista_arquivos = os.listdir(caminho)

# Dicionário de arquivos
locais = {
    "Imagens": [".png", ".jpg", ".psd"],
    "Planilhas": [".xlsx", ".csv"],
    "Documentos": [".pdf", ".doc", ".docx"]
}

# Organização e criação de pastas
for arquivo in lista_arquivos:
    # 01. Arquivo.Doc
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            # Criar a pasta se não existir
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            # Mover o arquivo para a pasta correta
            shutil.move(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

