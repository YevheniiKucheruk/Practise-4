minutes=int(input('Введіть кільість використаних минут:'))
messages=int(input('Введіть кількість використаних текстових повідомлень:'))


if messages<=50 and minutes<=200:
    SumaForCustomers=45
    SumaForCompany=SumaForCustomers-(SumaForCustomers*0.05)-1.44
elif messages>=50 and minutes>=200:
    messages=messages-50
    minutes=minutes-200
    SumaForCompany=45+(messages*0.5)+(minutes*0.27)
    SumaForCustomers=SumaForCompany+1.44+(SumaForCompany*0.05)
    SumaForCompany=float('{:.2f}'.format(SumaForCompany))
    SumaForCustomers=float('{:.2f}'.format(SumaForCustomers))
elif messages<=50 and minutes>=200:
    minutes=minutes-200
    SumaForCompany=45+(minutes*0.27)
    SumaForCustomers=SumaForCompany+1.44+(SumaForCompany*0.05)
    SumaForCompany=float('{:.2f}'.format(SumaForCompany))
    SumaForCustomers=float('{:.2f}'.format(SumaForCustomers))
elif messages>=50 and minutes<=200:
    messages=messages-50
    SumaForCompany=45+(messages*0.5)
    SumaForCustomers=SumaForCompany+1.44+(SumaForCompany*0.05)
    SumaForCompany=float('{:.2f}'.format(SumaForCompany))
    SumaForCustomers=float('{:.2f}'.format(SumaForCustomers))

print("Базову плата за користування(без внесків та податків): " + str(SumaForCompany)+" ГРН")
print('Загальний рахунок для користувача: ' + str(SumaForCustomers)+" ГРН")
import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Кучерук Євгеній')
