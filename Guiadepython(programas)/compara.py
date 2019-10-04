#Kevin Luis Arellano Martinez
#Matricula 1878209
#haremos un programa que compare dos numeros que le pediremos al usuario
numerouno= int(input("Dame un numero"))
numerodos= int(input("Dame otro numero"))
#usaremos un if para comparar y mostrar ademas usaremos signos de comparacion
if numerouno > numerodos:
    mayor= "{} es mayor que {}"
    print (mayor.format(numerouno,numerodos))
elif numerouno < numerodos:
    menor= "{} es menor que{}"
    print(menor.format(numerouno,numerodos))
else:
    iguales="{} es igual que{}"
    print (iguales.format(numerouno,numerodos))
