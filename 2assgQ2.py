a=int(input("enter a "))
b=int(input("enter b "))
gcd=0
if a<=b:
    leng=a
else:
    leng=b

if a==1 and b==1:
    gcd=1

else:
    for i in range(leng,0,-1):
        if a%i==0 and b%i==0:
            gcd=i
            break

print("GCD  of numbers is",gcd)
