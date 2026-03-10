# Simple Recursive Algorithm (Sum Array)

def sum_array(A, n):
    if n == 1:
        return A[0]
    
    s = sum_array(A, n-1)
    s = s + A[n-1]
    return s

A = [1, 2, 3, 4, 5]
n = len(A)

print("Jumlah =", sum_array(A, n))