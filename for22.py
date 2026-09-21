try:
    X=float(input("ведите вещественное число"))
    N=int(input("введите целое число > 0"))
    if N<=0:
        print("N должно быть больше 0")
    else:
        s=1
        f=1
        for i in range(1,N+1):
            f*=i
            s+=(X**i)/f
        print(f"приближённое значение({X})={s}")
except ValueError:
    print("введено не число")