#wap to calculate the grade of students from his marks
#Author- Parth1105
#date- 21-08-23

marks=int(input("enter your marks \n"))
if marks>=90:
    grade="Ex" #90-100=Ex
elif marks>=80:
    grade="A" #80-90=A
elif marks>=70:
    grade="B" #70-80=B
elif marks>=60:
    grade="C" #60-70=C
elif marks>=50:
    grade="D" #50-60=D
else:
    grade="F" #marks<50=F
print("your grade is "+grade)
