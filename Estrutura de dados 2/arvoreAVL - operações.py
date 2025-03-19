from collections import deque

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def fator_balanco(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotacao_direita(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def rotacao_esquerda(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def rotacao_esquerda_direita(self, node):
        node.left = self.rotacao_esquerda(node.left)
        return self.rotacao_direita(node)

    def rotacao_direita_esquerda(self, node):
        node.right = self.rotacao_direita(node.right)
        return self.rotacao_esquerda(node)

    def inserir(self, node, key):
        if not node:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self.inserir(node.left, key)
        elif key > node.key:
            node.right = self.inserir(node.right, key)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balanco = self.fator_balanco(node)

        if balanco > 1 and key < node.left.key:
            return self.rotacao_direita(node)
        if balanco < -1 and key > node.right.key:
            return self.rotacao_esquerda(node)
        if balanco > 1 and key > node.left.key:
            node.left = self.rotacao_esquerda(node.left)
            return self.rotacao_direita(node)
        if balanco < -1 and key < node.right.key:
            node.right = self.rotacao_direita(node.right)
            return self.rotacao_esquerda(node)

        return node

    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)

    def remover(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.remover(node.left, key)
        elif key > node.key:
            node.right = self.remover(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self.remover(node.right, temp.key)

        if node is None:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balanco = self.fator_balanco(node)

        if balanco > 1 and self.fator_balanco(node.left) >= 0:
            return self.rotacao_direita(node)

        if balanco > 1 and self.fator_balanco(node.left) < 0:
            node.left = self.rotacao_esquerda(node.left)
            return self.rotacao_direita(node)

        if balanco < -1 and self.fator_balanco(node.right) <= 0:
            return self.rotacao_esquerda(node)

        if balanco < -1 and self.fator_balanco(node.right) > 0:
            node.right = self.rotacao_direita(node.right)
            return self.rotacao_esquerda(node)

        return node

    def buscar_chave(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self.buscar_chave(node.left, key)

        return self.buscar_chave(node.right, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def print_fator_balanco(self, node):
        if node:
            self.print_fator_balanco(node.left)
            print(f'Chave: {node.key}, Fator de Balanço: {self.fator_balanco(node)}')
            self.print_fator_balanco(node.right)

    def nivel_traversal(self):
        if not self.root:
            return
        
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            print(node.key, end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    def sucessor(self, node):
        if node.right:
            return self.min_value_node(node.right)

        succ = None
        while self.root:
            if node.key < self.root.key:
                succ = self.root
                self.root = self.root.left
            elif node.key > self.root.key:
                self.root = self.root.right
            else:
                break
        return succ

    def inserir_chave(self, key):
        self.root = self.inserir(self.root, key)

    def remover_chave(self, key):
        self.root = self.remover(self.root, key)

    def buscar_chave_key(self, key):
        return self.buscar_chave(self.root, key)

    def inorder_traversal(self):
        self.inorder(self.root)
        print()

    def sucessor_key(self, key):
        node = self.buscar_chave_key(key)
        if node:
            succ = self.sucessor(node)
            if succ:
                return succ.key
        return None


# Teste na árvore AVL
avl_tree = AVLTree()
keys = [11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 5, 4, 3, 2, 1, 6, 7, 8, 9, 10]

for key in keys:
    avl_tree.inserir_chave(key)

print("Nível de travessia da árvore AVL construída:")
avl_tree.nivel_traversal()

# Removendo chaves 5, 10 e 15
avl_tree.remover_chave(5)
avl_tree.remover_chave(10)
avl_tree.remover_chave(15)

print("\nNível de travessia após remover chaves 5, 10, e 15:")
avl_tree.nivel_traversal()

print("\nFatores de balanço de todos os nós após as remoções:")
avl_tree.print_fator_balanco(avl_tree.root)
