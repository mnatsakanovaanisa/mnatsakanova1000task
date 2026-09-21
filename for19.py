try:
    N=int(input("введите целое число > 0"))
    if N<=0:
        print(" N должно быть больше 0")
    else:
        F=1
        for i in range(1, N + 1):
            F*=i
        print(f"{N}!={F}")
except ValueError:
    print("введено не целое число")