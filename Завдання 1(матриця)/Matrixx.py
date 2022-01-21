radkiv=int(input('Введіть кількість рядків: '))
stovbciv=int(input('Введіть кількість стовбців: '))
matrix=str()
for i in range(radkiv):
    for j in range(stovbciv):
        line=input()
        line = '{:>4}'.format(line)
        matrix=matrix+line
    matrix=(matrix+'\n')
print(matrix)
import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Кучерук Євгеній')
