x=int(input("Enter a number"))
c=0
i=0
for i in range(2,x):
    if x%i==0:
        c+=1
        break
if x==i+1:
    print(x,"is prime nunmber.")
else:
    print(x,"is not prime nunmber.")        