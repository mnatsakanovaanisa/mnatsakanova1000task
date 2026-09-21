try:
    N=int(input("введите целое число,> 0"))
    if N<=0:
        print("N должно быть больше 0")
    else:
        A=N
        while A>0:
            C=A%10
            print(C)
            A//=10
except ValueError:
    print("введено не целое число")