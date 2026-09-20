a=  float(input("Введите цену за 1 кг конфет: "))
if a<0:
    print ("цена не может быть отрицательной")
else:
    for b in range(1, 6):
         w= 1+ b*0.2
    c= a*w
    print (f"стомость {w} кг конфет : {c}")