age = [22, 19, 24, 25, 26, 24, 25, 24]
#1.
st = set(age)
print(len(st))
print(len(age))
#2. La diferencia es que los tipo string, es un tipo de variable que nos sirve para almacenar
#caracteres, las listas, para almacenar varios caracteres dentro de una sola variable, los 
#tuple, es de misma forma una lista pero no nos permite modificarla, y los sets
#de misma forma son una manera de almacenar datos, con la diferencia de que estos no nos permiten
#repetir los mismos. 

#3.
sentence = "I am a teacher and I love to inspire and teach people"
word = set(sentence.split())
print(len(word))