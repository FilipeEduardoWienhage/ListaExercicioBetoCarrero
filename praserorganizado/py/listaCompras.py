import random
import csv


def geradorListaCompras():
    listaItens = ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Óleo', 'Leite', 'Café', 'Frango', 'Carne', 'Peixe']

    listaCompras = random.sample(listaItens, 5)

    return listaCompras

def salvar_lista_csv(listaCompras, nome_arquivo="lista_compras.csv"):
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)

        for item in listaCompras:
            writer.writerow([item])


def criarListaAleatoria():
    listaCompras = geradorListaCompras()
    
    salvar_lista_csv(listaCompras)


criarListaAleatoria()