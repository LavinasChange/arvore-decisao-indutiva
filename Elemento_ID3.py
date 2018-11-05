class ElementoID3:

    def __init__(self, aresta, historico_arestas, nome_coluna, nivel_arvore):
        self.aresta = aresta
        self.historico_aresas = historico_arestas + [aresta]
        self.nome_coluna = nome_coluna
        self.nivel_arvore = nivel_arvore
