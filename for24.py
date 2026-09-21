try:
    X =float(input("введите вещественное X"))
    N =int(input("введите целое N >0 "))
    if N<=0:
        print("N должно быть больше0")
    else:
        s=1
        f= 1
        for i in range(2,N+1,2):
            f*=i*(i -1)
            s+=((-1)**(i//2))*(X** i)/f
        print(f"приближённое значение cos({X})={s}")
except ValueError:
    print("введено не число")