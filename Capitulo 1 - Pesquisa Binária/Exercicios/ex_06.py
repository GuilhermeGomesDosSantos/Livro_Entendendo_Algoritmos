# Buscar número em lista com valores duplicados: Dada uma lista de números com valores duplicados [5, 7, 7, 7, 10, 15, 20, 20, 25], encontre o índice do primeiro 7 usando busca binária.

def buscar_numero_repetido_primeiro_indice(lista_num, target):

    valor_inicial = 0
    valor_maximo = len(lista_num) - 1

    while valor_inicial <= valor_maximo:

        meio = (valor_inicial + valor_maximo) // 2

        if lista_num[meio] == target:
            resultado = meio
            valor_maximo = meio - 1  # Continua procurando à esquerda
        
        elif lista_num[meio] > target:
            valor_maximo = meio - 1

        else:
            valor_inicial = meio + 1

    return resultado

print(buscar_numero_repetido_primeiro_indice([5, 7, 7, 7, 10, 15, 20, 20, 25],7))