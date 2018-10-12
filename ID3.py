from math import log2
from typing import List

from Dia import Dia


class ID3:

    def __init__(self):
        self.dias: List[Dia] = []

    @staticmethod
    def entropia(positivo, total):
        diferenca = total - positivo
        if diferenca == 0 or diferenca == total:
            return 0

        a = positivo / total
        b = diferenca / total
        return - a * log2(a) - b * log2(b)

    def entropia_simp(self, lista):
        soma = self.soma_jogar_tenis(lista)
        return self.entropia(soma, len(lista))

    @staticmethod
    def ganho(geral, total_itens, lista_entropia):
        soma = 0
        for entropia_item in lista_entropia:
            soma += entropia_item[0] * entropia_item[1] / total_itens
        return geral - soma

    @staticmethod
    def soma_jogar_tenis(lista):
        return sum(x.jogarTenis == 'Sim' for x in lista)

    @property
    def tamanho(self):
        return len(self.dias)

    @property
    def entropia_geral(self):
        soma = self.soma_jogar_tenis(self.dias)
        return self.entropia(soma, self.tamanho)

    @property
    def entropia_perpectiva(self):
        ensolarado_str = "Ensolarado"
        nublado_str = "Nublado"
        chuvoso_str = "Chuvoso"

        ensolarado = []
        nublado = []
        chuvoso = []

        for x in self.dias:
            if x.perspectiva == ensolarado_str:
                ensolarado.append(x)

            if x.perspectiva == nublado_str:
                nublado.append(x)

            if x.perspectiva == chuvoso_str:
                chuvoso.append(x)

        entropia_ensolarado = self.entropia_simp(ensolarado)
        entropia_nublado = self.entropia_simp(nublado)
        entropia_chuvoso = self.entropia_simp(chuvoso)

        return entropia_ensolarado, entropia_nublado, entropia_chuvoso
