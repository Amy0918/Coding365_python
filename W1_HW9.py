a,b,c=map(int,input().split())

a=int(a)
b=int(b)
c=int(c)


if a>0 and b>0 and c>0 and (a+b>c) and (a+c>b) and (b+c>a):
    if (a*a+b*b==c*c) or (b*b+c*c==a*a) or (a*a+c*c==b*b):
        print("Right Triangle")
    elif (a*a+b*b<c*c) or (b*b+c*c<a*a) or (a*a+c*c<b*b):
        print("Obtuse Triangle")
    else: 
        print("Acute Triangle")
else: print("Not Triangle")

