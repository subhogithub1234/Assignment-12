x=int(input("Enter the number:"))
print("The next prime number of %d"%x,end=" is ")
while x!=0:
    c=0
    i=1
    while x>=i:
        if x%i==0:
            c+=1
        i+=1    
    if c==2:
        print(x)
        break
    x+=1
