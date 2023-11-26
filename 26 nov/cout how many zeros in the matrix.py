s=0
matrix=[[0,5,1],
        [4,9,0],
        [11,0,7]]
for i in range (len(matrix)):
    for j in range (len(matrix)):
        if matrix [i][j] ==0:
            s+=1
print(s)
