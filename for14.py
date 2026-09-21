try:
    N=int(input("ввведите целое число, > 0 "))
    if N <=0:
        print("N должно быть больше 0")
    else:
        S=0
        for i in range(1,N+1):
            S +=2*i-1
            print(S)
except ValueError:
    print("введено не целое числз")
