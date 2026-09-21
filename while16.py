try:
    P=float(input("введите процент P ,0< P < 50"))
    if not (0 <P<50):
        print("P должно бытьмежду 0 и 50")
    else:
        A=10
        B=0
        K =0
        while B<=200:
            K += 1
            B +=A
            A *= (1 +P/100)
        print(f"количество дней ={K}, суммарный пробег ={B}")
except ValueError:
    print("введено не число")