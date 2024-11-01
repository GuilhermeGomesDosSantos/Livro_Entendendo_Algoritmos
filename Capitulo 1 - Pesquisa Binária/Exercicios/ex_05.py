# Localizar o primeiro nome com "João": Em uma lista com nomes que começam com letras diversas ["Ana", "Bianca", "Carlos", "João", "José", "Marcos", "Roberto"], use a busca binária para encontrar "João".

def buscar_nome_joao(list_name, target):

    valor_inicial = 0
    valor_maximo = len(list_name) - 1

    while valor_inicial <= valor_maximo:

        meio = (valor_maximo + valor_inicial) // 2

        if list_name[meio] == target:
            return True
        
        elif list_name[meio] > target:
            valor_maximo = meio - 1

        else:
            valor_inicial = meio + 1
    
    return None

print(buscar_nome_joao(["Ana", "Bianca", "Carlos", "João", "José", "Marcos", "Roberto"], "João"))
print(buscar_nome_joao(["Ana", "Bianca", "Carlos", "João", "José", "Marcos", "Roberto"], "Gui"))