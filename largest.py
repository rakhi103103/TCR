#largest of 3 number
n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
n3=int(input("enter 3rd number: "))

if(n1>n2)and(n1>n3):
    largest = n1
elif(n2>n1)and(n2>n3):
    largest = n2
else:
    largest = n3

print("Largest number : ",largest)