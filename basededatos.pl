enfermedad(perro, 'problema estomacal',1).
enfermedad(perro, 'problema del riñon',2).
enfermedad(perro, 'problema del corazon',3).
enfermedad(gato, 'problema gastrointestinal',1).
enfermedad(gato, 'alergia',2).
enfermedad(gato, 'leucemia felina',3).
diagnostico(Mascota,Enfermedad,X,Y,Z):-X>=3, enfermedad(Mascota,Enfermedad,1);Y>=4, enfermedad(Mascota,Enfermedad,2);Z>=6, enfermedad(Mascota,Enfermedad,3).
