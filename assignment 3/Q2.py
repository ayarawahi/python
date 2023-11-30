def index_of_smallest_element():
    input_list=[]
    for i in range(10):
        num=int(input("enter the numbers"))
        input_list.append(num)
        print(input_list) 
    print("min = ",  input_list.index(min( input_list)))
index_of_smallest_element()     
        
