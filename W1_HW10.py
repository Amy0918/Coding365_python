import sys
#第一門課
numbera=int(input())
if (numbera < 999) or (numbera >= 10000):
    print("-1")
    sys.exit()  

hra=int(input())
if hra==1 :
    classa1=int(input())
    A=[classa1,0]

elif hra==2:
    classa1=int(input())
    classa2=int(input())
    A=[classa1,classa2]
else :
    print("-1")
    sys.exit()  

#第二門課
numberb=int(input())
if (numberb < 999) or (numberb >= 10000):
    print("-1")
    sys.exit() 

hrb=int(input())
if hrb==1 :
    classb1=int(input())
    B=[classb1,0]

elif hrb==2:
    classb1=int(input())
    classb2=int(input())
    B=[classb1,classb2]
else :
    print("-1")
    sys.exit()

#第三門課
numberc=int(input())
if (numberc < 999) or (numberc >= 10000):
    print("-1")
    sys.exit()

hrc=int(input())
if hrc==1 :
    classc1=int(input())
    C=[classc1,0]

elif hrc==2:
    classc1=int(input())
    classc2=int(input())
    C=[classc1,classc2]
else :
    print("-1")
    sys.exit()
 

if (A[0]//10 >0 and A[0]//10 <6) and (A[0]%10 >0 and A[0]%10 <9) and (B[0]//10>0 and B[0]//10<6) and (B[0]%10>0 and B[0]%10<9) and (C[0]//10>0 and C[0]//10<6) and (C[0]%10>0 and C[0]%10<9) :
    if A[0]==B[0] or A[0]==B[1] :
        print("%d,%d,%d"%(numbera,numberb,A[0]))
    if A[1]==B[0] or A[1]==B[1] :
        if A[1]!=0 :
            print("%d,%d,%d"%(numbera,numberb,A[1]))

    if A[0]==C[0] or A[0]==C[1] :
        print("%d,%d,%d"%(numbera,numberc,A[0]))
    if A[1]==C[0] or A[1]==C[1] :
        if A[1]!=0 :
            print("%d,%d,%d"%(numbera,numberc,A[1]))

    if B[0]==C[0] or B[0]==C[1] :
        print("%d,%d,%d"%(numberb,numberc,B[0]))
    if B[1]==C[0] or B[1]==C[1] :
        if B[1]!=0 :
            print("%d,%d,%d"%(numberb,numberc,B[1]))

    if A[0]!=B[0] and A[0]!=B[1] and A[1]!=B[0] and A[1]!=B[1] and B[0]!=C[0] and B[0]!=C[1] and B[1]!=C[0] and B[1]!=C[1] and A[0]!=C[0] and A[0]!=C[1] and A[1]!=C[0] and A[1]!=C[1] :
        print("correct")

else : print("-1")

