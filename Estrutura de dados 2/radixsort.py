def counting_sort_for_radix(vetor, digito):  
    n = len(vetor)
    vetor_final = [0] * n
    count = [0] * 10
    
    # Armazena a contagem de ocorrências de cada dígito
    for i in range(n):
        indice = vetor[i] // digito
        count[indice % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Constrói o vetor final
    i = n - 1
    while i >= 0:
        indice = vetor[i] // digito
        vetor_final[count[indice % 10] - 1] = vetor[i]
        count[indice % 10] -= 1
        i -= 1
    
    for i in range(n):
        vetor[i] = vetor_final[i]

def radix_sort(vetor):
    m = max(vetor)
    
    # Realiza o counting sort para cada dígito
    digito = 1
    while m // digito > 0:
        counting_sort_for_radix(vetor, digito)
        digito *= 10

# Vetor fornecido
vetor = [29, 125, 391, 74, 213, 178, 43, 19, 424, 131, 120, 158, 105, 92, 169, 81, 1, 143, 210, 51]

# Teste do algoritmo Radixsort
radix_sort(vetor)
print(vetor)