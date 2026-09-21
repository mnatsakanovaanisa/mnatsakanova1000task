try:
    N=int(input("введите целое число, > 0 "))
    if N<=0:
        print("N должно быть больше 0")
    else:
        P=1
        for i in range(1, N+1):
            P*=1+i*0.1
        print("произведение ", P)
except ValueError:
    print("введено не целое число")