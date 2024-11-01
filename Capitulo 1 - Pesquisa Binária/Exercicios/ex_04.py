# Verificar a presença de 50: Na lista [10, 20, 30, 40, 60, 70, 80, 90], verifique se o número 50 está presente.
# Retorne o índice se encontrado ou None caso contrário.

def busca_binaria_numero(lista_num, target):

    valor_inicial = 0
    valor_maximo = len(lista_num) - 1

    while valor_inicial <= valor_maximo:

        meio = (valor_inicial + valor_maximo) // 2

        if lista_num[meio] == target:
            return f"O numero '{target}' foi localizado no indice {meio} da lista !!!"
        
        elif lista_num[meio] > target:
            valor_maximo = meio - 1

        else:
            valor_inicial = meio + 1

    return None

print(busca_binaria_numero([10, 20, 30, 40, 60, 70, 80, 90], 50))
print(busca_binaria_numero([10, 20, 30, 40, 60, 70, 80, 90], 500))
print(busca_binaria_numero([10, 20, 30, 40, 60, 70, 80, 90], 10))