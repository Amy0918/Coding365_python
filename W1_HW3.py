import math
num1=input()
num2=input()

num1=float(num1)
num2=float(num2)

summ=num1+num2
summ=summ*100
summ=int(summ)
summ=summ/100

dif=num1-num2
dif=dif*100
dif=int(dif)
dif=dif/100

pro=num1*num2
pro=pro*100
pro=int(pro)
pro=pro/100

quo=num1/num2
quo=quo*100
quo=int(quo)
quo=quo/100

print("Sum:%.2f"%abs(summ))
print("Difference:%.2f"%abs(dif))
print("Product:%.2f"%abs(pro))
print("Quotient:%.2f"%abs(quo))