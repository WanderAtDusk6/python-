k=['banana',1,3.1415926,5,True,6,77,67,99]

for i in k:
    print(i,end=' ')
print(k[6])

k[0]='pineapple'
for i in k:
    print(i)

k.append('msj')
for i in k:
    print(i,end=' ')

