it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#1.
print(len(it_companies))
#2.
it_companies.add('Twitter')
print(it_companies)
#3.
it_companies.update(['X', 'Steam', 'Instagram'])
print(it_companies)
#4.
it_companies.remove('Twitter')
print(it_companies)
#5. 
#Usar descartar, si el item no existe, no se tiene error, caso cotnrario de lo que pasa con remove. 
it_companies.discard('OLA')
print(it_companies)
