from math import log2

from Dia import Dia
from ID3 import ID3


def entropia(positivo, total):
    diferenca = total - positivo
    if diferenca == 0 or diferenca == total:
        return 0

    a = positivo / total
    b = diferenca / total
    return - a * log2(a) - b * log2(b)


def ganho(geral, total_itens, lista_entropia):
    soma = 0
    for entropia_item in lista_entropia:
        soma += entropia_item[0] * entropia_item[1] / total_itens
    return geral - soma


def import_txt():
    texto = open("data.txt").read()
    linhas = texto.replace(' ', '').splitlines()
    objetos = ID3()
    for linha in linhas:
        objetos.dias.append(Dia(linha.split(',')))
    return objetos


if __name__ == '__main__':
    id3 = import_txt()

    ganho_p = id3.ganho(id3.entropia_perpectiva(["Ensolarado", "Nublado", "Chuvoso"]))
    ganho_t = id3.ganho(id3.entropia_temperatura(["Quente", "Moderada", "Fresca"]))
    ganho_u = id3.ganho(id3.entropia_umidade(["Alta", "Normal"]))
    ganho_v = id3.ganho(id3.entropia_vento(["Forte", "Fraco"]))

    print(ganho_p, ganho_t, ganho_u, ganho_v)

    max(ganho_p, ganho_t, ganho_v, ganho_u)
