import numpy as np


def package_gaussian(A,b = np.array([])):
    try:
        if b.size == 0:
            coeffs = A[:,:-1]
            rhs = A[:,-1]
            solution = np.linalg.solve(coeffs,rhs)
        else:
            solution = np.linalg.solve(A,b)
        return solution
    except np.linalg.LinAlgError:
        return "Equation has no unique solution"


    
def forward_elimination(mat):
    n = len(mat)

    for i in range(n):
        if mat[i][i] == 0:
            for j in range(i+1,n):
                if mat[j][i] != 0:
                    mat[i],mat[j] = mat[j],mat[i]
                    break
        
        for j in range(i+1,n):
            ratio= mat[j][i] / mat[i][i]
            for k in range(i,len(mat[0])):
                mat[j][k] -= ratio * mat[i][k]

def back_substitution(mat):
    n = len(mat)
    x = [0 for _ in range(n)]

    for i in range(n-1,-1,-1):
        x[i] = mat[i][-1]
        for j in range(i+1,n):
            x[i] -= mat[i][j] * x[j]
        x[i] /= mat[i][i]
    return np.array(x,dtype=float)

def gaussian_elimination(matrix):
    forward_elimination(matrix)
    return back_substitution(matrix)


A = np.array([[3, -1, -1,2], [1, 1, 0,0], [2, 0, -3,-3]],dtype=float)

print(package_gaussian(A))

print(gaussian_elimination(A))