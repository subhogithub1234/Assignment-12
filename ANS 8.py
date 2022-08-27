n=int(input("Enter the value of N:"))
t1=0
t2=1
print(t1,sep="\n")
nextno=0
for i in range(2,n+1):
      t1=t2
      t2=nextno
      nextno=t1+t2
      print(nextno)