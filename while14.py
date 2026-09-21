try:
    A=float(input("введите A, > 1"))
    if A <=1:
        print(" A должно быть больше 1")
    else:
        K=0
        S=0
        while S+ 1/(K +1)<A:
            K +=1
            S+=1 /K
        print(f"K ={K},сумма {S}")
except ValueError:
    print("введено не число ")
