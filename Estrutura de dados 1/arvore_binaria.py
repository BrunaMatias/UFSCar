class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_key(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def search_key(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def remove_key(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._remove(root.left, key)
        elif key > root.key:
            root.right = self._remove(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._min_node(root.right)
            root.right = self._remove(root.right, root.key)

        return root

    def _min_node(self, root):
        atual = root
        while atual.left is not None:
            atual = atual.left
        return atual.key

    def preorder_walk(self):
        self._preorder(self.root)

    def _preorder(self, root):
        if root is not None:
            print(root.key, end=' ')
            self._preorder(root.left)
            self._preorder(root.right)

    def inorder_walk(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root is not None:
            self._inorder(root.left)
            print(root.key, end=' ')
            self._inorder(root.right)

    def postorder_walk(self):
        self._postorder(self.root)

    def _postorder(self, root):
        if root is not None:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.key, end=' ')

    def min_key(self):
        atual = self.root
        while atual.left is not None:
            atual = atual.left
        return atual.key

    def max_key(self):
        atual = self.root
        while atual.right is not None:
            atual = atual.right
        return atual.key

    def sucessor(self, key):
        node = self._search(self.root, key)
        if node is not None and node.right is not None:
            return self._min_node(node.right)
        sucessor = None
        atual = self.root
        while atual is not None:
            if key < atual.key:
                sucessor = atual
                atual = atual.left
            elif key > atual.key:
                atual = atual.right
            else:
                break
        return sucessor.key if sucessor else None

# Teste com árvore genérica
tree = BinaryTree()

# Inserir as chaves
keys_to_insert = [29, 12, 4, 3, 5, 6, 15, 13, 16, 51, 42, 30, 32, 43, 77, 52, 64, 81, 78, 82]
for key in keys_to_insert:
    tree.insert_key(key)

# Mostrar percurso preorder, inorder e postorder
print("Percurso Preorder:")
tree.preorder_walk()
print("\nPercurso Inorder:")
tree.inorder_walk()
print("\nPercurso Postorder:")
tree.postorder_walk()

# Encontrar o mínimo e o máximo
print("\n\nMínimo:", tree.min_key())
print("Máximo:", tree.max_key())

# Encontrar sucessores
print("\n\nSucessor de 3:", tree.sucessor(3))
print("Sucessor de 52:", tree.sucessor(52))
print("Sucessor de 16:", tree.sucessor(16))

# Remover chaves
remover_key = [12, 30, 43]
for key in remover_key:
    tree.remove_key(key)

# Mostrar percurso preorder, inorder e postorder após remoção
print("\nPercurso Preorder após remoção:")
tree.preorder_walk()
print("\nPercurso Inorder após remoção:")
tree.inorder_walk()
print("\nPercurso Postorder após remoção:")
tree.postorder_walk()