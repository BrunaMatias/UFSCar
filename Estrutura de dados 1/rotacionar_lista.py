def rotacionar_lista(lista, k):
    if not lista or k <= 0:
        return lista

    # Converter a lista para uma lista simples de valores
    valores = []
    atual = lista
    while atual:
        valores.append(atual[0])
        atual = atual[1]

    # Calcula o número real de posições a serem rotacionadas
    k = k % len(valores)

    if k == 0:
        return lista

    # Realiza a rotação na lista de valores
    valores = valores[-k:] + valores[:-k]

    # Recria a lista encadeada a partir da lista de valores rotacionada
    nova_lista = [valores[0], None]
    atual = nova_lista

    for valor in valores[1:]:
        atual[1] = [valor, None]
        atual = atual[1]

    return nova_lista

def imprimir_lista(lista):
    atual = lista
    while atual:
        print(atual[0], end=" ")
        atual = atual[1]
    print()

# Testando a função com a lista fornecida
chaves = [1, 3, 4, 7, 9]
lista_encadeada = [chaves[0], None]
atual = lista_encadeada

for chave in chaves[1:]:
    atual[1] = [chave, None]
    atual = atual[1]

print("Lista original:")
imprimir_lista(lista_encadeada)

# Realizando rotações e imprimindo os resultados
k = int(input("Informe um valor para rotacionar:"))
lista_rotacionada = rotacionar_lista(lista_encadeada, k)
print(f"\nRotação a direita de {k} posição(s):")
imprimir_lista(lista_rotacionada)
