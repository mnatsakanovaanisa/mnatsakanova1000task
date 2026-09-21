try:
    N= int (input("введите N,> 0"))
    if N <=0:
        print("N должно быть больше 0")
    else:
        A= 1
        i=N
        while i>0:
            A*=i
            i-=2
        print(f"{N}!! = {A}")
except ValueError:
    print("введено не целое число")