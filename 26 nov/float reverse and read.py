
    



def read_float(n):
    res=[]
    for i in range (n):
        num=float(input("enter a number"))
        res.append (num)
    return res
def multiply (ls,factor):
    for i in range (len(ls)):
        ls[i]=ls[i]*factor
    return ls
def reverse(ls):
    ls.reverse()
    return ls
def main():
    my_list=read_float(3)
    number=int(input("enter the factor :"))
    new_list=multiply(my_list,number)
    final_list=reverse(new_list)
    print(final_list)
main()
    