# def input_matrix():
#     matrix=[]
#     col=[]
#     no_of_row=int(input('Enter no. of rows :: '))
#     no_of_col=int(input('Enter no. of Columns :: '))
    
#     for ir in range (1,no_of_row+1):
#         for ic in range(1,no_of_col+1):
#             print('Enter value of a',ir,ic)
#             val=int(input())
#             col.append(val)
#         matrix.append(col)
#         col=[]
    
#     return no_of_row, no_of_col, matrix

# #-----------ADDITION------------------

# def addition_of_matrix(matrixA,matrixB):
#     addition_matrix=[]
#     addition_col=[]
#     no_of_rowA=len(matrixA)
#     no_of_colA=len(matrixA[0])
#     no_of_rowB=len(matrixB)
#     no_of_colB=len(matrixB[0])
    
#     if no_of_rowA == no_of_rowB and no_of_colA == no_of_colB:
#         for r in range (no_of_rowA):
#             for c in range(no_of_colA):
#                 val=matrixA[r][c] + matrixB[r][c]
#                 addition_col.append(val)
#             addition_matrix.append(addition_col)
#             addition_col=[]
        
#     return addition_matrix

# #--------------SUBTRACTION---------------

# def subtraction_of_matrix(matrixA,matrixB):
#     subtraction_matrix=[]
#     subtraction_col=[]
#     no_of_rowA=len(matrixA)
#     no_of_colA=len(matrixA[0])
#     no_of_rowB=len(matrixB)
#     no_of_colB=len(matrixB[0])
    
#     if no_of_rowA == no_of_rowB and no_of_colA == no_of_colB:
#         for r in range (no_of_rowA):
#             for c in range(no_of_colA):
#                 val=matrixA[r][c] - matrixB[r][c]
#                 subtraction_col.append(val)
#             subtraction_matrix.append(subtraction_col)
#             subtraction_col=[]
        
#     return subtraction_matrix

# #---------------PRODUCT---------------

# def product_of_matrix(matrixA,matrixB):
#     product_matrix=[]
#     product_col=[]
#     no_of_rowA=len(matrixA)
#     no_of_colA=len(matrixA[0])
#     no_of_rowB=len(matrixB)
#     no_of_colB=len(matrixB[0])
    
#     val=0
#     for i in range(no_of_rowA):
#         for j in range(no_of_colB):
#             for k in range(no_of_colA):
#                 val=val+(matrixA[i][k]*matrixB[k][j])
#             product_col.append(val)
#             val=0
#         product_matrix.append(product_col)
#         product_col=[]
        
#     return product_matrix


# #------------ADJOINT OF MATRIX-------------

# def adjoint_matrix(matrix):
#     cofac=cofactor_matrix(matrix)
#     adjoint=transpose(cofac)
#     return adjoint
    

# #------------INVERSE OF A MATRIX-------------
# def inverse_of_matrix(matrix):
#     r=len(matrix)
#     c=len(matrix[0])
#     if r!=c:
#         return "Matrix must be square"
#     identity = []

#     for i in range(r):
#         row = []
#         for j in range(r):
#             if i == j:
#                 row.append(1)
#             else:
#                 row.append(0)
#         identity.append(row)
    
#     for i in range(r):
#         piv=matrix[i][i]
#         if piv==0:
#             return "Matrix is not invertible"
#         for j in range(r):
#             matrix[i][j] /= piv
#             identity[i][j] /= piv
#         for k in range(r):
#             if k != i:
#                 factor = matrix[k][i]
#                 for j in range(r):
#                     matrix[k][j] -= factor * matrix[i][j]
#                     identity[k][j] -= factor * identity[i][j]
#     return identity
    

# def reduce_for_inverse(minor,i,j):
#     row_len=len(minor)
#     for k in range(row_len):
#         del minor[k][j]
#     del minor[i]
#     return minor


# #------------COFACTOR OF MATRIX------------

# def cofactor_matrix(matrix):
#     co_factor_matrix=[]
#     row_cofactor=[]
#     minor=[]
#     temporary=[]
#     for a in matrix:
#         for b in a:
#             temporary.append(b)
#         minor.append(temporary)
#         temporary=[]
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             reduce_for_inverse(minor,i,j)
#             cofactor=(((-1)**(i+j))*(main_determinant(minor)))
#             minor=[]
#             temporary=[]
#             for a in matrix:
#                 for b in a:
#                     temporary.append(b)
#                 minor.append(temporary)
#                 temporary=[]
#             row_cofactor.append(cofactor)
#         co_factor_matrix.append(row_cofactor)
#         row_cofactor=[]
#     return co_factor_matrix


# #---------------DETERMINANT---------------

