try:
    X=float(input("введите вещественное число, |X| <1"))
    N=int(input("введите целое число, > 0"))
    if abs(X)>= 1:
        print("|X| должно быть меньше 1")
    else:
        s= 0
        for i in range(1, N+1):
            s+=( (-1)**(i-1)) *(X**i)/i
        print(f"приближённое значение ln(1 + {X}) = {s}")
except ValueError:
    print("введено не число")