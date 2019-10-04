#Kevin Luis Arellano Martinez
#Matricula 1878209
#convertiremos las minusculas de cualquier nombre en mayusculas 
nombres= input(("Digame su nombre:"))
apellidos = input(("Digame sus apellidos:"))
#se piden datos logicamente y despues se usara una suma por asi decirlo para juntar los nombres y apellidos
#y usaremos un comando llamada .upper() para convertir todo en mayusculas
fullname= apellidos+ " " +nombres
print(fullname.upper())

