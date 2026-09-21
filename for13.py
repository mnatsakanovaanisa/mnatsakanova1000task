try:
    N =int(input("введите целое N, > 0 "))
    if N<=0:
        print("N должно быть больше 0")
    else:
        A=0
        for i in range(1,N+1):
            S=1+i*0.1
            A += S*((-1)**(i+1))
        print("сумма", A)
except ValueError:
    print("введено не целое число")