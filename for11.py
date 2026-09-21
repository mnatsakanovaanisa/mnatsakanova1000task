try:
    N= int (input("введите число "))
    if N<0:
        print ("число должно быть положительным")
    else:
        B=0
        for i in range (1, 2*N+1):
            B+=i**2
            print (f"сумма равна {B}")
except ValueError: 
    print("введено не целое число")