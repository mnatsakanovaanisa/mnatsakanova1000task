try:
    N =int(input("ведите целое число, > 1"))
    if N<= 1:
        print("N должно быть больше 1")
    else:
        K=0
        С= 1 
        while С<N:
            A =С*3
            if A>=N:
                break
            С=A
            K+=1
        print(f"наибольшее K,что 3^{K}<{N} равно{K}")
except ValueError:
    print("введен не целое число")