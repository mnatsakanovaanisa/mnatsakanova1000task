a=  float(input("Введите цену за 1 кг конфет: "))
if a<0:
    print ("цена не может быть отрицательной")
else:
    for b in range(1, 11):
        d=b/10
    c= a*d
    print (f"стомость {b} кг конфет : {c}")