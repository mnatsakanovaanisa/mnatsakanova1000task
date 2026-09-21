try:
    A=float(input("введите вещественное число "))
    N=int(input("введите целое число,> 0 "))
    if N<=0:
        print("N должно быть больше 0")
    else:
        C=1
        for i in range(1, N+1):
            C*=A
        print(f"{A}в степени {N}={C}")
except ValueError:
    print("неправильный ввод")