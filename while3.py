N= int(input("введиет первое число"))
K=int (input("введите второе число"))
if N<=0 and K<=0:
    print ("числа должны быть положительными")
elif N==0 and K==0:
    print ("на 0 нельзя делить")
else:
    A=0
    B=N
    while B>=K:
        B-=K
        A+=1  
print ("частное равно", A)
print ("остаток равен", B)
        