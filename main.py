from Dia import Dia
from ID3 import ID3


def gerar_objetos():
    texto = open("data.txt").read()
    linhas = texto.replace(' ', '').splitlines()
    objetos = ID3()
    for linha in linhas:
        objetos.dias.append(Dia(linha.split(',')))
    return objetos


if __name__ == '__main__':
    id3 = gerar_objetos()

    ganho_perspectiva = id3.ganho(id3.entropia_perpectiva(["Ensolarado", "Nublado", "Chuvoso"])), "Perspectiva"
    ganho_temperatura = id3.ganho(id3.entropia_temperatura(["Quente", "Moderada", "Fresca"])), "Temperatura"
    ganho_umidade = id3.ganho(id3.entropia_umidade(["Alta", "Normal"])), "Umidade"
    ganho_vento = id3.ganho(id3.entropia_vento(["Forte", "Fraco"])), "Vento"

    raiz = id3.raiz_arvore([ganho_perspectiva, ganho_temperatura, ganho_vento, ganho_umidade])
    print(raiz)

    arestas_raiz = id3.arestas(raiz[1])

    print(arestas_raiz)
