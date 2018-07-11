a=int(input())
b=int(input())
c=int(input())

r=b*b-4*a*c
x1=((-b)+r**0.5)/(2*a)
x2=((-b)-r**0.5)/(2*a)

print("%.1f"%x1)
print("%.1f"%x2)