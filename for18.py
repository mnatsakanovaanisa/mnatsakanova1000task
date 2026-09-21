try:
    A=float(input("введите вещественное число "))
    N=int(input("введите целое число, >0 "))
    if N<=0:
        print("N должно быть больше 0")
    else:
        T =1
        W=1
        for i in range(1, N+1):
            W*= A
            T +=W*((-1)**i)
        print("сумма", T)
except ValueError:
    print("неправильный ввод")