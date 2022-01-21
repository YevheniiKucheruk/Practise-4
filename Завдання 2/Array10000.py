from array import*
import datetime
import random
my_array=array('i',{})
for i in range(10000):
    number=random.randint(1,1000000)
    my_array.append(number)
print(my_array)

start_time = datetime.datetime.now()
Numerosity=len(my_array)
for j in range(Numerosity):
    key = my_array[j]
    i=j-1
    while i>=0 and my_array[i]>key:
        my_array[i+1]=my_array[i]
        i=i-1
    my_array[i+1]=key

print(my_array)
print(my_array.buffer_info())
time_taken=end_time-start_time
print('Час виконання алгоритму: '+str(time_taken), "секунд")
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Кучерук Євгеній')

