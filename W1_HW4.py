a,b,c=map(int,input().split())

a=int(a)
b=int(b)
c=int(c)

def triangle(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        if a==b==c:
            print("2")
        elif (a==b) or (b==c) or (c==a):
            print("3")
        else: print("4")
    else: print("1")

triangle(a,b,c)



