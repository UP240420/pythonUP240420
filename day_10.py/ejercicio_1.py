#Itere de 0 a 10 usando el bucle for, haga lo mismo usando el bucle while

for i in range(11):
    print(i)
    i = 0
while i <= 10:
    print(i)
    i += 1

#Iterar de 10 a 0 usando el bucle for, haga lo mismo usando el bucle while.

for i in range(10, -1, -1):
    print(i)
    i = 10
while i >= 0:
    print(i)
    i -= 1

#Escribe un bucle que haga siete llamadas a print(), por lo que obtenemos en la salida el siguiente triángulo:

for i in range(1, 8):
    print('#' * i)

#Utilice bucles anidados para crear lo siguiente:

for i in range(5):  # 5 rows
    for j in range(5):  # 5 columns
        print('#', end=' ')
    print()

#multipicaciones

for i in range(11):
    print(f"{i} x {i} = {i * i}")

#Itere a través de la lista, ['Python', 'Numpy','Pandas','Django', 'Flask'] usando un bucle for e imprima los elementos.

my_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in my_list:
    print(item)

#Use el bucle for para iterar de 0 a 100 e imprimir solo números pares

for i in range(0, 101, 2):
    print(i)

#Use el bucle for para iterar de 0 a 100 e imprimir solo números impares

for i in range(1, 101, 2):
    print(i)



