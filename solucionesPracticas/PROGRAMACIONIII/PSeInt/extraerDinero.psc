Algoritmo extraerDinero
	Definir saldoCuenta, montoExtraer Como Real;
	saldoCuenta = Aleatorio(0,50000);
	Escribir "Dinero disponible: ",saldoCuenta;
	Repetir
		
		Escribir "Ingrese Monto a extraer";
		Leer montoExtraer;
		si montoExtraer > saldoCuenta Entonces
			escribir "fondoinsuficiente"
		FinSi
		
	Hasta Que montoExtraer <= saldoCuenta y montoExtraer >=0
	saldoCuenta = saldoCuenta - montoExtraer;
	//instrucciones que entregan dinero
	Escribir "La operacion ha sido procesada"
	Escribir "Saldo actual: ",saldoCuenta; 
	
	
FinAlgoritmo
