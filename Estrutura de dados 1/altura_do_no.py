class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def altura_no(node):
    if node is None:
        return -1
    else:
        altura_esquerda = altura_no(node.left)
        altura_direita = altura_no(node.right)
        
        # A altura do nó é o máximo entre as alturas dos filhos mais 1
        altura_node = max(altura_esquerda, altura_direita) + 1
        
        return altura_node

# Construa uma árvore binária de busca simples
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(20)

# Calculando a altura de um nó específico 
chave_alvo = root.left.right
altura_alvo = altura_no(chave_alvo)

# Exibindo a altura do nó alvo
print(f"A altura do nó é: {altura_alvo}")