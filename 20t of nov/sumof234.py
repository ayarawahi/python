def sum_digit(x):
    
    sum1=0
    while(x!=0):
        sum1+=x%10
        x=x//10
    print(sum1)
        
sum_digit(234)