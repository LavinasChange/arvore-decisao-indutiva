class ArvoreID3:

    def __init__(self, no, arestas, eh_raiz=False):
        self.no = no
        self.eh_folha = False
        self.eh_raiz = eh_raiz
        self.arestas: [] = arestas

        if not arestas:
            self.eh_folha = True
