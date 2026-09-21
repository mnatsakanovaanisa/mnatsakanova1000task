try:
    N =int(input("введите N > 1"))
    if N<=1:
        print("N должно быть больше 1")
    else:
        K=0
        S= 0
        while S+(K + 1)<=N:
            K+=1
            S +=K
        print(f"K ={K},сумма={S}")
except ValueError:
    print("введено не целое число")