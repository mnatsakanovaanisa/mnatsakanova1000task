try:
    P=float(input("введите процент, 0<P<25"))
    if not (0<P<25):
        print("P должно быть между 0 и 25")
    else:
        S=1000
        K=0
        while S<=1100:
            S*=(1+P/100)
            K+=1
        print(f"количество месяцев ={K}, итоговый размер вклада={S}")
except ValueError:
    print("введено не число")