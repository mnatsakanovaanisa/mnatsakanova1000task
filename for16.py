
try:
    A=float(input("введите вещественное числ "))
    N =int(input("введите целое число > 0"))
    if N<=0:
        print("N должно быть больше 0")
    else:
        P = 1
        for i in range(1, N+1):
            P*= A
            print(f"A^{i}={P}")
except ValueError:
    print("неправильный ввод")