from No import No

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # Inicializa a lista com a cabeça (primeiro nó) vazia

    def inserir_no_inicio(self, valor):
        novo_no = No(valor) # Cria um novo nó com o valor fornecido
        novo_no.proximo = self.cabeca # Faz o novo nó apontar para o antigo primeiro nó
        self.cabeca = novo_no # Atualiza a cabeça da lista para o novo nó

    def inserir_no_final(self, valor):
        novo_no = No(valor)

        # verifica se a lista esta vazia
        if self.cabeca == None:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no

        else:
            no_anterior = self.cabeca
            
            while no_anterior.proximo != None:
                no_anterior = no_anterior.proximo

            no_anterior.proximo = novo_no
            novo_no.proximo = None

    def adicionar_no_depois_encontrar_alvo(self, valor, alvo):

        novo_no = No(valor)
        no = self.cabeca
        encontra = False

        while no != None:
            if no.valor == alvo:
                novo_no.proximo = no.proximo
                no.proximo = novo_no
                encontra = True
                break
            no = no.proximo
            
        if not encontra:
            print(f"O alvo: {alvo} não foi encontrado")

    def remover_no(self, valor):
        no = self.cabeca
        encontra = False

        if no.valor == valor:
            self.cabeca = no.proximo

        else:
            no_anterior = no
            no = no.proximo

        while no != None:
            if no.valor == valor:
                no_anterior.proximo = no.proximo
                encontra = True
                break

            else:
                no_anterior = no
                no = no.proximo

        if not encontra:
            print("O nó não foi encontrado")


    def exibir(self):
        no_atual = self.cabeca
        while no_atual:
            print(no_atual.valor, end=" -> ")
            no_atual = no_atual.proximo
        print("None")  # Indica o final da lista

lista = ListaEncadeada()
lista.inserir_no_inicio(3)
lista.inserir_no_inicio(2)
lista.inserir_no_inicio(1)
lista.remover_no(44)
lista.inserir_no_final(100)
# lista.adicionar_no_depois_encontrar_alvo(44, 1)
lista.exibir()