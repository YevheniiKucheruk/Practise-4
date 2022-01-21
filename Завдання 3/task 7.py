water=int(input('Введіть кількість використаної води (в кубометрах): '))
suma=20
if water <=30:
    suma=suma+(water*9.86)
    suma=float('{:.2f}'.format(suma))
    print('Ваш рахунок за споживану воду: '+str(suma) + ' ГРН')
elif water >30:
    water=water-30
    suma=suma+(30*9.86)
    if water <=20:
        suma=suma+(water*11.22)
        suma=float('{:.2f}'.format(suma))
        print('Ваш рахунок за споживану воду: '+str(suma) + ' ГРН')
    elif water >20:
        water=water-20
        suma=suma+(20*11.22)
        if water <=10:
            suma=suma+(water*13.06)
            suma=float('{:.2f}'.format(suma))
            print('Ваш рахунок за споживану воду: '+str(suma) + ' ГРН')
        elif water >10:
            water= water-10
            suma=suma+(10*13.06)
            if water >1:
                suma=suma+(water*17.89)
                suma=float('{:.2f}'.format(suma))
                print('Ваш рахунок за споживану воду: '+str(suma) + ' ГРН')
import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Кучерук Євгеній')

        
        
