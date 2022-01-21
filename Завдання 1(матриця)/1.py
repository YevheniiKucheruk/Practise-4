radkiv=int(input('Введіть кількість рядків: '))
stovbciv=int(input('Введіть кількість стовбців: '))
n=[]
g=str()
for i in range(radkiv):
    for j in range(stovbciv):
        a=int(input())
        a='{:^4}'.format(a)
        n.append(a)
        j+=1
    print(n)
    g=str(g)+"\n"+str(n)
    n.clear()
print(g)
        
