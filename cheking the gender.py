gender=(input("enter ur gender"))

if(gender.lower()=="m"):
    age =int(input("enter ur age" ))
    if ( 24<age<30):
         print("accepte")
    else:
        print("rejected")
else:
    print("not pass")