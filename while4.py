N= int(input("введите число"))
if N<=0:
    print ("число не подходит под условие ")
else:
    while N>1:
        if N%3 !=0:
            print ("alse")
            break
        N=N//3
    else:
        print ("true")

print("программа завершена")