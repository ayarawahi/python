s=0
matrix=[[0,5,1],
        [4,9,0],
        [11,0,7]]

matrix2=[[5,3,4],
        [3,3,4],
        [5,6,7]]
def ad_mat(mat1,mat2):
    new_mat=[]
    for row in range (len(mat1)):
        rows=[]
        for cln in range (len(mat1)):
            rows.append(mat1[row][cln]+mat2[row][cln])
        new_mat.append(rows)
    print(new_mat)
ad_mat(matrix,matrix2)