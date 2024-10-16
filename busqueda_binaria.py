def busqueda_binaria(A, ele):
    if len(A) == 0:
        return -1

    m = len(A) // 2

    if A[m] == ele:
        return m

    elif A[m] < ele:
        r = busqueda_binaria(A[m+1:], ele)
        if r == -1:
            return -1
        else:
            return m + 1 + r

    else:
        return busqueda_binaria(A[:m], ele)

A = [3, 5, 7, 9, 17, 21, 30]
ele = 17
i = busqueda_binaria(A, ele)
print(f"El índice del elemento {ele} es: {i}")
