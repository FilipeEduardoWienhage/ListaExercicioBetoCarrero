import os
import shutil


def organizarPorExtensao():
    diretorio = "C:/Users/filip/Documents/GitHub/ListaExercicioBetoCarrero/praserorganizado"

    arquivos = os.listdir(diretorio)

    for arquivo in arquivos:
        caminhoCompleto = os.path.join(diretorio, arquivo)

        if os.path.isfile(caminhoCompleto):
            partes = arquivo.split('.')

            if len(partes) > 1:
                extensao = partes[-1]
            else:
                continue

            pasta_destino = os.path.join(diretorio, extensao)

            os.makedirs(pasta_destino, exist_ok=True)

            shutil.move(caminhoCompleto, os.path.join(pasta_destino, arquivo))

            print(f"Movido: {arquivo} para {pasta_destino}")


organizarPorExtensao()