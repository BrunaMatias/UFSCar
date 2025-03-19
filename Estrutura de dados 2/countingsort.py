def counting_sort(vetor):
    m = max(vetor)
    count = [0] * (m + 1)
    
    for i in vetor:
        count[i] += 1
    
    # Vetor de contagem armazena a soma das contagens
    total = 0
    for i in range(len(count)):
        count[i], total = total, total + count[i]
    
    resultado = [0] * len(vetor)
    
    # Coloca cada elemento do vetor inicial na posição correta do vetor resultante
    for i in vetor:
        resultado[count[i]] = i
        count[i] += 1
    
    return resultado

# Vetor fornecido
vetor = [29, 12, 3, 7, 2, 17, 4, 19, 42, 31, 20, 15, 10, 9, 16, 8, 1, 13, 21, 5]

vetor_ordenado = counting_sort(vetor)
print(vetor_ordenado)