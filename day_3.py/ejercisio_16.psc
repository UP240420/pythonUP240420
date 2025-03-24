Algoritmo sin_titulo
	// Declarar variables
    Definir i, contador Como Entero
    Definir suma, promedio, numero Como Real
	
    // Inicializar variables
    suma <- 0
    contador <- 0
	
    // Ingresar 10 valores
    Para i <- 1 Hasta 10 Hacer
        Escribir "Ingresa el valor ", i, ":"
        Leer numero
		
        // Verificar si el n�mero est� en el rango [5, 2500]
        Si numero >= 5 Y numero <= 2500 Entonces
            suma <- suma + numero
            contador <- contador + 1
        FinSi
    FinPara
	
    // Calcular el promedio si hay valores en el rango
    Si contador > 0 Entonces
        promedio <- suma / contador
        Escribir "El promedio de los valores en el rango es: ", promedio
    Sino
        Escribir "No hay valores dentro del rango [5, 2500]."
    FinSi
FinAlgoritmo