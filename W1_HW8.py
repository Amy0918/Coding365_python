inp= int(input())
outp= int(input())
home= int(input())
intext= int(input())
outext= int(input())

priceA=0.08*inp+0.139*outp+0.135*home+1.128*intext+1.483*outext
priceB=0.07*inp+0.130*outp+0.121*home+1.128*intext+1.483*outext
priceC=0.06*inp+0.108*outp+0.101*home+1.128*intext+1.483*outext

A=183
B=383
C=983

if priceA < B:
    print(A)
    if priceA <= A :
        print(A)
    else:
        priceA=int(priceA)
        print(priceA)

elif priceB >= B and priceB < C:
    print(B)
    if priceB <= B :
        print(B)
    else:
        priceB=int(priceB)
        print(priceB)

else :
    print(C)
    if priceA <= C :
        print(C)
    else:
        priceC=int(priceC)
        print(priceC)
