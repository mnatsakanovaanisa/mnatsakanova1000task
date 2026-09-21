try:
    X=float(input("введите вещественное число"))
    N=int(input("введите целое число, > 0"))
    if N <=0:
        print("N должно быть больше 0.")
    else:
        s=X
        f= 1
        for i in range(2, N+1,2):
            f*=i*(i-1)
            s+=((-1) **(i//2))*(X**i)/f

        print(f"приближённое значение sin({X})={s}")
except ValueError:
    print("введено не число")