def bucket_sort(vetor):
    def insertion_sort(bucket):
        # Realiza Insertion Sort em um bucket
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1

            while j >= 0 and key < bucket[j]:
                bucket[j + 1] = bucket[j]
                j -= 1

            bucket[j + 1] = key   
        return bucket

    bucket_count = len(vetor)
    
    # Cria buckets vazios
    buckets = [[] for _ in range(bucket_count)]
    
    valor_max = max(vetor)
    valor_min = min(vetor)
    range_value = valor_max - valor_min
    
    for num in vetor:
        indice = int(((num - valor_min) / range_value) * (bucket_count - 1))
        buckets[indice].append(num)
    
    # Ordena cada bucket com o Insertion Sort
    for i in range(bucket_count):
        buckets[i] = insertion_sort(buckets[i])
    
    # Concatena todos os buckets em um único vetor
    vetor_ordenado = []
    for bucket in buckets:
        vetor_ordenado.extend(bucket)
    
    return vetor_ordenado

# Vetor fornecido
vetor = [29, 12, 3, 7, 2, 17, 4, 19, 42, 31, 20, 15, 10, 9, 16, 8, 1, 13, 21, 5]
vetor_ordenado = bucket_sort(vetor)
print(vetor_ordenado)
