a,b,c,d,e=map(int,input().split())


mean=(a+b+c+d+e)/5
var=((a-mean)**2+(b-mean)**2+(c-mean)**2+(d-mean)**2+(e-mean)**2)/5
dev=var**0.5

mean=mean*100
mean=int(mean)
mean=mean/100

var=var*100
var=int(var)
var=var/100

dev=dev*100
dev=int(dev)
dev=dev/100

print("%.2f"%mean)
print("%.2f"%var)
print("%.2f"%dev)
