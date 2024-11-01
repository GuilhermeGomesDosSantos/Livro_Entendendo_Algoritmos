# Buscar o número 23: Em uma lista ordenada de números [10, 13, 15, 18, 23, 29, 35, 40], encontre o índice do número 23.
# Se ele não estiver presente, retorne None.

def searchNumber(lista, target):

    indice_valor_inicial = 0
    tamaho_total_lista = len(lista) - 1

    while indice_valor_inicial <= tamaho_total_lista:

        mid = (indice_valor_inicial + tamaho_total_lista) // 2

        if lista[mid] == target:
            return mid
        
        elif lista[mid] < target:
            indice_valor_inicial = mid + 1

        else:
            tamaho_total_lista = mid - 1

    return None

print(searchNumber([10, 13, 15, 18, 23, 29, 35, 40], 23))