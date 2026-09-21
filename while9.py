try:
    N= int(input("введите целое число, > 1"))
    if N<=1:
        print("N должно быть больше 1")
    else:
        K = 0
        С= 1 
        while С<=N:
            С*= 3
            K+= 1
        print(f"наименьшее K, что 3^{K}>{N},равно{K}")
except ValueError:
    print("введено не целое число")