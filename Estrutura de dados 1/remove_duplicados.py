class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Função para remover itens duplicados
def remove_duplicatas(linked_list):
    atual = linked_list
    valores_vistos = set()

    while atual:
        if atual.data not in valores_vistos:
            valores_vistos.add(atual.data)
            atual = atual.next
        else:
            next_node = atual.next
            if next_node:
                next_node.prev = atual.prev
            atual.prev.next = next_node
            atual = next_node

    return linked_list

def print_linked_list(linked_list):
    atual = linked_list
    while atual:
        print(atual.data, end=" ")
        atual = atual.next
    print()

# Exemplo de uso com lista passada:
lista_original = Node(1)
lista_original.next = Node(2)
lista_original.next.prev = lista_original
lista_original.next.next = Node(2)
lista_original.next.next.prev = lista_original.next
lista_original.next.next.next = Node(3)
lista_original.next.next.next.prev = lista_original.next.next
lista_original.next.next.next.next = Node(4)
lista_original.next.next.next.next.prev = lista_original.next.next.next
lista_original.next.next.next.next.next = Node(4)
lista_original.next.next.next.next.next.prev = lista_original.next.next.next.next
lista_original.next.next.next.next.next.next = Node(4)
lista_original.next.next.next.next.next.next.prev = lista_original.next.next.next.next.next
lista_original.next.next.next.next.next.next.next = Node(5)
lista_original.next.next.next.next.next.next.next.prev = lista_original.next.next.next.next.next.next

print("Lista original:")
print_linked_list(lista_original)

# Aplica função
lista_final = remove_duplicatas(lista_original)

print("Lista sem duplicatas:")
print_linked_list(lista_final)
