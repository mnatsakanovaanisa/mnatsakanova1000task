A= int (input ("введите первое число"))
B= int(input ("введите второе число"))
if A>=B:
    print ("значения не подходят под условие A<B")
else:
    C=0
    for i in range(A, B+1):
        C +=i
        
print (f"сумма от {A} до {B} равна{C}")
