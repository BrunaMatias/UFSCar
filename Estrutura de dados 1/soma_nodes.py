def cria_node(key, left=None, right=None):
    return {'key': key, 'left': left, 'right': right}

def soma_nodes(node):
    if node is None:
        return 0

    # Verifica se o nó atual é interno (não é folha)
    if node['left'] or node['right']:
        # Soma as chaves do nó atual e seus descendentes
        return node['key'] + soma_nodes(node['left']) + soma_nodes(node['right'])
    else:
        return 0  # Retorna 0 se o nó for uma folha

# Construindo a árvore do exercício anterior como exemplo
root = cria_node(11,
                   left=cria_node(24,
                                   left=cria_node(40, left=cria_node(42), right=cria_node(46)), 
                                    right=cria_node(26)),
                   right=cria_node(30, left=cria_node(48), right=cria_node(58)))

# Testando a função
result = soma_nodes(root)
print("A soma das chaves dos nós internos é:", result)