#Kevin Luis Arellano Martinez
#Matricula 1878209
#ahora en el tercer programa haremos un programa que de numeros aleatorios
#pero para eso tenemos que saber, que hay que importar una libreria
#con el comando import viene especificado en la guia.
import random
#ya importada la libreria usaremos un comando llamadoo randrage
#este tiene que ir especificado con un rango claro esta
def sumadenumaleatorios():
    numerodos = float (random.randrange(1,10))
    numerouno= float (11.2)
    resultado =numerouno + numerodos
    print ("la suma de dos numeros aleatorios es " )
    print (resultado)

#este comando llama a ejecutar la funcion y solo queda probar

sumadenumaleatorios()