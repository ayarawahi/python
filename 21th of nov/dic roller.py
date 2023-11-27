def count_input (n):
    att=input("enter the attempts:").split(",")
    count=[]
    for i in range (1,n+1):
        count.append(att.count(str(i)))
    return count
def print_count(lst):
    for i in range (1,len(lst)+1):
        print("{}:{}".format(i,lst[i-1]))
    
def main():
    sides=int(input("enter the n of sides"))
    new_count=count_input(sides)
    print_count(new_count)
main()