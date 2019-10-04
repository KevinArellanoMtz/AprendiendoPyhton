#Kevin Luis Arellano Martinez
#Matricula 1878209
#aqui haremos un prgrama que verificara si un numero es entero o no
#este sera proporcionado por el usuario
numeroaevaluar=input()
print(type(numeroaevaluar))
#aqui la verdad no lo entendi muy bien porque es la primera vez que lo uso
#por lo que entendi es algo de cierto y falso,y el .find busca un . para verificar si es float
siesentero=(numeroaevaluar.isdigit() and numeroaevaluar.find(".")==1)
if (siesentero):
    print("Tu numero es entero, correcto crack")
else:
    print("Tu numero no es entero, intentalo de nuevo crack")