#Iterar de 0 a 100 e imprimir la suma de todos los números:

total_sum = 0
for i in range(101):
    total_sum += i
print("The sum of all numbers is", total_sum)

#Iterar de 0 a 100 e imprimir la suma de todos los números pares y la suma de todos los impares:

sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print("The sum of all evens is", sum_evens, "And the sum of all odds is", sum_odds)
