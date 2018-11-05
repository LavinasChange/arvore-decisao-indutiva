from Dia import Dia
from ID3 import ID3
from Elemento_ID3 import ElementoID3


def gerar_objetos():
    texto = open("data.txt").read()
    linhas = texto.replace(' ', '').splitlines()
    objetos = ID3()
    for linha in linhas:
        objetos.dias.append(Dia(linha.split(',')))
    return objetos


def eh_folha(lista):
    for x in lista:
        if max(x) == (0, 0):
            return True
    return False


def treinamento(filtros=None):
    if filtros is None:
        filtros = ['']

    id3.filtrar_dias_por_atributo(filtros)
    entropia_perspectiva = id3.entropia_por_coluna(id3.buscar_arestas_das_colunas(1), 1)
    entropia_temperatura = id3.entropia_por_coluna(id3.buscar_arestas_das_colunas(2), 2)
    entropia_umidade = id3.entropia_por_coluna(id3.buscar_arestas_das_colunas(3), 3)
    entropia_vento = id3.entropia_por_coluna(id3.buscar_arestas_das_colunas(4), 4)

    ganho_perspectiva = id3.ganho(entropia_perspectiva), "1"
    ganho_temperatura = id3.ganho(entropia_temperatura), "2"
    ganho_umidade = id3.ganho(entropia_umidade), "3"
    ganho_vento = id3.ganho(entropia_vento), "4"
    valor_coluna_treinada, coluna_treinada = id3.raiz_arvore(
        [ganho_perspectiva, ganho_temperatura, ganho_vento, ganho_umidade])

    return coluna_treinada


def col_to_str(num_coluna):
    num_coluna = int(num_coluna)
    if num_coluna == 1:
        return "Perspeciva"
    if num_coluna == 2:
        return "Temperatura"
    if num_coluna == 3:
        return "Humidade"
    if num_coluna == 4:
        return "Vento"


if __name__ == '__main__':
    id3 = gerar_objetos()
    nivel_arvore = 0

    historico = ['']
    coluna = treinamento(historico)
    arestas = id3.arestas(coluna)
    lista_id3 = []
    for x in arestas:
        lista_id3.insert(0, ElementoID3(x, historico, col_to_str(coluna), nivel_arvore))

    # Solucionar para cada aresta manter seu historico de arestas
    aux = []

    while lista_id3:
        elemento = lista_id3.pop()
        coluna = treinamento(elemento.historico_aresas)
        arestas = id3.arestas(coluna)

        for x in arestas:
            aux.insert(0, ElementoID3(x, elemento.historico_aresas, col_to_str(coluna), nivel_arvore))

        print(elemento.nivel_arvore, elemento.historico_aresas, elemento.nome_coluna)

        if not lista_id3:
            lista_id3 = aux
            aux = []
            nivel_arvore += 1
