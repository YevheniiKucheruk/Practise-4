number=float(input('Введіть вашу магнітуду: '))
table=('Мікро (micro)','Дуже слабкий (very minor)','Слабкий (minor)','Легкий (light)','Помірний (moderate)','Сильний (strong)','Дуже сильний (major)','Великий (great)','Рідкісно великий (meteoric)')
if number <0:
    print('Ви ввели число менше нуля')
else:
    if number <2.0:
        print('Ваша магнітуда підходить під опис: ' + table[0])
    if 2.0<=number<3.0:
        print('Ваша магнітуда підходить під опис: ' + table[1])
    if 3.0<=number<4:
        print('Ваша магнітуда підходить під опис: ' + table[2])
    if 4.0<=number<5.0:
        print('Ваша магнітуда підходить під опис: ' + table[3])
    if 5.0<=number<6.0:
        print('Ваша магнітуда підходить під опис: ' + table[4])
    if 6.0<=number<7.0:
        print('Ваша магнітуда підходить під опис: ' + table[5])
    if 8.0<=number<9.0:
        print('Ваша магнітуда підходить під опис: ' + table[6])
    if 9.0<=number<10.0:
        print('Ваша магнітуда підходить під опис: ' + table[7])
    if number>=10.0:
        print('Ваша магнітуда підходить під опис: ' + table[8])
import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Кучерук Євгеній')

