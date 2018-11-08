from math import log2
from typing import List

from Dia import Dia


class ID3:

    def __init__(self):
        self.dias: List[Dia] = []
        self.backup: List[Dia] = self.dias

    @staticmethod
    def entropia(positivo, total):
        diferenca = total - positivo
        if diferenca == 0 or diferenca == total:
            return 0, total

        a = positivo / total
        b = diferenca / total
        return - a * log2(a) - b * log2(b), total

    def entropia_simp(self, lista):
        return self.entropia(self.soma_ultimo_parametro(lista), len(lista))

    def ganho(self, lista_entropia):
        soma = 0
        for entropia_item in lista_entropia:
            soma += entropia_item[0] * entropia_item[1] / self.num_objetos
        return self.entropia_geral[0] - soma

    @staticmethod
    def soma_ultimo_parametro(lista):
        return sum(x.parametros[-1] == 'FernandoHaddad' for x in lista)

    @property
    def num_objetos(self):
        return len(self.dias)

    @property
    def entropia_geral(self):
        return self.entropia(self.soma_ultimo_parametro(self.dias), self.num_objetos)

    def entropia_by_coluna(self, nomes, coluna):
        saida = []
        for item in nomes:
            lista = []
            for x in self.dias:

                if x.parametros[coluna] == item:
                    lista.append(x)
            saida.append(self.entropia_simp(lista))
        return saida

    def entropia_por_coluna(self, nomes, coluna):
        return self.entropia_by_coluna(nomes, coluna)

    @staticmethod
    def raiz_arvore(lista_ganhos):
        return max(lista_ganhos)

    def arestas(self, coluna):
        ultima_coluna = [x.parametros[int(-1)] for x in self.dias]
        for x in ultima_coluna:
            if x != ultima_coluna[0]:
                return self.unique([x.parametros[int(coluna)] for x in self.dias]), False

        return [ultima_coluna[0]], True

    @staticmethod
    def unique(lista):
        lista = list(set(lista))
        lista.sort()
        return lista

    def filtrar_dias_por_atributo(self, arestas):
        if arestas == ['']:
            self.dias = self.backup
            return

        self.dias = []
        for x in self.backup:
            if all(elem in x.parametros for elem in arestas):
                self.dias.append(x)

    def buscar_arestas_das_colunas(self, posicao):
        lista = []
        for x in self.dias:
            lista.append(x.parametros[posicao])
        return self.unique(lista)

    @property
    def num_colunas(self):
        return len(self.backup[0].parametros)

    def buscar_folha(self, coluna):
        ultima_coluna = [x.parametros[int(-1)] for x in self.dias]
        return ultima_coluna[0]
