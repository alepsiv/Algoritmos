def fibonacci_arreglo(n, fib_arr=None):
    if fib_arr is None:
        fib_arr = [0, 1, 1]  

    if n < len(fib_arr):  
        return fib_arr[n]
    else:
        
        fib_arr.append(fibonacci_arreglo(n - 1, fib_arr) + fibonacci_arreglo(n - 2, fib_arr))
        return fib_arr[n]

n = 7
print(f"El valor de la posición {n} en la serie de Fibonacci es {fibonacci_arreglo(n)}")
