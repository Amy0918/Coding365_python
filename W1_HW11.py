a1=int(input())
a2=int(input())

b1=int(input())
b2=int(input())

c1=int(input())
c2=int(input())

lona=a2-a1
lonb=b2-b1
lonc=c2-c1


if b1 > a2 :
    lon1=lona+lonb
    #print(lon1)
elif b2 > a2 :
    lon1=b2-a1
    #print(lon1)
else :
    lon1=a2-a1
    #print(lon1)

if (c1 > b2) and (c1 > a2) :
    lon2=lon1+lonc
elif c2 > b2 :
    if (b1 > a2) or (b2 > a2):
        lon2=lon1+(c2-b2)
    else:
        lon2=lon1+(c2-a2)
else:
    lon2=lon1

print(lon2)

