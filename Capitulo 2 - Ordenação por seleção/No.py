# Classe Nó representa cada elemento da lista encadeada
class No:
    def __init__(self, valor):
        self.valor = valor  # Armazena o valor do nó
        self.proximo = None  # Inicialmente, não aponta para nenhum próximo nó
