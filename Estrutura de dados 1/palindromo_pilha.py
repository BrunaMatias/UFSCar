def palindromo(palavra):
    pilha = []
    for char in palavra:
        pilha.append(char)
        
    inverso = ''

    while pilha:
        inverso += pilha.pop()

    if palavra == inverso:
        return True
            
    else:
        return False

texto = input("Informe uma palavra: ")
resultado = palindromo(texto)

if resultado:
    print(f'A palavra "{texto}" é um palíndromo.')
else:
    print(f'A palavra "{texto}" não é um palíndromo.')