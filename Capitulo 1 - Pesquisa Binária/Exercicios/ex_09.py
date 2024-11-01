# Buscar número com limites de intervalo: Em uma lista grande de números inteiros [1, 3, 5, 7, 9, 11, 13, 15, ... até 999], busque o número 501. Use uma busca binária para localizar o índice exato e garantir que ela funcione em grandes listas.

lista = list(range(1, 1000, 2))

def busca_binaria_intervalo(lista, target):
    valor_inicial = 0
    valor_maximo = len(lista) - 1

    while valor_inicial <= valor_maximo:

        meio = (valor_inicial + valor_maximo) // 2

        if lista[meio] == target:
            return meio
        
        elif lista[meio] > target:
            valor_maximo = meio - 1

        else:
            valor_inicial = meio + 1

    return None

print(busca_binaria_intervalo(lista, 501))