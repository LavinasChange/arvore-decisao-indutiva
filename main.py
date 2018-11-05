from Dia import Dia
from ID3 import ID3
from Elemento_ID3 import ElementoID3


def gerar_objetos():
    global cabecalho

    linhas = open("data.txt").read().replace(' ', '').splitlines()
    objetos = ID3()

    cabecalho = linhas.pop(0).split(',')
    for linha in linhas:
        objetos.dias.append(Dia(linha.split(',')))

    return objetos


def treinamento(filtros=None):
    if filtros is None:
        filtros = ['']
    id3.filtrar_dias_por_atributo(filtros)
    ganhos = []

    ultima = 1
    for coluna in range(id3.num_colunas - ultima):
        entropia = id3.entropia_por_coluna(id3.buscar_arestas_das_colunas(coluna), coluna)
        print(entropia)
        ganho = id3.ganho(entropia), str(coluna)
        ganhos.append(ganho)

    valor_coluna_treinada, coluna_treinada = id3.raiz_arvore(ganhos)

    return coluna_treinada


def col_to_str(num_coluna):
    global cabecalho
    return cabecalho[int(num_coluna)]


if __name__ == '__main__':
    id3 = gerar_objetos()
    nivel_arvore = 0

    historico = ['']
    coluna = treinamento(historico)
    arestas = id3.arestas(coluna)
    lista_id3 = []
    for x in arestas:
        lista_id3.insert(0, ElementoID3(x, historico, col_to_str(coluna), nivel_arvore))

    ultimo_nivel = []
    aux = []
    nivel_arvore += 1
    while lista_id3:
        elemento = lista_id3.pop()
        coluna = treinamento(elemento.historico_aresas)
        arestas = id3.arestas(coluna)

        for x in arestas:
            aux.insert(0, ElementoID3(x, elemento.historico_aresas, col_to_str(coluna), nivel_arvore))

        #print('Nível', elemento.nivel_arvore, elemento.nome_coluna, elemento.historico_aresas)

        if not lista_id3:
            lista_id3 = aux.copy()
            if aux:
                ultimo_nivel = aux.copy()
            aux = []
            nivel_arvore += 1

    print()

    f = ['Ensolarado', 'Alta']
    x = treinamento(f)

    for x in ultimo_nivel:
        print(x.nome_coluna,x.historico_aresas)
