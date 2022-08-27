x=int(input("Enter the lower bound:"))
y=int(input("Enter the upper bound:"))
print("Prime numbers between",x,"to",y,"...")
n=0
for i in range(x,y+1):
   
    for n in range(2,i+1):
        if i%n==0:
           break
    if i==n:
        print(i)         