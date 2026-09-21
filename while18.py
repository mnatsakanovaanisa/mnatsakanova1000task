try:
    N=int(input("введите целое ичсло, > 0"))
    if N<=0:
        print("N должно быть больше 0")
    else:
        A=N
        W= 0
        S=0
        while A >0:
            C= A%10
            W+= 1
            S+=C
            A//=10
        print(f"количество цифр ={W},сумма цифр ={S}")
except ValueError:
    print("введено не целое число")