a=[]
i=0
n=(int(input("enter the no of elements")))
for i in range(i,n):
  b=input("enter number")
  a.append(b)
print(a)  
uni = [x for n, x in enumerate(a) if x not in a[:n]]
print(uni)
b=sorted(uni)
print(b)
