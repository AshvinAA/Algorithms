# FAST MATRIX DRIFT
import sys

MOD = 10**9 + 7

def matmul(A, B):
    return [
        [
            (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
            (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD
        ],
        [
            (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
            (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD
        ]
    ]

def matpow(A, X):
    result = [[1, 0], [0, 1]]
    while X > 0:
        if X % 2 == 1:
            result = matmul(result, A)
        A = matmul(A, A)
        X //= 2
    return result

def solve():
    
    line = sys.stdin.readline()
    if not line:
        return
    
    T = int(line.strip())
    
    for _ in range(T):
      
        elements = sys.stdin.readline().split()
        if not elements: break
        a11, a12, a21, a22 = map(int, elements)
        
       
        X_line = sys.stdin.readline()
        if not X_line: break
        X = int(X_line.strip())
        
        A = [[a11, a12], [a21, a22]]
        AX = matpow(A, X)
        
        
        sys.stdout.write(f"{AX[0][0]} {AX[0][1]}\n{AX[1][0]} {AX[1][1]}\n")

if __name__ == '__main__':
    solve()