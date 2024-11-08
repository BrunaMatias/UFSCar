class FilaComDuasPilhas:
    def __init__(s):
        s.pilha_entrada = []
        s.pilha_saida = []

    def enqueue(s, key):
        s.pilha_entrada.append(key)

    def dequeue(s):
        if not s.pilha_saida:
            while s.pilha_entrada:
                s.pilha_saida.append(s.pilha_entrada.pop())
        if not s.pilha_saida:
            print("A fila está vazia")
            
        return s.pilha_saida.pop()
    
fila = FilaComDuasPilhas()

qtd_inserida = int(input(f"Informe a quantidade de número a serem inseridos: "))

for i in range(qtd_inserida):
    inserido = int(input(f"Informe o número {i} a ser inserido: "))
    fila.enqueue(inserido)

qtd_retirada = int(input(f"Informe a quantidade de número a serem retirados: "))

for i in range(qtd_retirada):
    print(fila.dequeue())  
