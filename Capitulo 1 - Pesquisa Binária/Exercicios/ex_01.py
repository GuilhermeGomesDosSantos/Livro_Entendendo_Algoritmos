# Input:  nums[] = [0, 1, 2, 6, 9, 11, 15]Output: The smallest missing element is 3
# Input:  nums[] = [1, 2, 3, 4, 6, 9, 11, 15]Output: The smallest missing element is 0
# Input:  nums[] = [0, 1, 2, 3, 4, 5, 6]Output: The smallest missing element is 7 

def encontrar_menor_indice_faltante(lista):
    valor_menor = 0
    valor_maior = len(lista) - 1

    while valor_menor <= valor_maior:
        meio = (valor_menor + valor_maior) // 2
        valor = lista[meio]

        if lista[meio] == meio:
            valor_menor = meio + 1

        else:
            valor_maior = meio - 1
    
    return valor_menor

print(encontrar_menor_indice_faltante([0, 1, 2, 6, 9, 11, 15]))
print(encontrar_menor_indice_faltante([1, 2, 3, 4, 6, 9, 11, 15]))
print(encontrar_menor_indice_faltante([0, 1, 2, 3, 4, 5, 6]))