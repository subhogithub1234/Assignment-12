print("Enter the two numbers:")
x,y=int(input()),int(input())
z=min(x,y)
for i in range(1,z+1):
    if x%i==0 and y%i==0:
        gcd=i
print("HCF of %d and %d is %d"%(x,y,gcd))        
