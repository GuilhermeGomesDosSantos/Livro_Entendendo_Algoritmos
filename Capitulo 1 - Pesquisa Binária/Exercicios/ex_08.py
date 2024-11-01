# Buscar uma data específica em uma lista de strings: Suponha que você tenha uma lista de datas ordenadas como strings ["2024-01-01", "2024-03-01", "2024-06-01", "2024-09-01", "2024-12-01"]. Encontre a posição da data "2024-09-01".

def busca_binaria_data(lista_data, target):

    valor_inicial = 0
    valor_maximo = len(lista_data) - 1

    while valor_inicial <= valor_maximo:

        meio = (valor_inicial + valor_maximo) // 2

        if lista_data[meio] == target:
            return meio
        
        elif lista_data[meio] > target:
            valor_maximo = meio - 1

        else:
            valor_inicial = meio + 1

    return None

print(busca_binaria_data(["2024-01-01", "2024-03-01", "2024-06-01", "2024-09-01", "2024-12-01"], "2024-06-01"))
print(busca_binaria_data(["2024-01-01", "2024-03-01", "2024-06-01", "2024-09-01", "2024-12-01"], "2024-06-09"))