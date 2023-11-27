word=["hi","this","is","aya"]
nn=int(input("Enter length: "))
def kword(w,n):
    result=[]
    longe=[]
    for s in range (len(w)):
        if (n > len(w[s])):
            result.append(w[s])
        else:
            longe.append(w[s])
    print("The words from the list is not longer than the givn number: ",nn)
    print(result)
    print("The words from the list are longer than the givn number: ",nn)
    print(longe)


kword(word,nn)
