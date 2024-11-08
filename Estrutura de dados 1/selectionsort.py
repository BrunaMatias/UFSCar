def selection_sort(lista):
    atual = lista

    while atual is not None:
        menor = atual
        corrente = atual[1]

        while corrente is not None:
            if corrente[0] < menor[0]:
                menor = corrente
            corrente = corrente[1]

        # Troca os valores
        atual[0], menor[0] = menor[0], atual[0]

        atual = atual[1]

def imprimir_lista(lista):
    atual = lista
    while atual is not None:
        print(atual[0], end=" ")
        atual = atual[1]
    print()

# Testando a função com as chaves fornecidas
chaves = [6, 11, 2, 28, 41, 9, 0, 4, 18, 3]

# Criando a lista encadeada como uma lista de listas [chave, próximo]
lista_encadeada = [chaves[0], None]
atual = lista_encadeada

for chave in chaves[1:]:
    atual[1] = [chave, None]
    atual = atual[1]

# Ordenando a lista usando Selection Sort
selection_sort(lista_encadeada)

print("\nLista ordenada:")
imprimir_lista(lista_encadeada)
