def isertionsort(array):
    for step in range (1,len(array)):
        key=array[step]
        j=step-1
        while j >=0 and key <array[j]:
            array[j+1]=array[j]
            j=j-1
            array[j+1]=key
     
data=[1,2,5,7,9,0]
isertionsort(data)
print("sorte arra:")
print(data)
