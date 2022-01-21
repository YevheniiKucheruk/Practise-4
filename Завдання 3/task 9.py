noise = int(input('Ввевіть рівень гучності (в дицибелах): '))
table= ('Відбійний молоток','Бензинова газонокосарка','Будильник','Тиха кімната')
if noise == 40:
    print('Ваш тип гучності: ' + table[3])
if noise == 70:
    print('Ваш тип гучності: ' + table[2])
if noise == 106:
    print('Ваш тип гучності: ' + table[1])
if noise == 130:
    print('Ваш тип гучності: ' + table[0])
if noise <40:
    print('Ваш шум нижчий за найтихіший(з таблиці): ' + table[3])
if noise>130:
    print('Ваш шум перевищує найгучніший шум(з таблиці): '+ table[0])
if 40<noise<70:
    print('Ваш шум знаходиться в проміжку: ' +table[3] +'-'+table[2])
if 70<noise<106:
    print('Ваш шум знаходиться в проміжку: ' +table[2] +'-'+table[1])
if 106<noise<130:
    print('Ваш шум знаходиться в проміжку: ' +table[1] +'-'+table[0])
import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Кучерук Євгеній')

