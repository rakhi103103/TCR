#fabonacii series
x=int(input("Enter number: "))
a=0
b=1
print("fabonacii series for ", x ," is ")

for i in range(x):
    print(a,end=" 2")
    a=b
    b=a+b
    
    

