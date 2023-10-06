num=int(input("enter the number : "))
prime=True
for i in range(2,num):
    if(num%i==0):#condition for prime number(divisible only by itself)
        prime=False #if condition false then if loop will break
        break
    if prime:
        print("this number is prime :")#if it is prime then it will print
    else:
            print("this number is not prime")
