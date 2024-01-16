import tkinter as tk
from tkinter import Entry, IntVar, Label, Button, Frame, messagebox
class MatrixOperations:
    def row_echelon_form(matrix):
        row = len(matrix)
        col = len(matrix[0])
        mat=[]
        for i in range(row):
           piv = matrix[i][i]  
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
    

    
    def rank_and_dimensions(matrix):
        row_echelon_matrix = MatrixOperations.row_echelon_form(matrix)

        rank = sum(1 for row in row_echelon_matrix if any(entry != 0 for entry in row))
        dimensions = len(row_echelon_matrix[0])  # Предполагается, что матрица не пуста

        return rank, dimensions
    def reduce_for_determinant(minor, i):
        row_len = len(minor)
        for k in range(row_len):
            del minor[k][0]
        del minor[i]
        return minor
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
            determ += sign * matrix[0][i] * MatrixOperations.main_determinant(sub_mat)

        return determ
    
    def cofactor_matrix(matrix):
        co_factor_matrix = []
        for i in range(len(matrix)):
            row_cofactor = []
            for j in range(len(matrix[0])):
                minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
                cofactor = ((-1) ** (i + j)) * MatrixOperations.main_determinant(minor)
                row_cofactor.append(cofactor)
            co_factor_matrix.append(row_cofactor)
        return co_factor_matrix

    
    def adjoint_matrix(matrix):
        transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        cofactor_matrix = MatrixOperations.cofactor_matrix(transposed_matrix)
        adjoint_matrix = [[cofactor_matrix[j][i] for j in range(len(cofactor_matrix))] for i in range(len(cofactor_matrix[0]))]
        return adjoint_matrix


    def inverse_of_matrix(matrix):
        r=len(matrix)
        c=len(matrix[0])
        if r!=c:
            return "Matrix must be square"
        identity = []
        for i in range(r):
            row = []
            for j in range(r):
                if i==j:
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
                    fact=matrix[k][i]
                    for j in range(r):
                        matrix[k][j] -= fact * matrix[i][j]
                        identity[k][j] -= fact * identity[i][j]
        return identity

        
    def matrix_multiply(matrix1, matrix2):
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                row.append(sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))))
            result.append(row)
        return result

    
    def vector_normalize(vector):
        magnitude = sum(x**2 for x in vector)**0.5
        return [x / magnitude for x in vector]

    
    def power_iteration(matrix, epsilon=1e-10, max_iterations=1000):
        matrix_size = len(matrix)
        eigenvector = [1.0] * matrix_size
        eigenvalue = 0.0

        for _ in range(max_iterations):
            next_eigenvector = MatrixOperations.matrix_multiply(matrix, [eigenvector])[0]
            eigenvalue = next_eigenvector[0]
            next_eigenvector = MatrixOperations.vector_normalize(next_eigenvector)

            # Check for convergence
            if abs(eigenvector[0] - next_eigenvector[0]) < epsilon:
                break

            eigenvector = next_eigenvector

        return eigenvalue
    
    def transpose_matrix(matrix):
        return [list(row) for row in zip(*matrix)]

    
    def identity_matrix(size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    
    def ower_iteration(matrix, max_iterations=1000, epsilon=1e-10):
        n = len(matrix)
        eigenvector = [1.0] * n

        for _ in range(max_iterations):
            new_eigenvector = MatrixOperations.matrix_multiply(matrix, eigenvector)
            eigenvalue = max(new_eigenvector)
            new_eigenvector = MatrixOperations.vector_scalar_multiply(new_eigenvector, 1 / eigenvalue)

            if max(abs(entry1 - entry2) for entry1, entry2 in zip(new_eigenvector, eigenvector)) < epsilon:
                break

            eigenvector = new_eigenvector

        return eigenvalue, eigenvector

    
    def jacobi_diagonalization(matrix, max_iterations=1000, epsilon=1e-10):
        n = len(matrix)
        eigenvectors = MatrixOperations.identity_matrix(n)

        for _ in range(max_iterations):
            max_off_diagonal, p, q = MatrixOperations.find_max_off_diagonal(matrix)
            if max_off_diagonal < epsilon:
                break

            a_pp, a_qq = matrix[p][p], matrix[q][q]
            a_pq = matrix[p][q]

            theta = 0.5 * MatrixOperations.arctan(2 * a_pq / (a_qq - a_pp))

            cos_theta = MatrixOperations.cos(theta)
            sin_theta = MatrixOperations.sin(theta)

            for i in range(n):
                matrix[i][p], matrix[i][q] = (
                    matrix[i][p] * cos_theta - matrix[i][q] * sin_theta,
                    matrix[i][p] * sin_theta + matrix[i][q] * cos_theta,
                )

                eigenvectors[i][p], eigenvectors[i][q] = (
                    eigenvectors[i][p] * cos_theta - eigenvectors[i][q] * sin_theta,
                    eigenvectors[i][p] * sin_theta + eigenvectors[i][q] * cos_theta,
                )

            for j in range(n):
                matrix[p][j], matrix[q][j] = (
                    matrix[p][j] * cos_theta - matrix[q][j] * sin_theta,
                    matrix[p][j] * sin_theta + matrix[q][j] * cos_theta,
                )

        eigenvalues = [matrix[i][i] for i in range(n)]

        return eigenvalues, eigenvectors

    
    def find_max_off_diagonal(matrix):
        n = len(matrix)
        max_val = 0
        p, q = 0, 0

        for i in range(n):
            for j in range(i + 1, n):
                if abs(matrix[i][j]) > max_val:
                    max_val = abs(matrix[i][j])
                    p, q = i, j

        return max_val, p, q

    
    def arctan(x):
        # Пример простой аппроксимации арктангенса для примера
        result = 0
        for n in range(1, 1000, 2):
            result += ((-1) ** (n // 2)) * (x ** n) / n
        return result

    
    def cos(x):
        # Пример простой аппроксимации косинуса для примера
        result = 0
        for n in range(1000):
            result += ((-1) ** n) * (x ** (2 * n)) / MatrixOperations.factorial(2 * n)
        return result

    
    def sin(x):
        # Пример простой аппроксимации синуса для примера
        result = 0
        for n in range(1000):
            result += ((-1) ** n) * (x ** (2 * n + 1)) / MatrixOperations.factorial(2 * n + 1)
        return result

    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    def svd(matrix, max_iterations=100, epsilon=1e-10):
        m, n = len(matrix), len(matrix[0])

        u = MatrixOperations.identity_matrix(m)
        v_t = MatrixOperations.identity_matrix(n)

        for _ in range(max_iterations):
            u, sigma, v_t = MatrixOperations.one_sided_jacobi_svd(matrix)

            sigma_matrix = MatrixOperations.create_sigma_matrix(sigma, m, n)
            approx_matrix = MatrixOperations.matrix_multiply(u, MatrixOperations.matrix_multiply(sigma_matrix, MatrixOperations.transpose_matrix(v_t)))

            if MatrixOperations.matrix_frobenius_norm_squared(MatrixOperations.matrix_subtract(matrix, approx_matrix)) < epsilon:
                break

        return u, sigma, v_t

    
    def one_sided_jacobi_svd(matrix):
        m, n = len(matrix), len(matrix[0])

        u = MatrixOperations.identity_matrix(m)
        v_t = MatrixOperations.identity_matrix(n)

        for _ in range(2 * max(m, n) ** 2):
            if m > n:
                matrix, u = MatrixOperations.one_sided_jacobi_svd_step(matrix, u)
            else:
                matrix, v_t = MatrixOperations.one_sided_jacobi_svd_step(MatrixOperations.transpose_matrix(matrix), MatrixOperations.transpose_matrix(v_t))

        sigma = [matrix[i][i] for i in range(min(m, n))]
        return u, sigma, v_t

    
    def one_sided_jacobi_svd_step(matrix, transformation_matrix):
        m, n = len(matrix), len(matrix[0])
        p, q = MatrixOperations.find_max_off_diagonal(matrix)
        theta = 0.5 * MatrixOperations.arctan(2 * matrix[p][q] / (matrix[q][q] - matrix[p][p]))

        cos_theta = MatrixOperations.cos(theta)
        sin_theta = MatrixOperations.sin(theta)

        for i in range(m):
            matrix[i][p], matrix[i][q] = (
                matrix[i][p] * cos_theta - matrix[i][q] * sin_theta,
                matrix[i][p] * sin_theta + matrix[i][q] * cos_theta,
            )

            transformation_matrix[i][p], transformation_matrix[i][q] = (
                transformation_matrix[i][p] * cos_theta - transformation_matrix[i][q] * sin_theta,
                transformation_matrix[i][p] * sin_theta + transformation_matrix[i][q] * cos_theta,
            )

        return matrix, transformation_matrix

    
    def create_sigma_matrix(sigma, m, n):
        sigma_matrix = [[0] * n for _ in range(m)]
        min_dim = min(m, n)

        for i in range(min_dim):
            sigma_matrix[i][i] = sigma[i]

        return sigma_matrix

    
    def matrix_frobenius_norm_squared(matrix):
        return sum(entry ** 2 for row in matrix for entry in row)
    def polar(matrix):
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
                        sum+= mat_a[i][k] *mat_b[k][j]
                    row.append(sum)
                new_matrix.append(row)
            return new_matrix
        def transp(mat):
            transpose_mat=[]
            for i in range(len(mat)):
                row=[]
                for j in range(len(mat[0])):
                    row.append(mat[j][i])
                transpose_mat.append(row)
            return transpose_mat
        transposee=transp(matrix)
        s=multiplication(transposee,matrix)
        sqrt_matrix=[[math.sqrt(element) for element in row] for row in s]
        sminone=[[1/x if x!=0 else 0 for x in row] for row in sqrt_matrix]
        q=multiplication(matrix,sminone)
        p=multiplication(q,sqrt_matrix)
        return sqrt_matrix
        
class MatrixInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Operations")

        self.row_var = IntVar()
        self.col_var = IntVar()
        self.matrix_vars = []

        self.input_row_column()

    def input_row_column(self):
        middle_frame = Frame(self.root, bg='black')
        middle_frame.grid(row=5, rowspan=4, column=2, columnspan=4, padx=200, pady=50)

        Label(middle_frame, text="Enter number of rows", bg='black', fg='white',
              borderwidth=3, relief="groove", font=('ariel', 10), width=21).grid(row=4, column=8, columnspan=3)
        Label(middle_frame, text="Enter number of columns", bg='black', fg='white',
              borderwidth=3, relief="groove", font=('ariel', 10), width=21).grid(row=5, column=8, columnspan=3)

        Entry(middle_frame, width=4, textvariable=self.row_var, borderwidth=3, bg='gray64',
              fg='black', relief="solid").grid(row=4, column=12)
        Entry(middle_frame, width=4, textvariable=self.col_var, borderwidth=3, bg='gray64',
              fg='black', relief="solid").grid(row=5, column=12)

        Button(middle_frame, text='Submit', bg="black", fg="white", width=5, command=self.input_grid).grid(row=6, column=10, columnspan=3)

    def input_grid(self):
        rows = self.row_var.get()
        cols = self.col_var.get()

        if rows > 0 and cols > 0:
            self.matrix_vars = [[IntVar() for _ in range(cols)] for _ in range(rows)]

            middle_frame = Frame(self.root, bg='black')
            middle_frame.grid_forget()
            right_frame = Frame(self.root, bg='BLACK')
            right_frame.grid(row=5, rowspan=100, column=50, columnspan=4, padx=200, pady=50)

            Label(right_frame, text="INPUT MATRIX", fg="white", bg="black", font=('ariel', 15)).grid(row=0, column=1, columnspan=3, padx=10, pady=10)

            for i in range(1, rows + 1):
                for j in range(1, cols + 1):
                    ent = Entry(right_frame, width=4, textvariable=self.matrix_vars[i-1][j-1])
                    ent.grid(row=i, column=j)

            Button(right_frame, text='Polar', bg="black", fg="white", font=('ariel', 15), width=5, command=self.input_cmd).grid(row=rows + 1, column=1, columnspan=3, pady=10)
            Button(right_frame, text='REF', font=('ariel', 15), bg="black", fg="white", width=5, command=self.ref_cmd).grid(row=rows + 2, column=1, columnspan=3, pady=10)
            Button(right_frame, text='Determinant', font=('ariel', 15), bg="black", fg="white", width=12, command=self.determinant_cmd).grid(row=rows + 3, column=1, columnspan=3, pady=10)
            Button(right_frame, text='Rank/Dimension', font=('ariel', 15), bg="black", fg="white", width=15, command=self.rank_dimension_cmd).grid(row=rows + 4, column=1, columnspan=3, pady=10)
            Button(right_frame, text='Inverse', font=('ariel', 15), bg="black", fg="white", width=8, command=self.inverse_cmd).grid(row=rows + 5, column=1, columnspan=3, pady=10)
            Button(right_frame, text='Cofactor Matrix', font=('ariel', 15), bg="black", fg="white", width=15, command=self.cofactor_matrix_cmd).grid(row=rows + 6, column=1, columnspan=3, pady=10)
            Button(right_frame, text='Eigenvalues', font=('ariel', 15), bg="black", fg="white", width=12, command=self.eigenvalues_cmd).grid(row=rows + 7, column=1, columnspan=3, pady=10)
            Button(right_frame, text='Eigenvectors', font=('ariel', 15), bg="black", fg="white", width=12, command=self.eigenvectors_cmd).grid(row=rows + 8, column=1, columnspan=3, pady=10)
            Button(right_frame, text='SVD', font=('ariel', 15), bg="black", fg="white", width=8, command=self.svd_cmd).grid(row=rows + 9, column=1, columnspan=3, pady=10)
        else:
            messagebox.showerror("Input Error", "Rows and columns must be greater than zero.")

    def input_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

        # Используем методы из MatrixOperations
        polar_form=MatrixOperations.polar(mainmatrix)
        messagebox.showinfo("Result", f"Polar (S=sqrt(A^T * A)):\n{polar_form}")

    def ref_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)
            
        ref_matrix = MatrixOperations.row_echelon_form(mainmatrix)

        messagebox.showinfo("Result", f"REF Matrix:\n{ref_matrix}")

    def determinant_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

        # Используем методы из MatrixOperations
        determinant_value = MatrixOperations.main_determinant(mainmatrix)

        messagebox.showinfo("Result", f"Determinant: {determinant_value}")
    def rank_dimension_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

        # Используем методы из MatrixOperations
        rank, dimensions = MatrixOperations.rank_and_dimensions(mainmatrix)

        messagebox.showinfo("Result", f"Rank: {rank}, Dimensions: {dimensions}")
    def inverse_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

    # Используем методы из MatrixOperations
        inverse_matrix = MatrixOperations.inverse_of_matrix(mainmatrix)

        inverse_result = "Inverse Matrix:\n"
        for row in inverse_matrix:
            inverse_result += "\t".join(map(str, row)) + "\n"

        messagebox.showinfo("Result", inverse_result)
    def cofactor_matrix_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

        # Используем методы из MatrixOperations
        cofactor_matrix = MatrixOperations.cofactor_matrix(mainmatrix)

        cofactor_result = "Cofactor Matrix:\n"
        for row in cofactor_matrix:
            cofactor_result += "\t".join(map(str, row)) + "\n"

        messagebox.showinfo("Result", cofactor_result)
    def eigenvalues_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

        # Используем методы из MatrixOperations
        eigenvalues = MatrixOperations.power_iteration(mainmatrix)

        messagebox.showinfo("Result", f"Eigenvalues: {eigenvalues}")
    def eigenvectors_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

    # Используем методы из MatrixOperations
        eigenvalues, eigenvectors = MatrixOperations.power_iteration(mainmatrix)

        eigenvectors_result = "Eigenvectors:\n"
        for i, vector in enumerate(eigenvectors):
            eigenvectors_result += f"Eigenvalue {i + 1}: {eigenvalues[i]}\n"
            eigenvectors_result += "\t".join(map(str, vector)) + "\n"

        messagebox.showinfo("Result", eigenvectors_result)
    def svd_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

        # Используем методы из MatrixOperations
        U, S, Vt = MatrixOperations.svd(mainmatrix)

        svd_result = f"Singular Value Decomposition:\nU:\n{U}\nS:\n{S}\nVt:\n{Vt}"
        messagebox.showinfo("Result", svd_result)

def main():
    root = tk.Tk()
    app = MatrixInputApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()