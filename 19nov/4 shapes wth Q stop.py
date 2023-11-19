shape=int(input("enter the number"))
if (shape==1):
    sum_a=0
    def shap_A(sum_a):
        high=float(input("enter the high"))
        base=float(input("enter the base"))
        sum_a=(1/2)*high*base
        return sum_a
    re=shap_A(sum_a)
    print(re)
     
elif(shape==2):
    sum_b=0
    def shap_B(sum_b):
        l=float(input("enter the l"))
        sum_b=l**2
        return sum_b
    resu=shap_B(sum_b)
    print(resu)
         
elif(shape==3):
    sum_C=0
    def shap_C(sum_C):
        r=float(input("enter the r"))
        sum_C=3.14*r**2
        return sum_C
    resul=shap_C(sum_C)
    print(resul)
    
elif(shape==4):
    sum_d=0
    def shap_d(sum_d):
        rr=float(input("enter the r"))
        hh=float(input("enter the hh"))
        sum_d=(2*3.14*rr*hh)+(2*3.14*rr**2)                     
        return sum_d
    result=shap_d(sum_d)
    print(result)
else:
    print("stop here")