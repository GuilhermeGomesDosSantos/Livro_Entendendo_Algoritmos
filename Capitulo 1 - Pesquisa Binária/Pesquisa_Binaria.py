# baixo e alto acompanham a parte da lista que você está procurando.
# Enquanto ainda não conseguiu chegar a um único elemento...
#… verica o elemento central.
# Acha o item.
# O chute foi muito alto.
# O chute foi muito baixo.
# O item não existe.
# Vamos testá-lo!
# Lembre-se, as listas começam no 0. O próximo endereço tem índice 1.
# “None” signica nulo em Python. Ele indica que o item não foi encontrado

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
    
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None
    
minha_lista = [1, 3, 5, 7, 9]
print (pesquisa_binaria(minha_lista, 3))
print (pesquisa_binaria(minha_lista, -1))