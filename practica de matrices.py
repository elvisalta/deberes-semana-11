def buscar_valor(matriz, valor):
    for i in range(len(matriz)):  # Recorrer filas
        for j in range(len(matriz[i])):  # Recorrer columnas
            if matriz[i][j] == valor:
                return i, j  # Devolver la posición si se encuentra el valor
    return None  # Devolver None si el valor no está en la matriz


# Definir una matriz 3x3 con valores numéricos
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar en la matriz: "))

# Realizar la búsqueda
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición {resultado}")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")

