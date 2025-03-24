Algoritmo sin_titulo
	Definir valor Como Real
    Definir i, mayor_0_menor_10, entre_10_100, mayor_100, negativos, iguales_0 Como Entero
	
    // Inicializaci�n de contadores
    mayor_0_menor_10 <- 0
    entre_10_100 <- 0
    mayor_100 <- 0
    negativos <- 0
    iguales_0 <- 0
	
    // Leer 100 valores
    Para i <- 1 Hasta 100 Hacer
        Escribir "Ingrese el valor ", i, ": "
        Leer valor
		
        // Clasificaci�n del valor
        Si valor > 0 Y valor < 10 Entonces
            mayor_0_menor_10 <- mayor_0_menor_10 + 1
        Sino
            Si valor >= 10 Y valor <= 100 Entonces
                entre_10_100 <- entre_10_100 + 1
            Sino
                Si valor > 100 Entonces
                    mayor_100 <- mayor_100 + 1
                Sino
                    Si valor < 0 Entonces
                        negativos <- negativos + 1
                    Sino
                        Si valor = 0 Entonces
                            iguales_0 <- iguales_0 + 1
                        Fin Si
                    Fin Si
                Fin Si
            Fin Si
        Fin Si
    Fin Para
	
    // Mostrar resultados
    Escribir "Resultados:"
    Escribir "Cantidad de valores mayores a 0 y menores a 10: ", mayor_0_menor_10
    Escribir "Cantidad de valores entre 10 y 100 (inclusive): ", entre_10_100
    Escribir "Cantidad de valores mayores a 100: ", mayor_100
    Escribir "Cantidad de valores negativos: ", negativos
    Escribir "Cantidad de valores iguales a 0: ", iguales_0
FinAlgoritmo
