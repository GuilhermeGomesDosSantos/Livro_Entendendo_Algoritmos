# Buscar o nome "Maria": Dada uma lista de nomes em ordem alfabética ["Ana", "Bruno", "Carlos", "Maria", "Paula", "Thiago"], encontre o índice de "Maria"

def pesquisa_binaria_nome(lista, target):

    indice_inicial = 0
    indice_maximo = len(lista) - 1

    while indice_inicial <= indice_maximo:
        
        meio = (indice_maximo + indice_inicial) // 2

        if lista[meio] == target:
            return meio
        
        elif lista[meio] > target:
            indice_maximo = meio - 1

        else:
            indice_inicial = meio + 1

    return f"None - Indice do usuário {target} não encontrado"

print(pesquisa_binaria_nome(["Ana", "Bruno", "Carlos", "Maria", "Paula", "Thiago"], "Gui"))