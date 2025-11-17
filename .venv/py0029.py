def fibo(n):
    a, b = 0, 1
    lista_fibo = []
    for _ in range(n):
        lista_fibo.append(a)
        a, b = b, a + b
    return lista_fibo
print(fibo(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]