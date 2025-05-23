#if a num is divisble by 2, 3 or both
n=int(input("Enter a number : "))
if(n%2==0 and n%3!=0):
    print(n,"is divisble by 2")
if(n%2!=0 and n%3==0):
    print(n,"is divisble by 3")
if(n%2==0 and n%3==0):
    print(n,"is divisble by both 2 and 3")
if(n%2!=0 and n%3!=0):
    print(n," is not didvisble by 2 ,3 or both")