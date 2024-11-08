class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def profundidade_no(raiz, alvo, profundidade=1):
    if raiz is None:
        return 0
    
    if raiz.key == alvo:
        return profundidade

    # Procura o nó alvo nas subárvores esquerda e direita
    profundidade_esquerda = profundidade_no(raiz.left, alvo, profundidade + 1)
    profundidade_direita = profundidade_no(raiz.right, alvo, profundidade + 1)

    # Retorna a profundidade do nó alvo
    return max(profundidade_esquerda, profundidade_direita)

# Criando uma árvore de exemplo
raiz = Node(10)
raiz.left = Node(5)
raiz.right = Node(15)
raiz.left.left = Node(2)
raiz.left.right = Node(8)
raiz.right.right = Node(20)

# Calculando a profundidade de um nó específico 
chave_alvo = 8
profundidade_alvo = profundidade_no(raiz, chave_alvo)

# Exibindo a profundidade do nó alvo
print(f"Profundidade do nó com chave {chave_alvo}: {profundidade_alvo}")