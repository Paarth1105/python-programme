#WAP calculate the bill amount
#author- Parth1105 
#date-28/08/23

n=input("Enter the name of item:")
v=float(input("Enter the value of item:"))
d=float(input("Enter the Discount of item in percentage:"))
cgst=float(input("Enter the cgst for given item in percentage:"))
sgst=float(input("Enter the sgst for given item in percentege:"))

ctax=v*(cgst/100) #calculate the ctax by dividing cgst by the 100 into value
stax=v*(sgst/100) #calculate the stax by dividing sgst by 100 into value
Discount=v*(d/100) #calculate the discount dividing discount by 100 into value

Total_amount=(v+ctax+stax)-Discount #formula to calculate the total amount

print("dailygo mart kokarud")
print("thanks for visiting ")
print("Name of item is:",n)
print("Total amount payable is:",Total_amount)
print("see you soon")