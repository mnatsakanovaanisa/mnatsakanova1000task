try:
    N=int(input("введите целое N, > 1"))
    A=float(input("введите начало отрезка A "))
    B=float(input("введите конец отрезка B ,A <B "))
    if N<=1:
        print("N должно быть больше 1")
    elif A>=B:
        print("A должно быть меньше B")
    else:
        H=(B-A)/N
        p=[A+i*H for i in range(N+1)]
        print(f"длина отрезкф H={H}")
        print("точки разбиения:",*p)
except ValueError:
    print("введено не число")