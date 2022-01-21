radkiv=int(input('Введіть кількість рядків: '))
stovbciv=int(input('Введіть кількість стовбців: '))
matrix=[]
for i in range(radkiv):
    line=[]
    for j in range(stovbciv):
        number=int(input('Введіть число: '))
        line.append(number)
    matrix.append(line)

print()
print()

print('Матриця '+str(radkiv)+'x'+str(stovbciv) )
for i in matrix:
    for j in i:
        print(j, end= ' ')
    print()

        

