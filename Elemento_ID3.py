class ElementoID3:

    def __init__(self, aresta, historico_arestas, nome_coluna, nivel_arvore, eh_folha):
        self.aresta = aresta
        self.historico_aresas = historico_arestas + [self.aresta]
        self.nome_coluna = nome_coluna
        self.nivel_arvore = nivel_arvore
        self.eh_folha = eh_folha
