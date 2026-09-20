N= int (input("введите число "))
if N<0:
    print ("число должно быть положительным")
else:
    B=0
    for i in range (1, N+1):
        B+=1/i

print (f"сумма 1+1/2+/...1/{N} равна {B}")