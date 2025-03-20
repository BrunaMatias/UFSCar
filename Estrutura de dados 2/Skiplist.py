import random

class SkipListNode:
    def __init__(self, key, level):
        self.key = key  # chave do nó
        self.level = level  # Nível em que a chave foi inserida
        # Ponteiros para os próximos nós em cada nível
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level  #
        self.head = SkipListNode(None, max_level)  
        self.level = 0  

    # Determinar nível aleatório de um novo nó
    def random_level(self):
        level = 0
        # Aumenta o nível enquanto o número < menor que 0.5 e não excede o nível máximo
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, key):
        # Lista de nós anteriores que precisam ser atualizados
        update = [None] * (self.max_level + 1)
        current = self.head 

        for i in range(self.level, -1, -1):
            # Avança até encontrar um nó com chave maior ou igual à nova chave
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

            update[i] = current

        level = self.random_level()

        # Se o nível do novo nó for maior que o nível atual, atualiza o nível
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.head
            self.level = level

        new_node = SkipListNode(key, level)

        for i in range(level + 1):
            # Atualiza os ponteiros para incluir novo nó
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, key):
        current = self.head  

        for i in range(self.level, -1, -1):
            # Avança até encontrar nó com chave maior ou igual à chave buscada
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]

        # True = chave encontrada ou false = não encontrada
        if current and current.key == key:
            return True
        return False

    def delete(self, key):
        # Lista de nós anteriores que precisam ser atualizados
        update = [None] * (self.max_level + 1)
        current = self.head  

        for i in range(self.level, -1, -1):
            # Avança até encontrar nó com chave maior ou igual à chave a ser removida
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

            update[i] = current

        current = current.forward[0]
        if current and current.key == key:

            for i in range(self.level + 1):
                # Atualiza ponteiros para excluir o nó
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            # Ajusta o nível da Skip List 
            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1

    def print_list(self):
        current = self.head.forward[0]  
        while current:
            print(f"key: {current.key}, Nível: {current.level}")
            current = current.forward[0]  
        print("Fim da lista")

# Criação da Skip List com nível máximo 3
skiplist = SkipList(max_level=3)

# Inserção das chaves
keys = [29, 15, 51, 12, 3, 42, 81, 77, 5, 30, 16, 52, 13, 4, 43, 82, 78, 6, 64, 32]
for key in keys:
    skiplist.insert(key)

print("Chaves na Skip List após inserção:")
skiplist.print_list()

# Remoção das chaves especificadas
keys_para_remover = [12, 42, 77]
for key in keys_para_remover:
    skiplist.delete(key)

# Impressão das chaves após remoção
print("\nChaves na Skip List após remoção de 12, 42 e 77:")
skiplist.print_list()
