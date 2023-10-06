#greatest amongst 4 numbers
#Author= Parth1105
#date= 21/08/23

num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
num3=int(input("enter number 3: "))
num4=int(input("enter number 4: "))

if(num1>num4):
    f1=num1
else:           #compare between num1 and num4
    f1=num4
if(num2>num3):
    f2=num2      #compare between num2 and num3
else:
    f2=num3

if(f1>f2):
    print(str(f1)+"is greatest")
else:
    print(str(f2)+"is greatest")
