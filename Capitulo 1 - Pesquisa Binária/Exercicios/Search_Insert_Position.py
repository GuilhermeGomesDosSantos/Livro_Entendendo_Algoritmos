# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


def searchInsert(lista, alvo):
        
    valor_menor_lista = 0
    valor_maior_lista = len(lista) - 1

    while valor_menor_lista <= valor_maior_lista:

        mid = (valor_menor_lista + valor_maior_lista) // 2

        if lista[mid] == alvo:
            return mid

        elif alvo < lista[mid]:
            valor_maior_lista -= 1

        elif alvo > lista[mid]:
            valor_menor_lista += 1
        
    return valor_menor_lista

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))