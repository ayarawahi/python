import random
import string
n=int(input("enter the size"))
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters ) for i in range(length+1))

 
random_string = generate_random_string(n)
print(random_string)