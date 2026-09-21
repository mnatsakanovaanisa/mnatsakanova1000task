try:
    N= int(input("введите N,степень двойки и > 0"))
    if N <= 0:
        print("N должно быть больше 0")
    else:     
        A = N
        B = True
        while A > 1:
            if A% 2!= 0:
                B=False
                break
            A //= 2
        if not A:
            print("число не является степенью двойки")
        else:
            K=0
            A =N
            while A>1:
                A//= 2
                K+=1
            print(f" степень K={K}")
except ValueError:
    print("введено не целое число")