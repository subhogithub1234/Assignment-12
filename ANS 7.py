print("Enter the two numbers:")
x,y=int(input()),int(input())
cop=0
for i in range(1,y+1):
    if x%i==0 and y%i==0:
        cop=i
if cop==1:
    print("numbers are co-prime.")
else:
    print("numbers are not co-prime.")        
