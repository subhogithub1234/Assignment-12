x=int(input("Enter a number"))
print("First %d prime numbers are..."%x)
n=0
for i in range(2,x**2):
    for n in range(2,i+1):
        if i%n==0:
            break
    if i==n:
       print(i)
       
