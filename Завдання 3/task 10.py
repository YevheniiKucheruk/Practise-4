system=input('Введіть систему мір(англійська чи метрична): ')
if system == 'англійська' or system == 'Англійська' :
    hight=int(input('Введіть вашу висоту в дюймах: '))
    weight=int(input('Введіть вашу вагу в фунтах: '))
    BMI=703*(weight/(hight**2))  #IMT (Body mass index)
    BMI= float('{:.1f}'.format(BMI))
    print('Ваш ІМТ дорівнює- '+ str(BMI))
elif system =='метрична' or system =='Метрична':
    hight=int(input('Введіть вашу висоту в см: '))
    weight=int(input('Введіть вашу вагу в кг: '))
    BMI=(weight/((hight/100)**2))  #IMT (Body mass index)
    BMI= float('{:.1f}'.format(BMI))
    print('Ваш ІМТ дорівнює- '+ str(BMI))
import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Кучерук Євгеній')

    
