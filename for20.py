try:
    N =int(input("введите целое число > 0 "))
    if N<=0:
        print("N должно быть больше 0")
    else:
        A=0
        F= 1
        for i in range(1, N + 1):
            F*= i 
            A+=F
        print(f"сумма 1!+2!+...+{N}!={A}")
except ValueError:
    print("введено не целое число")