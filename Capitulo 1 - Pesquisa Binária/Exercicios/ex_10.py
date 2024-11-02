# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def busca_indice(lista):

    valor_menor = 0
    lista_ordenada = sorted(lista)
    valor_maximo = len(lista_ordenada) - 1

    print(lista_ordenada)
    while valor_menor <= valor_maximo:

        meio = (valor_menor + valor_maximo) // 2

        if lista_ordenada[meio] == meio:
            valor_menor = meio + 1

        else:
            valor_maximo = meio - 1

    return valor_menor    

print(busca_indice([3,0,1]))
print(busca_indice([0,1]))
print(busca_indice([0, 1, 2, 3, 4, 5, 6, 7, 9]))