# def main_determinant(matrix):
#     row = len(matrix)
#     col = len(matrix[0])  
#     if row != col:
#         return "Matrix is not square"
#     if row==1:
#         return matrix[0][0]
#     if row == 2:
#         return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
#     determ = 0
#     for i in range(row):
#         sub_mat = []
#         sign = (-1) ** i
#         for j in range(1, col):
#             sub_row = []
#             for k in range(row):
#                 if k != i:
#                     # sub_row - строкa подматрицы без элемента, находящегося в строке i и столбце i.
#                     sub_row.append(matrix[j][k])
#             sub_mat.append(sub_row)
#         determ += sign * matrix[0][i] * main_determinant(sub_mat)

#     return determ

# #---------------TRANSPOSE---------------

# def transpose(matrix):
#     row_len=len(matrix)
#     col_len=len(matrix[0])
#     row_tr=[]
#     transpose_matrix=[]
#     for z in range (row_len):
#         for e in range (col_len):
#             row_tr.append(matrix[e][z])
#         transpose_matrix.append(row_tr)
#         row_tr=[]
#     return transpose_matrix

# #--------------REF----------------------

# def ref(matrix):
    # row = len(matrix)
    # col = len(matrix[0])
    # mat=[]
    # for i in range(row):
    #     piv = matrix[i][i]  # Pivot element
    #     if piv != 0:
    #         # Normalize the current row
    #         matrix[i] = [element / piv for element in matrix[i]]

    #     for j in range(i + 1, row):
    #         factor = -matrix[j][i]
    #         # Update the rows below with the appropriate factor
    #         for index in range(col):
    #             matrix[j][index] = matrix[j][index] + factor * matrix[i][index]
    # mat.append(matrix)

    # return mat

def input_matrix():
    matrix=[]
    col=[]
    no_of_row=int(input('Enter no. of rows :: '))
    no_of_col=int(input('Enter no. of Columns :: '))
    
    for ir in range (1,no_of_row+1):
        for ic in range(1,no_of_col+1):
            print('Enter value of a',ir,ic)
            val=int(input())
            col.append(val)
        matrix.append(col)
        col=[]
    
    return no_of_row, no_of_col, matrix

#-----------ADDITION------------------

def addition_of_matrix(matrixA,matrixB):
    addition_matrix=[]
    addition_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    
    if no_of_rowA == no_of_rowB and no_of_colA == no_of_colB:
        for r in range (no_of_rowA):
            for c in range(no_of_colA):
                val=matrixA[r][c] + matrixB[r][c]
                addition_col.append(val)
            addition_matrix.append(addition_col)
            addition_col=[]
        
    return addition_matrix

#--------------SUBTRACTION---------------

def subtraction_of_matrix(matrixA,matrixB):
    subtraction_matrix=[]
    subtraction_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    
    if no_of_rowA == no_of_rowB and no_of_colA == no_of_colB:
        for r in range (no_of_rowA):
            for c in range(no_of_colA):
                val=matrixA[r][c] - matrixB[r][c]
                subtraction_col.append(val)
            subtraction_matrix.append(subtraction_col)
            subtraction_col=[]
        
    return subtraction_matrix

#---------------PRODUCT---------------

def product_of_matrix(matrixA,matrixB):
    product_matrix=[]
    product_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    
    val=0
    for i in range(no_of_rowA):
        for j in range(no_of_colB):
            for k in range(no_of_colA):
                val=val+(matrixA[i][k]*matrixB[k][j])
            product_col.append(val)
            val=0
        product_matrix.append(product_col)
        product_col=[]
        
    return product_matrix
#--------------Transpose----------
def transpose(matrix):
    row_len=len(matrix)
    col_len=len(matrix[0])
    row_tr=[]
    transpose_matrix=[]
    for z in range (row_len):
        for e in range (col_len):
            row_tr.append(matrix[e][z])
        transpose_matrix.append(row_tr)
        row_tr=[]
    return transpose_matrix


#------------ADJOINT OF MATRIX-------------

def adjoint_matrix(matrix):
    cofac=cofactor_matrix(matrix)
    adjoint=transpose(cofac)
    return adjoint
    

#------------INVERSE OF A MATRIX-------------

def reduce_for_inverse(minor,i,j):
    row_len=len(minor)
    for k in range(row_len):
        del minor[k][j]
    del minor[i]
    return minor


def inverse_of_matrix(matrix):
    r=len(matrix)
    c=len(matrix[0])
    if r!=c:
        return "Matrix must be square"
    identity = []

    for i in range(r):
        row = []
        for j in range(r):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        identity.append(row)
    
    for i in range(r):
        piv=matrix[i][i]
        if piv==0:
            return "Matrix is not invertible"
        for j in range(r):
            matrix[i][j] /= piv
            identity[i][j] /= piv
        for k in range(r):
            if k != i:
                factor = matrix[k][i]
                for j in range(r):
                    matrix[k][j] -= factor * matrix[i][j]
                    identity[k][j] -= factor * identity[i][j]
    return identity
    
