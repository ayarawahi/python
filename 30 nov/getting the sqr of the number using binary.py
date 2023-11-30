def search_n(x):
    li,hi=1, x
    if (x==1 or x==0):
        return x
    while (li<=hi):
        mid=(hi+li)//2
        if (mid*mid == x):
            return mid
        elif(mid*mid < x):
            li=mid+1
        else:
            hi= mid -1
    return -1

    
num=int (input("num"))
tar_key=search_n(num)

print (tar_key)
