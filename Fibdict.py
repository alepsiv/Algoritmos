def fibonacci_diccionario(n, dict={1: 1, 2: 1}):  
    if n in dict:  
        return dict[n]
    else:
        dict[n] = fibonacci_diccionario(n - 1, dict) + fibonacci_diccionario(n - 2, dict)  
        return dict[n]

n = 3
print(f"El valor de la posición {n} en la serie de Fibonacci es {fibonacci_diccionario(n)}")
