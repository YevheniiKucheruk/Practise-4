T=float(input('Введіть початкову температуру(в °C ): ')) # початкова темепература
T1=float(input('Введіть кінцеву температуру(в °C ): '))# кінечна температура
m=float(input('Введіть масу води(в грамах): ')) # маса води
C=4.186

q=m*C*(T1-T)
q=float('{:.2f}'.format(q))
kWh = 0
money = 0
if q>0:
    print('Щоб досягнути цієї мети '+ str(T1)+ ' °C '+ ' треба додати ' + str(q) + ' Дж')
    kWh=q/(3.6*10**6)
    money=kWh*1.33
    print('Рахунок за нагрів води - ' + str(money)+' ГРН')
elif q<0:
    q=q*(-1)
    print('Щоб досягнути цієї мети '+ str(T1)+ ' °C '+ ' треба забрати ' + str(q) + ' Дж')
import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Кучерук Євгеній')