def inverse_of_matrix(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        return None

    # Create an identity matrix of the same size as the input matrix
    identity = [[float(i == j) for j in range(n)] for i in range(n)]

    # Perform Gaussian elimination
    for i in range(n):
        # Swap rows if the pivot element is zero
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    identity[i], identity[j] = identity[j], identity[i]
                    break
            else:
                # No non-zero pivot element found, the matrix is singular
                return None

        pivot = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] /= pivot
        for j in range(n):
            identity[i][j] /= pivot

        for j in range(n):
            if j != i:
                factor = matrix[j][i]
                for k in range(i, n):
                    matrix[j][k] -= factor * matrix[i][k]
                for k in range(n):
                    identity[j][k] -= factor * identity[i][k]

    return identity

# Example usage
# matrix = [[1, 2], [3, 4]]
# inverse_matrix = inverse_of_matrix(matrix)

# print(inverse_matrix)

#------------COFACTOR OF MATRIX------------

def cofactor_matrix(matrix):
    co_factor_matrix=[]
    row_cofactor=[]
    minor=[]
    temporary=[]
    for a in matrix:
        for b in a:
            temporary.append(b)
        minor.append(temporary)
        temporary=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            reduce_for_inverse(minor,i,j)
            cofactor=(((-1)**(i+j))*(main_determinant(minor)))
            minor=[]
            temporary=[]
            for a in matrix:
                for b in a:
                    temporary.append(b)
                minor.append(temporary)
                temporary=[]
            row_cofactor.append(cofactor)
        co_factor_matrix.append(row_cofactor)
        row_cofactor=[]
    return co_factor_matrix


#---------------DETERMINANT---------------
def main_determinant(matrix):
    row = len(matrix)
    col = len(matrix[0])  
    if row != col:
        return "Matrix is not square"
    if row==1:
        return matrix[0][0]
    if row == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    determ = 0
    for i in range(row):
        sub_mat = []
        sign = (-1) ** i
        for j in range(1, col):
            sub_row = []
            for k in range(row):
                if k != i:
                    # sub_row - строкa подматрицы без элемента, находящегося в строке i и столбце i.
                    sub_row.append(matrix[j][k])
            sub_mat.append(sub_row)
        determ += sign * matrix[0][i] * main_determinant(sub_mat)

    return determ
#------minor-------
def reduce_for_determinant(minor,i):
    row_len=len(minor)
    for k in range(row_len):
        del minor[k][0]
    del minor[i]
    return minor


#---------------TRANSPOSE---------------

def multiply_matrix_vector(matrix, vector):
    result = []
    for row in matrix:
        element = sum(x * y for x, y in zip(row, vector))
        result.append(element)
    return result

def normalize_vector(vector):
    magnitude = sum(x ** 2 for x in vector) ** 0.5
    return [x / magnitude for x in vector]

def power_iteration(matrix, num_iterations=1000):
    n = len(matrix)
    # Initialize a random vector
    vector = [1.0] * n

    for _ in range(num_iterations):
        # Multiply matrix by the vector
        result = multiply_matrix_vector(matrix, vector)
        # Normalize the result
        vector = normalize_vector(result)

    # Calculate the eigenvalue
    eigenvalue = multiply_matrix_vector(matrix, vector)[0]

    return eigenvalue, vector

#----------REF--------------------
def row_echelon_form(matrix):
    row = len(matrix)
    col = len(matrix[0])
    mat=[]
    for i in range(row):
        piv = matrix[i][i]  # Pivot element
        if piv != 0:
            # Normalize the current row
            matrix[i] = [element / piv for element in matrix[i]]

        for j in range(i + 1, row):
            factor = -matrix[j][i]
            # Update the rows below with the appropriate factor
            for index in range(col):
                matrix[j][index] = matrix[j][index] + factor * matrix[i][index]
    mat.append(matrix)

    return mat
#----------------rand and dimension-------
def rank_and_dimensions(matrix):
    row_echelon_matrix = row_echelon_form(matrix)

    rank = sum(1 for row in row_echelon_matrix if any(entry != 0 for entry in row))
    dimensions = len(row_echelon_matrix[0])  # Assuming the matrix is not empty

    return rank, dimensions
#--------polar--------
#p=qs-> should return matrixA(которую мы выводили), q=matrixA * s^-1
import math
def multiplication(mat_a,mat_b):
    new_matrix=[]
    if len(mat_a[0])!=len(mat_b):
        return 'multiplication is not possible'

    for i in range(len(mat_a)):
        row=[]
        for j in range(len(mat_b[0])):
            sum=0
            for k in range(len(mat_b)):
                sum+= mat_a[i][k] * mat_b[k][j]
            row.append(sum)
        new_matrix.append(row)
    return new_matrix
def polar(matrix):
    r,c=len(matrix),len(matrix[0])
    transp=transpose(matrix)
    s=multiplication(transp,matrix)
    
    sqrt_matrix = [[math.sqrt(element) for element in row] for row in s]
    sminone = [[1/x if x!=0 else 0 for x in row] for row in sqrt_matrix]
    
    q=multiplication(matrix,sminone)
    p=multiplication(q,sqrt_matrix)
    return q
    
    
