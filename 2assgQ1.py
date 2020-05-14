x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))
count=0
for i in range(1,x+1):
    if i%y==0 and i%z==0:
        count=count+1

print("special integer is",count)
