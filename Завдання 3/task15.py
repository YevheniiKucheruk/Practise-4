Letter =input('Введіть вашу букву з буквенної системи оцінювання: ')
if Letter == "A+" or Letter  == "A" or Letter  == "A-" or Letter  == "B+" or Letter  == "B" or Letter  == "B-" or Letter  == "C+" or Letter  == "C" or Letter  == "C-" or Letter  == "D+" or Letter  == "D" or Letter  == "F":
    if Letter  == "A+":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці >4.0')
    if Letter  == "A":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці 4.0')
    if Letter  == "A-":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці 3.7')
    if Letter  == "B+":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці 3.3.')
    if Letter  == "B":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці 3.0')
    if Letter  == "B-":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці 2.7')
    if Letter  == "C+":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці 2.3')
    if Letter  == "C":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці 2.0')
    if Letter  == "C-":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці 1.7')
    if Letter  == "D+":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці 1.3')
    if Letter  == "D":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці 1.0')
    if Letter  == "F":
        print('Ваша оцінка '+Letter+' еквівалентна оцінці 0')
else:
    print('Ваша введена буква не підходить в табличку')
import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Кучерук Євгеній')


