from Dia import Dia
from ID3 import ID3


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


def treinamento(filtro=''):
    id3.filtrar_dias_por_atributo(filtro)
    entropia_perspectiva = id3.entropia_por_coluna(id3.buscar_arestas_das_colunas(1), 1)
    entropia_temperatura = id3.entropia_por_coluna(id3.buscar_arestas_das_colunas(2), 2)
    entropia_umidade = id3.entropia_por_coluna(id3.buscar_arestas_das_colunas(3), 3)
    entropia_vento = id3.entropia_por_coluna(id3.buscar_arestas_das_colunas(4), 4)

    folha = eh_folha([entropia_perspectiva, entropia_temperatura, entropia_umidade, entropia_vento])

    valor_coluna_treinada =  coluna_treinada = 0
    if not folha:
        ganho_perspectiva = id3.ganho(entropia_perspectiva), "1"
        ganho_temperatura = id3.ganho(entropia_temperatura), "2"
        ganho_umidade = id3.ganho(entropia_umidade), "3"
        ganho_vento = id3.ganho(entropia_vento), "4"
        valor_coluna_treinada, coluna_treinada = id3.raiz_arvore([ganho_perspectiva, ganho_temperatura, ganho_vento, ganho_umidade])

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

    coluna = treinamento()
    arestas = id3.arestas(coluna)

    aux = []
    while arestas:
        coluna = treinamento(arestas.pop())
        novas_arestas = id3.arestas(coluna)

        print(col_to_str(coluna))
        print(novas_arestas)
        for x in novas_arestas:
            aux.append(x)

        if not arestas:
            arestas = aux
            aux = []
