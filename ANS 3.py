print("Prime numbers under 100.....")
for i in range(2,100):
    c=0
    for n in range(2,i):
        if i%n==0:
            c+=1
    if c==0:
        print(i)        