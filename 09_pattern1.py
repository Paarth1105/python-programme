#Program on star pattern 1
#Author= Parth1105
#date= 21/08/23

n=3
for i in range(3):
    print(""*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(""*(n-i-1))
