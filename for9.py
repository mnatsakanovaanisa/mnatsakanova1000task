try:
    A=int(input("введите первое число"))
    B =int(input("введите второе число"))

    if A>= B:
        print("значения не подходят под условие A< B")
    else:
        C=0
        for i in range(A, B+1):
            C+=(i**2)
        print(f"произведение квадратов от {A} до {B} равна {C}")
except ValueError:
    print("введено не целое число")
