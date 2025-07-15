# 1. Ordenamiento por burbuja
def bubble_sort(lista):  # Función de ordenamiento burbuja
    n = len(lista)  # Obtiene la longitud de la lista
    # Recorre toda la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Si el elemento actual es mayor que el siguiente
            if lista[j] > lista[j+1]:
                # Intercambia los elementos
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista  # Devuelve la lista ordenada

# 2. Ordenamiento quicksort
def quicksort(lista):  # Función de ordenamiento quicksort
    # Caso base: lista vacía o de un solo elemento
    if len(lista) <= 1:
        return lista  # Devuelve la lista tal cual
    else:
        pivote = lista[0]  # Elegimos el primer elemento como pivote
        # Elementos menores al pivote
        menores = [x for x in lista[1:] if x < pivote]
        # Elementos mayores o iguales al pivote
        mayores = [x for x in lista[1:] if x >= pivote]
        # Ordena recursivamente y combina
        return quicksort(menores) + [pivote] + quicksort(mayores)

# 3. Búsqueda lineal
def busqueda_lineal(lista, objetivo):  # Función de búsqueda lineal
    # Recorre la lista
    for i in range(len(lista)):
        # Si encuentra el objetivo
        if lista[i] == objetivo:
            return i  # Devuelve la posición
    return -1  # Devuelve -1 si no lo encuentra

# 4. Búsqueda binaria
def busqueda_binaria(lista, objetivo):  # Función de búsqueda binaria
    izquierda = 0  # Límite izquierdo
    derecha = len(lista) - 1  # Límite derecho
    # Mientras el rango sea válido
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Calcula el punto medio
        # Si encuentra el objetivo
        if lista[medio] == objetivo:
            return medio  # Devuelve la posición
        # Si el medio es menor que el objetivo
        elif lista[medio] < objetivo:
            izquierda = medio + 1  # Busca en la mitad derecha
        else:
            derecha = medio - 1  # Busca en la mitad izquierda
    return -1  # Devuelve -1 si no lo encuentra

# Datos de prueba
datos = [34, 7, 23, 32, 5, 62, 19, 45]  # Lista de números para probar
objetivo = 32  # Número a buscar

# Resultados
print("Lista original:", datos)  # Muestra la lista original

# Búsqueda lineal en la lista original
resultado_lineal = busqueda_lineal(datos, objetivo)  # Busca el objetivo con búsqueda lineal
print("Búsqueda lineal:", "Encontrado en posición" if resultado_lineal != -1 else "No encontrado", resultado_lineal)  # Muestra resultado

# Ordenar con Bubble Sort
ordenada_bubble = bubble_sort(datos.copy())  # Ordena la lista con bubble sort
print("Lista ordenada con Bubble Sort:", ordenada_bubble)  # Muestra la lista ordenada

# Ordenar con Quicksort
ordenada_quick = quicksort(datos.copy())  # Ordena la lista con quicksort
print("Lista ordenada con Quicksort:", ordenada_quick)  # Muestra la lista ordenada

# Búsqueda binaria sobre ambas listas ordenadas
resultado_binaria_bubble = busqueda_binaria(ordenada_bubble, objetivo)  # Busca con binaria en bubble sort
resultado_binaria_quick = busqueda_binaria(ordenada_quick, objetivo)  # Busca con binaria en quicksort

print("Búsqueda binaria (lista ordenada con Bubble):", resultado_binaria_bubble)  # Muestra resultado binaria bubble
print("Búsqueda binaria (lista ordenada con Quicksort):", resultado_binaria_quick)  # Muestra resultado binaria quicksort