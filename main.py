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

    entropia_geral = id3.entropia_geral
    perspectiva_ensolarado_entropia, perspectiva_nublado_entropia, perspeciva_chuvoso_entropia = id3.entropia_perpectiva(
        ["Ensolarado", "Nublado", "Chuvoso"])
    temperatura_quente_entropia, temperatura_moderada_entropia, temperatura_fresca_entropia = id3.entropia_temperatura(
        ["Quente", "Moderada", "Fresca"])
    umidade_alta_entropia, umidade_normal_entropia = id3.entropia_umidade(["Alta", "Normal"])
    vento_forte_entropia, vento_fraco_entropia = id3.entropia_vento(["Forte", "Fraco"])

    ganho_p = id3.ganho([perspectiva_ensolarado_entropia, perspectiva_nublado_entropia, perspeciva_chuvoso_entropia])
    ganho_t = id3.ganho([temperatura_quente_entropia, temperatura_moderada_entropia, temperatura_fresca_entropia])
    ganho_u = id3.ganho([umidade_alta_entropia, umidade_normal_entropia])
    ganho_v = id3.ganho([vento_forte_entropia, vento_fraco_entropia])

#  ganho_p = ganho(entropia_geral, 14, [(perspectiva_ensolarado_entropia, 5), (perspectiva_nublado_entropia, 4),
#                                       (perspeciva_chuvoso_entropia, 5)])
# ganho_t = ganho(entropia_geral, 14, [(perspectiva_ensolarado_entropia, 5), (perspectiva_nublado_entropia, 4),
#                                     (perspeciva_chuvoso_entropia, 5)])
# ganho_u = ganho(entropia_geral, 14, [(perspectiva_ensolarado_entropia, 5), (perspectiva_nublado_entropia, 4),
#                                     (perspeciva_chuvoso_entropia, 5)])
# ganho_v = ganho(entropia_geral, 14, [(perspectiva_ensolarado_entropia, 5), (perspectiva_nublado_entropia, 4),
#                                    (perspeciva_chuvoso_entropia, 5)])

# max(ganho_p, ganho_t, ganho_v, ganho_u)
