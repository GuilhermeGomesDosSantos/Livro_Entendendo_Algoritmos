def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


# Armazena o menor valor.
# Armazena o índice do menor valor.
# Agora, você pode usar esta função para escrever a ordenação por seleção:


def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacaoporSelecao([5, 3, 6, 2, 10]))
# Ordenações em um array.
# Encontra o menor elemento do array e adiciona ao novo array.
