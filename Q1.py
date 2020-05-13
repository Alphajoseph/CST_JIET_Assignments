ar = [1, 6, 5, 4, 5, 6, 4]
r = ar[0] 
for i in range(1,len(ar)): 
    r = r ^ ar[i] 
print("Element  is",r)
