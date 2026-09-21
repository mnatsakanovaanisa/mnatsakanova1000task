try:
    N=int(input("введте целое число > 0"))
    if N<=0:
        print("N должно быть больше 0")
    else:
        T=N
        A= 0
        while T> 0:
            W = T%10
            A=A* 10 +W
            T//= 10
        print(f"число справф налево{A}")
except ValueError:
    print("введено не целое число" )