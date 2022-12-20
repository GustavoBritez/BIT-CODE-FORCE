n = int(input())

while (n < 1 or n > 150):
    n = int(input())
menos = 0
suma = 0
contar = 0
contar2 = 0
for i in range(n):
    bit = input()
    if(bit.count("-") >= 2):
        menos = menos +1
    if(bit.count("+") >= 2):
        suma = suma +1
        
print (suma-menos)
