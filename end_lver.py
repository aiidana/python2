import tkinter as tk
from tkinter import Entry, IntVar, Label, Button, Frame, messagebox
class MatrixOperations:
    def row_echelon_form(matrix):
        row=len(matrix)
        col=len(matrix[0])
        mat=[]
        for i in range(row):
            piv=matrix[i][i]
            if piv!=0:
                matrix[i]=[element / piv for element in matrix[i]]
            for j in range(i+1,row):
                factor=-matrix[j][i]
                for index in range(col):
                    matrix[j][index]=matrix[j][index]+factor*matrix[i][index]
        mat.append(matrix)
        return mat
    
    def rank_and_dimensions(matrix):
        row_echelon_matrix = MatrixOperations.row_echelon_form(matrix)

        rank = sum(1 for row in row_echelon_matrix if any(entry != 0 for entry in row))
        dimensions = len(row_echelon_matrix[0])  

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
        determ=0
        for i in range(row):
            sub_mat=[]
            sign=(-1)**i
            for j in range(1,col):
                sub_row=[]
                for k in range(row):
                    if k!=i:
                        sub_row.append(matrix[j][k])
                sub_mat.append(sub_row)
            determ+= sign*matrix[0][i] *MatrixOperations.main_determinant(sub_mat)
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
            row=[]
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

    def jordan_decomposition(matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        
        if rows != cols:
            raise ValueError("Jordan decomposition is only defined for square matrices")

        n = rows

        
        jordan_matrix = [[0] * n for _ in range(n)]
        jordan_basis = [[0] * n for _ in range(n)]

        for i in range(n):
            jordan_matrix[i][i] = 1
            jordan_basis[i][i] = 1

        for i in range(n):
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    factor = matrix[j][i] / matrix[i][i]
                    for k in range(n):
                        matrix[j][k] -= factor * matrix[i][k]
                        jordan_basis[j][k] -= factor * jordan_basis[i][k]

        return jordan_basis
    def cramer(matrix, constants):
        n = len(matrix)
        if n != len(matrix[0]):
            raise ValueError("Matrix must be square for Cramer's Rule.")

        determinant_matrix = MatrixOperations.main_determinant(matrix)

        if determinant_matrix == 0:
            raise ValueError("Matrix is singular, Cramer's Rule is not applicable.")

        solutions = []

        for i in range(n):
            modified_matrix = [row[:] for row in matrix]
            for j in range(n):
                modified_matrix[j][i] = constants[j]

            solutions.append(MatrixOperations.main_determinant(modified_matrix) / determinant_matrix)

        return solutions
    def dot_product(vector1, vector2):
        return sum(x * y for x, y in zip(vector1, vector2))

    
    def scalar_multiply(scalar, vector):
        return [scalar * x for x in vector]

    
    def subtract_vectors(vector1, vector2):
        return [x - y for x, y in zip(vector1, vector2)]

    
    def magnitude(vector):
        return sum(x**2 for x in vector) ** 0.5

    
    def normalize(vector):
        mag = MatrixOperations.magnitude(vector)
        return [x / mag for x in vector]

    
    def eigen_decomposition(matrix, iterations=1000, epsilon=1e-10):
        n = len(matrix)

        
        eigenvector = [1.0] * n

        for _ in range(iterations):
            
            Av = MatrixOperations.multiply_matrix_vector(matrix, eigenvector)

            
            eigenvalue = MatrixOperations.dot_product(Av, eigenvector)

            
            norm_eigenvector = MatrixOperations.normalize(eigenvector)

            
            if MatrixOperations.magnitude(MatrixOperations.subtract_vectors(norm_eigenvector, eigenvector)) < epsilon:
                break

            eigenvector = norm_eigenvector

        return eigenvalue

    
    def multiply_matrix_vector(matrix, vector):
        result = []
        for row in matrix:
            result.append(MatrixOperations.dot_product(row, vector))
        return result
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
        return q

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
            Button(right_frame, text='Jordan', font=('ariel', 15), bg="black", fg="white", width=12, command=self.jordan_decomposition_cmd).grid(row=rows + 7, column=1, columnspan=3, pady=10)
            Button(right_frame, text='Eigenvalue', font=('ariel', 15), bg="black", fg="white", width=20, command=self.eigenvalues_cmd).grid(row=rows + 8, column=1, columnspan=3, pady=10)
            Button(right_frame, text='Cramer', font=('ariel', 15), bg="black", fg="white", width=8, command=self.cramer_cmd).grid(row=rows + 9, column=1, columnspan=3, pady=10)
        else:
            messagebox.showerror("Input Error", "Rows and columns must be greater than zero.")

    def input_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

        # Используем методы из MatrixOperations
        polar_result = MatrixOperations.polar(mainmatrix)

        messagebox.showinfo("Result", f"Polar Q=A*S^-1: {polar_result}")

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

        
        determinant_value = MatrixOperations.main_determinant(mainmatrix)

        messagebox.showinfo("Result", f"Determinant: {determinant_value}")
    def rank_dimension_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

        
        rank, dimensions = MatrixOperations.rank_and_dimensions(mainmatrix)

        messagebox.showinfo("Result", f"Rank: {rank}, Dimensions: {dimensions}")
    def inverse_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

    
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

        eigenvalues = MatrixOperations.eigen_decomposition(mainmatrix)

        messagebox.showinfo("Result", f"Eigenvalues: {eigenvalues}")
    
    def input_constants(self):
        constants_frame = Frame(right_frame, bg='BLACK')  
        constants_frame.grid(row=10, column=1, columnspan=3, pady=10)

        Label(constants_frame, text="Enter constants", fg="white", bg="black", font=('ariel', 15)).grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        constants = []
        for i in range(len(self.matrix_vars)):
            constant_var = IntVar()
            Entry(constants_frame, width=4, textvariable=constant_var).grid(row=i + 1, column=2)

            constants.append(constant_var.get())

        return constants

    def cramer_cmd(self):
        mainmatrix = self.input_cmd()
        constants = self.input_constants()

        try:
            solutions = MatrixOperations.cramer(mainmatrix, constants)
            messagebox.showinfo("Result", f"Solutions: {solutions}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
     
    def jordan_decomposition_cmd(self):
        mainmatrix = []
        for i in self.matrix_vars:
            row_values = [var.get() for var in i]
            mainmatrix.append(row_values)

        jordan_basis = MatrixOperations.jordan_decomposition(mainmatrix)

        jordan_result = "Jordan Decomposition Matrix:\n"
        for row in jordan_basis:
            jordan_result += "\t".join(map(str, row)) + "\n"

        messagebox.showinfo("Result", jordan_result)

def main():
    root = tk.Tk()
    app = MatrixInputApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()