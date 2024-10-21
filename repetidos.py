def repetidos(A):
    B = []
    k = 0
    
    for i in range(len(A)):
        if i == 0 or A[i] != A[i-1]:
            B.append(A[i])
    
    k = len(B)
    return B,k
        
        
A = [1, 1, 2, 2, 3, 4, 5, 7, 7, 7,9,9,9,9,9,9,9]


B, k = repetidos(A)


print(f"A: {B} , k= {k}")
