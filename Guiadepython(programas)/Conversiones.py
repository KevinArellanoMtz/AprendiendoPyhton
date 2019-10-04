#Kevin Luis Arellano Martinez
#Matricula 1878209
#Segundo programa
#Lo primero que haremos sera declarar una variable str
#str es un tipo de dato de cadena se determina entre ""
numero="19"
#con un sencillo comando que es type y el print mostrara el tipo de dato que es este 
print(type(numero))
#Y para convertir es como declarar una variable pero usamos int y lo asignamos
numero=int(numero)
#simple demostramos que el tipo de dato ha cambiado y usamos el print y el type de nuevo
print(type(numero))
#ya se demostro que el numero es int eso significa que es numerico
#usaremos el format para sustituir el {} para no tener que pasar espacio para mostrar el "numero"
#para esto  declaramos otra variable tipo string y utulizaremos los corchetes
informacion= "Este numero utlizado es un tipo de dato {}"
#ahora utilizamos el .format para cambiar lo por los corchetes y poner el contenido de la variable numero
print(informacion.format(numero))


