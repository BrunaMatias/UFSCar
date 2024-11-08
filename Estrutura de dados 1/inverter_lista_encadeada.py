def inverter_lista_encadeada(lista):
    atual = lista
    anterior = None

    while atual is not None:
        proximo_no = atual[1]
        atual[1] = anterior
        anterior = atual
        atual = proximo_no

    return anterior

def imprimir_lista(lista):
    atual = lista
    while atual is not None:
        print(atual[0], end=" ")
        atual = atual[1]
    print()

# Testando a função com as chaves fornecidas
chaves = [7, 12, 3, 29, 42, 10, 1, 5, 19, 4]

# Criando a lista encadeada como uma lista de listas [chave, próximo]
lista_encadeada = [chaves[0], None]
atual = lista_encadeada

for chave in chaves[1:]:
    atual[1] = [chave, None]
    atual = atual[1]

# Invertendo a lista
lista_invertida = inverter_lista_encadeada(lista_encadeada)

print("\nLista invertida:")
imprimir_lista(lista_invertida)
