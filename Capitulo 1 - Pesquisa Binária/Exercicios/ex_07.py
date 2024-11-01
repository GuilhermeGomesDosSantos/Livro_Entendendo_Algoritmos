# Verificar a existência de um sobrenome: Na lista de sobrenomes em ordem alfabética ["Alves", "Barbosa", "Cardoso", "Lima", "Martins", "Pereira", "Silva", "Souza"], verifique se o sobrenome "Martins" está presente. Retorne o índice.

def busca_binaria_sobrenome(lista_sobrenome, target):

    valor_inicial = 0
    valor_maximo = len(lista_sobrenome) - 1

    while valor_inicial <= valor_maximo:

        meio = (valor_inicial + valor_maximo) // 2

        if lista_sobrenome[meio] == target:
            return meio
        
        elif lista_sobrenome[meio] > target:
            valor_maximo = meio - 1

        else:
            valor_inicial = meio + 1

    return None

print(busca_binaria_sobrenome(["Alves", "Barbosa", "Cardoso", "Lima", "Martins", "Pereira", "Silva", "Souza"], "Martins"))
print(busca_binaria_sobrenome(["Alves", "Barbosa", "Cardoso", "Lima", "Martins", "Pereira", "Silva", "Souza"], "Gui"))