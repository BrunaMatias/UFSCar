class Node:
  """
  Representa um nó na árvore AVL

  Atributos:
    key: Chave do nó.
    left: Filho a esquerda do nó
    right: Filho a direita do nó
    altura: Altura do nó
  """

  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.altura = 1

class AVLTree:
  """
  Atributo:
    root:  Nó raiz da árvore
  """

  def __init__(self):
    self.root = None

  def altura(self, node):
    if node is None:
      return 0
    return node.height

  def get_balance(self, node):

    if node is None:
      return 0
    return self.altura(node.left) - self.altura(node.right)

  def update_altura(self, node):
    """
    Argumentos:
      node: O nó para o qual a altura será atualizada.
    """

    node.altura = max(self.altura(node.left), self.altura(node.right)) + 1

  def right_rotate(self, node):
    """
    Argumentos:
      node: O nó em que a rotação será realizada.

    Retorno:
      O novo nó raiz após a rotação.
    """

    new_root = node.left
    node.left = new_root.right
    new_root.right = node

    self.update_altura(node)
    self.update_altura(new_root)
    return new_root

  def left_rotate(self, node):
    """
    Argumentos:
      node: O nó em que a rotação será realizada.

    Retorno:
      O novo nó raiz após a rotação.
    """

    new_root = node.right
    node.right = new_root.left
    new_root.left = node

    self.update_altura(node)
    self.update_altura(new_root)
    return new_root

  def insert(self, key):
    """
    Insere uma nova chave na árvore AVL.

    Argumentos:
      key: A chave a ser inserida.

    Retorno:
      A raiz da árvore AVL atualizada.
    """

    def _insert(node, key):
      """
      Função para inserir uma nova chave na árvore AVL.

      Argumentos:
        node: O nó atual na recursão.
        key: A chave a ser inserida.
      """
      
      if node is None:
        return Node(key)

      if key < node.key:
        node.left = _insert(node.left, key)
      else:
        node.right = _insert(node.right, key)

      self.update_altura(node)

      balance = self.get_balance(node)

      # Caso 1: Rotação à direita
      if balance > 1 and key < node.left.key:
        return self.right_rotate(node)

      # Caso 2: Rotação à esquerda
      if balance < -1 and key > node.right.key:
        return self.left_rotate(node)

      # Casos 3 e 4: Rotação dupla
      if balance > 1 and key > node.left.key:
        node.left = self.left_rotate(node.left)
        return self

# Exemplo de uso
avl = AVLTree()

avl.insert(8)
avl.insert(3)
avl.insert(12)
avl.insert(6)
avl.insert(10)
avl.insert(5)
avl.insert(1)

avl.in_order(avl.root)