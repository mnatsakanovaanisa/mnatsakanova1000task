try:
    N=int(input("введите целое число,> 0 "))
    if N<=0:
        print("N должно быть больше 0")
    else:
        sum=1
        f=1
        for i in range(1, N+1):
            f*=i
            sum+=1/f
        print(f"приближённое значение e ={sum}")
except ValueError:
    print("введено не целое число")