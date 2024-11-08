def fatoracao_prima(n):
    fatores_primos = []

    divisor = 2
    while n > 1:
        while n % divisor == 0:
            fatores_primos.append(divisor)
            n //= divisor
        divisor += 1

    fatores_primos.reverse()
    print(" * ".join(map(str, fatores_primos)))

numero = int(input())
print(f'Fatoração prima de {numero}: ', end='')
fatoracao_prima(numero)