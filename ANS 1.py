x=int(input("Enter a number:"))
z=x
s=0
while z!=0:
    r=z%10
    s=s*10+r
    z//=10
print("Reverse of the number is",s)    
