#!/usr/bin/env python3
from pyswip import Prolog
import os
#Consulta a prolog, se obtiene el diagnóstico del animal
def query(prolog,x,y,z,mascota):
	querylist = list(prolog.query('diagnostico('+mascota+',Enfermedad,'+str(x)+','+str(y)+','+str(z)+')'))
	index = 1
	for element in querylist:
		print('Diagnostico '+str(index)+': '+element['Enfermedad'])
		index += 1
	if (querylist == []):
		print('No hay diagnostico') 
	a = input()
#Menú principal
def  main_menu(prolog):
	os.system('clear')
	while True:
		print ('***************Bienvenido PetDiag PL***************')
		print ('Puede pulsar Ctrl+C para salir en cualquier momento')
		print ('Elije que animal deseas diagnosticar')
		selection = input ('1. Perro.\n2. Gato.\n3. Salir.\n')
		if (selection == '1'):
			menu_perro(prolog)
		elif (selection == '2'):
			menu_gato(prolog)
		elif (selection == '3'):
			break
		os.system('clear')
	print ('Hasta la próxima!.') 
#Posibles síntomas de perros
def menu_perro(prolog):
	x = 0; y = 0; z = 0
	print('Ingresa s/n a las siguientes preguntas.\n¿Tu perro tiene...')
	x += pregunta('-Diarrea?.',1)
	x += pregunta('-Fiebre?',1)
	x += pregunta('-Gases?',1)
	x += pregunta('-Deshidratación?',1)
	x += pregunta('-Letargo?',1)
	y += pregunta('-Vomito?',2)
	y += pregunta('-Adelgazamiento?',2)
	z += pregunta('-Debilidad?',3)
	z += pregunta('-Desmayos?',3)
	z += pregunta('-Respiración acelerada?',3)
	#debug
	#print(str(x)+","+str(y)+","+str(z))
	a = input()
	query(prolog,x,y,z,'perro')
#Posibles sitomas de gatos
def menu_gato(prolog):
	x = 0; y = 0; z = 0
	print('Ingresa s/n a las siguientes preguntas.\n¿Tu gato tiene...')
	x += pregunta('-Diarrea?.',1)
	x += pregunta('-Vómito?',1)
	x += pregunta('-Pérdida de apetito?',1)
	x += pregunta('-Dolor abdominal?',1)
	x += pregunta('-Debilidad?',1)
	y += pregunta('-Tos?',2)
	y += pregunta('-Estornudos?',2)
	y += pregunta('-Secreción nasal?',2)
	z += pregunta('-Somnolencia?',3)
	z += pregunta('-Anemia?',3)
	z += pregunta('-Tumores?',3)
	#debug
	#print(str(x)+","+str(y)+","+str(z))
	a = input()
	query(prolog,x,y,z,'gato')
#Método que generaliza la optención de puntos y el formato de la pregunta
def pregunta(a,n):
	#Dependiendo de la longitud de la pregunta, se aplica una tabulación diferente
	if(len(a) < 8):
		seleccion = input (a+'\t\t\t')
	elif(len(a) < 14):
		seleccion = input (a+'\t\t')
	else:
		seleccion = input (a+'\t')
	if (seleccion == 's') :
		return n
	else:	
		return 0
	
#Conección con prolog
try:
	prolog = Prolog()
	prolog.consult("basededatos.pl")
	#Menú de consulta
	main_menu(prolog)
except FileNotFoundError:
	print ("Error, el archivo basededatos.pl no se encuentra en el directorio actual")
except KeyboardInterrupt:
	print ("Hasta la próxima!")
