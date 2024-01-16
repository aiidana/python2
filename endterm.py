import tkinter as tk
wind=tk.Tk()
wind.geometry('500x430')
wind.title('endterm')
"""
ref ->
rref
inverse ->
determinant ->
eigenvalue
eigenvector

dimension
rank
"""

def read_matrix(rows,cols):
    matrix=[]
    for i in range(rows.get()):
        rowss=[]
        for j in range(cols.get()):
            value = matrix_entries[i][j].get()
            rowss.append(float(value))
        matrix.append(rowss)
    return matrix
def ref(matrix):
    row=len(matrix)
    col=len(matrix[0])
    for i in range(row):
        piv=matrix[i][i] # -> 1
        if piv!=0:
            for element in matrix[i]:
                 matrix[i]=element/piv
        for j in range(i + 1, row):
             factor = -matrix[j][i]
             for index in range(col):
                   # Iterate over indices directly
                matrix[j][index] = matrix[j][index] + factor * matrix[i][index]
    return matrix
def determinant(matrix):
    row = len(matrix)
    col = len(matrix[0])  
    if row != col:
        return "Matrix is not square"
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
        determ += sign * matrix[0][i] * determinant(sub_mat)

    return determ
def calculate_determinant():
    
    wind2 = tk.Toplevel(wind)
    wind2.geometry('600x400')
    row_value = rows.get()
    col_value = cols.get()
    
    matrix_entries.clear()
    for i in range(row_value): 
        row_entries = []
        for j in range(col_value):
            entry = tk.Entry(wind2)
            entry.grid(row=i + 2, column=j)
            row_entries.append(entry)
        matrix_entries.append(row_entries)

    matrix = read_matrix(row_value, col_value)
    determinant_result = determinant(matrix)
    def res():
        result_label.config(text=f"Determinant: {determinant_result}")

    buttn = tk.Button(wind2, text='determinant=', command=res)
    buttn.place(x=100, y=400)
    
    result_label = tk.Label(wind2, text=f"Determinant: {determinant_result}")
    result_label.place(x=10, y=230)
    
    

# row=int(input('row:'))
# column=int(input('column:'))
# rr=read_matrix(row,column)

# res=determinant(rr)
# print(res)

rows=tk.IntVar()
entry_row=tk.Entry(wind,text=rows,width=20,font=('Arial',15),bg='black',fg='white')
entry_row.place(x=65,y=30)
lab_row=tk.Label(wind,text='  row:',font=('Arial',10))
lab_row.place(x=10,y=20)

cols = tk.IntVar()
entry_column=tk.Entry(wind,width=20,text=cols,font=('Arial',15),bg='black',fg='white')
entry_column.place(x=65,y=90)
lab_col=tk.Label(wind,text='column:',font=('Arial',10))
lab_col.place(x=10,y=70)


matrix_entries = []

#########################################################################################################################

bt1_ref=tk.Button(wind,text='ROW ECHELON FORM',bg='black',fg='white',width=30)
bt1_ref.place(x=130,y=180)

bt2_rref=tk.Button(wind,text='RREF',bg='black',fg='white',width=30)
bt2_rref.place(x=130,y=210)

bt3_inverse=tk.Button(wind,text='INVERSE',bg='black',fg='white',width=30)
bt3_inverse.place(x=130,y=240)

bt4_determinant=tk.Button(wind,text='DETERMINANT',command=calculate_determinant,bg='black',fg='white',width=30)
bt4_determinant.place(x=130,y=270)

bt5_eigval=tk.Button(wind,text='EIGENVALUE',bg='black',fg='white',width=30)
bt5_eigval.place(x=130,y=300)

bt6_eigvec=tk.Button(wind,text='EIGENVECTOR',bg='black',fg='white',width=30)
bt6_eigvec.place(x=130,y=330)

bt7_dimension=tk.Button(wind,text='DIMENSION',bg='black',fg='white',width=30)
bt7_dimension.place(x=130,y=360)

bt8_rank=tk.Button(wind,text='RANK',bg='black',fg='white',width=30)
bt8_rank.place(x=130,y=390)
wind.mainloop()






