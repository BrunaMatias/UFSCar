def alunos_sem_lanche(estudantes, sanduiches):
    fila = estudantes.copy()
    pilha = sanduiches.copy()

    while fila and pilha:
        if fila[0] == pilha[0]:
            fila.pop(0)
            pilha.pop(0)
        else:
            temp = fila.pop(0)
            fila.append(temp)
            
            pilha.pop(0)

    return len(fila)

qtd_estudantes = int(input("Informe a quantidade de estudantes: "))
preferencias = []
ordem_sanduiches = []

for i in range(qtd_estudantes):
    estudante = int(input(f"Informe a preferência do estudante {i}: "))
    preferencias.append(estudante)

print("\n")
qtd_sanduiches = int(input("Informe a quantidade de sanduiches: "))

for i in range(qtd_sanduiches):
    sanduiche = int(input("Informe a ordem dos sanduíches na pilha: "))
    ordem_sanduiches.append(sanduiche)

resultado = alunos_sem_lanche(preferencias, ordem_sanduiches)

print("Número de alunos sem lanche:", resultado)