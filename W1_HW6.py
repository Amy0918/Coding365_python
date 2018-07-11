a=float(input())
b=float(input())
c=float(input())


r=b*b-4*a*c
if r>=0 :
    if a==0 :
        x1=(-1)*c/b

        x1=x1*10.0
        x1=int(x1)
        x1=x1/10.0

        print("%.1f" % x1)
    else :
        x1=(-b+r**0.5)/(2*a)
        x2=(-b-r**0.5)/(2*a)

        x1=x1*10.0
        x1=int(x1)
        x1=x1/10.0

        x2=x2*10.0
        x2=int(x2)
        x2=x2/10.0

        print("%.1f" % x1)
        print("%.1f" % x2)
else:
    r=((-1)*(b*b-4*a*c))**0.5
    T1=((-1)*b)/(2*a)
    T2=r/(2*a)

    T1=T1*10.0
    T1=int(T1)
    T1=T1/10.0

    T2=T2*10.0
    T2=int(T2)
    T2=T2/10.0

    if T2 > 0 :
        print('%.1f+%.1fi'%(T1, T2))
        print('%.1f-%.1fi'%(T1, T2))
    else :
        T2=abs(T2)
        print('%.1f-%.1fi'%(T1, T2))
        print('%.1f+%.1fi'%(T1, T2))        
