class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def podar_folhas(node):
    if node is None:
        return None
    
    # Se o nó atual for uma folha, retorna None para ser podado
    if node.left is None and node.right is None:
        return None

    # Caso contrário, realiza a poda nos filhos (recursivamente)
    node.left = podar_folhas(node.left)
    node.right = podar_folhas(node.right)

    return node

# Função auxiliar para imprimir a árvore (usando caminhamento em ordem)
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.key, end=' ')
        inorder_traversal(node.right)

# Construindo uma árvore de exemplo
root = Node(11)
root.left = Node(24)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(26)
root.left.left.left = Node(42)
root.left.left.right = Node(46)
root.right.left = Node(48)
root.right.right = Node(58)

# Exibindo a árvore antes da poda
print("Árvore original:")
inorder_traversal(root)
print()

# Podando os nós folhas
root = podar_folhas(root)

# Exibindo a árvore após a poda
print("Árvore após a poda:")
inorder_traversal(root)