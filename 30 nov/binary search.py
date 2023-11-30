def search_n(key,lst):
    li,hi=0, len(lst)-1
    while (li<=hi):
        mid=(hi+li)//2
        if (lst[mid] == key):
            return mid
        elif(lst[mid] < key):
            li=mid+1
        else:
            hi= mid -1
    return -1
num=[4,8,9,3,1,89,66]
num.sort()
print (num)
tar_key=int(input("trget num"))
res=print("your target is in index:",search_n(tar_key,num))

