import os 
from tkinter.filedialog import askdirectory

# A função askdirectory retorna o deretório da pasta selecionada
caminho = askdirectory(title="Seleciona uma pasta")

# Lista dos arquivos dentro da pasta selecionada
lista_arquivos = os.listdir(caminho)

# Pastas a serem criadas para guardar os arquivos da pasta selecionada
locais = {
    "imagens": [".png", ".jpg"],
    "documentos": [".docx"],
    "pdfs": [".pdf"]
}

# A variável arquivo recebe os arquivo recebidos da pasta selecionada
for arquivo in lista_arquivos:
    # A função splitext é utilizada para separar o caminho do arquivo da sua extensão(.pdf, .png, .docx, etc)
    # nome recebe o caminho do arquivo | extensão recebe a extensão do arquivo
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")

    # pasta recebe as chaves do dicionário "locais"
    for pasta in locais:

        # O IF compara o arquivo com os tipos de dados da pasta definida do dicionário locais(imagens, documentos ou pdfs)
        if extensao in locais[pasta]:

            # Se a pasta não existir o código irá criar a pasta
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")

            # Move os arquivos do diretório anterior para a pasta determinada
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
