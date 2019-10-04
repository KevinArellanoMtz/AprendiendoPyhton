#Kevin Luis Arel
#Matricula 1878209
#haremos un programa que compruebe que un numero
#sea multiplo de 3,5 y 7 
#primero pediremos en numero a evaluar
numeroaevaluar=int(input("Dame un numero que sea multiplo de 3,5 o 7 : "))
#aqui se declara cuales son los multiplos de 3,5 y 7

multiplode3=((numeroaevaluar%3)==0)
multiplode5=((numeroaevaluar%5)==0)
multiplode7=((numeroaevaluar%7)==0)
#se usara un if es decir un si esta es un condicionador aqui usaremos and y or
#el and es una condicion (y) que compara dos cosas y estas dos tienen que ser verdaderas
#el or (o) se cumple si una de esas es verdadera
if ((multiplode3 and multiplode5) or multiplode7):
    print("Tu numero es correcto")
else:
    print("Tu numero no es correcto")