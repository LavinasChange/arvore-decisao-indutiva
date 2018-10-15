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
    entropia_perspectiva = id3.entropia_perpectiva(["Ensolarado", "Nublado", "Chuvoso"])
    entropia_temperatura = id3.entropia_temperatura(["Quente", "Moderada", "Fresca"])
    entropia_umidade = id3.entropia_umidade(["Alta", "Normal"])
    entropia_vento = id3.entropia_vento(["Forte", "Fraco"])

    folha = eh_folha([entropia_perspectiva, entropia_temperatura, entropia_umidade, entropia_vento])
    print('folha', folha)

    raiz_valor, raiz = 0, 0
    if not folha:
        ganho_perspectiva = id3.ganho(entropia_perspectiva), "Perspectiva"
        ganho_temperatura = id3.ganho(entropia_temperatura), "Temperatura"
        ganho_umidade = id3.ganho(entropia_umidade), "Umidade"
        ganho_vento = id3.ganho(entropia_vento), "Vento"
        raiz_valor, raiz = id3.raiz_arvore([ganho_perspectiva, ganho_temperatura, ganho_vento, ganho_umidade])

    return raiz_valor, raiz


if __name__ == '__main__':
    id3 = gerar_objetos()

    no_valor, no = treinamento()
    arestas = id3.arestas(no)
    print("Nó =>", no, "|Arestas =>", arestas)

    print("Escolhido aresta", arestas[1])

    no_valor, no = treinamento(arestas[1])
    arestas = id3.arestas(no)
    print("Nó =>", no, "| Arestas =>", arestas)

    # print("Escolhido aresta", arestas[1])
    no_valor, no = treinamento(arestas[1])

    arestas = id3.arestas(no)
    print(no_valor, no)
#    for aresta in arestas:
#    treinamento(aresta)
