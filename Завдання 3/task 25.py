number=int(input('Ведіть число: '))
for i in range(1,number+1):
    mult = number * i #Multiplication
    print(str(number) + '*'+ str(i) + '=' + str(mult))
import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Кучерук Євгеній')

