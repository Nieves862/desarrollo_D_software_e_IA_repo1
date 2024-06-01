Algoritmo intentosIngreso
	Definir intento Como Entero;
	Definir acceso, permite Como Logico;
	Definir claveG, claveI Como Caracter;
	intento = 0;
	permite = Verdadero;
	acceso= Falso;
	claveG = "clave123";
	Repetir
		Escribir "Ingrese la clave";
		Leer claveI
		intento = intento + 1;
		si claveG == claveI Entonces
			acceso = Verdadero;
			permite = Falso;
		SiNo
			si intento >= 3 Entonces
				Escribir "Intentos agotados. Clave Bloqueada"
				permite = Falso;
			SiNo
				Escribir "Error en la clave, ingresar de nuevo"
			FinSi
			
		FinSi
		
	
	Hasta Que no permite
	
	si acceso  Entonces
		Escribir "Bienvenido al sistema!"
	FinSi
	
FinAlgoritmo
