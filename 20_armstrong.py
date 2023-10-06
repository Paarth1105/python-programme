num = int(input("enter the number: ")) #take input from the user
sum = 0
temp = num  #find the sum of the cube of each digit
while temp > 0: 
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    if num == sum:
        print(num,"is the armstrong number")
    else:
        print(num,"is not the armstrong number")