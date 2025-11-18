def separar_lista(lista):
    lista_pares = sorted([num for num in lista if num % 2 == 0])
    lista_impares = sorted([num for num in lista if num % 2 != 0])
    return lista_pares, lista_impares
if __name__ == "__main__":
    ejemplo_lista = [6, 1, 8, 7, 3, 2, 4, 9, 5]
    pares, impares = separar_lista(ejemplo_lista)
    print(f"Lista original: {ejemplo_lista}")
    print(f"Números pares ordenados: {pares}")
    print(f"Números impares ordenados: {impares}")

