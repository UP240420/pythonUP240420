Algoritmo sin_titulo
		Definir suma Como Real
		Definir promedio Como Real
		Definir valor Como Real
		Definir i Como Entero
		
		suma <- 0
		
		Para i <- 1 Hasta 10 Con Paso 1 Hacer
			Escribir "Ingrese el valor ", i, ": "
			Leer valor
			suma <- suma + valor
		Fin Para
		
		promedio <- suma / 10
		
		Escribir "La suma de los valores ingresados es: ", suma
		Escribir "El promedio de los valores ingresados es: ", promedio
FinAlgoritmo

