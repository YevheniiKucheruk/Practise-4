letter= input('Введіть літеру англійського алфавіту: ')
if letter == 'a' or letter == 'e'or letter == 'i' or letter == 'o' or letter == 'u'or letter == 'A' or letter == 'E'or letter == 'I' or letter == 'O' or letter == 'U':
    print('Введена літера ' + letter + ' є голосною')
elif letter == 'y' or letter == 'Y':
    print('Введена літера ' + letter + ' може бути голосною або приголосною')
else:
    print('Введена літера ' + letter + ' є приголосною')
import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Кучерук Євгеній')


