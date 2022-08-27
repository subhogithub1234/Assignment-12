print("Enter the two numbers:")
x,y=int(input()),int(input())
if x>y:
    min1=y
else:
    min1=x
while min1:
    if min1%x==0 and min1%y==0:
        lcm=min1
        break
    min1+=1
print("LCM of %d and %d is %d"%(x,y,lcm) )           