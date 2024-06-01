Algoritmo calificaciones
	Definir calificacion Como Entero
	Escribir "Ingrese la calificación del estudiante"
	Leer calificacion
	Segun calificacion hacer
		10: 
			Escribir "El estudiante ha obtenido una calificación excelente"
		9: 
			Escribir "El estudiante ha obtenido una calificación sobresaliente"
		8: 
			Escribir "El estudiante ha obtenido una calificación buena"
		7: 
			Escribir "El estudiante ha aprobado"
		6,5,4,3,2,1: 
			Escribir "El estudiante ha reprobado"
		De Otro Modo: 
			Escribir "Calificación no válida"
	FinSegun
FinAlgoritmo