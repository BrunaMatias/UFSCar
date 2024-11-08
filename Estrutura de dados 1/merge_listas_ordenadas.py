def merge_listas_ordenadas(lista1, lista2):
    resultado = [None, None]
    atual = resultado

    while lista1 is not None and lista2 is not None:
        if lista1[0] < lista2[0]:
            atual[1] = lista1
            lista1 = lista1[1]
        else:
            atual[1] = lista2
            lista2 = lista2[1]
        atual = atual[1]

    if lista1 is not None:
        atual[1] = lista1
    else:
        atual[1] = lista2

    return resultado[1]

def imprimir_lista(lista):
    atual = lista
    while atual is not None:
        print(atual[0], end=" ")
        atual = atual[1]
    print()

# Testando a função com as chaves fornecidas
chaves1 = [5, 12, 19, 23, 29, 42]
chaves2 = [2, 3, 7, 15, 20, 25, 33, 39]

# Criando as listas encadeadas ordenadas como listas de listas [chave, próximo]
lista1 = [chaves1[0], None]
atual = lista1

for chave in chaves1[1:]:
    atual[1] = [chave, None]
    atual = atual[1]

lista2 = [chaves2[0], None]
atual = lista2

for chave in chaves2[1:]:
    atual[1] = [chave, None]
    atual = atual[1]

# Realizando o merge e imprimindo o resultado
lista_merged = merge_listas_ordenadas(lista1, lista2)

print("\nLista Resultante:")
imprimir_lista(lista_merged)
