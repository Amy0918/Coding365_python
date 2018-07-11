x=input()
y=input()
z=input()

x=int(x)
y=int(y)
z=int(z)

total=0

if x>=1 and x<=10 :
        total +=380*x
elif x>10 and x<=20:
        total +=0.9*380*x
elif x>20 and x<=30:
        total +=0.85*380*x
elif x>30: 
        total +=0.8*380*x


if 1<=y and y<=10 :
        total +=1200*y
elif y>10 and y<=20:
        total +=0.95*1200*y
elif y>20 and y<=30:
        total +=0.85*1200*y
elif y>30: 
        total +=0.8*1200*y


if 1<=z and z<=10 :
        total +=180*z
elif z>10 and z<=20:
        total +=0.85*180*z
elif z>20 and z<=30:
        total +=0.8*180*z
elif z>30: 
        total +=0.7*180*z

print(int(total))
