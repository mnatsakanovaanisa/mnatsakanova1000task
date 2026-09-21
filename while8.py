try:
    N=int(input("введите целое число, > 0"))
    if N<= 0:
        print("N должно быть больше 0")
    else:
        K= 0
        while (K + 1)**2 <= N:
            K+=1
        print(f"наибольшее число K, что K^2<={N}, равно{K}")
except ValueError:
    print("введено не целое число")