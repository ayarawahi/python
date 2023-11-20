m=0
ans="abaacbb"
user_ans=input("enter")
for i in range(len(ans)):
    if(user_ans[i]==ans[i]):
        m+=1
    else:
        print(i+1,end=" ")
print()
print(m,"out of",len(ans))
