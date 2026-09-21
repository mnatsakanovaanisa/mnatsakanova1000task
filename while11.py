try:
    N= int(input("введите N, > 1 "))
    if N<=1:
        print("N должно быть больше 1")
    else:
        K=0
        S=0
        while S< N:
            K+= 1
            S+=K
            print(f"K={K}, сумм={S}")
except ValueError:
    print("введено не целое число")