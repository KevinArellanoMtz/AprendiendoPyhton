#Kevin Luis Arellano Martinez
#Matricula 1878209
#haremos un programa donde usaremos el ciclo while con un break
#donde pediremos un numero y este sera acumulado en una variable
Totalacumulado=int(0)
numeroquepediremos=str("")
#ahora usaremos el ciclo while "en lo personal no lo he utilizado mucho"
while True :
    numeroquepediremos=input("Deme un numero y yo lo ire acumulando")
    #aqui creo que se entiende bien le pedimos un numero para irlo acumulando y usaremos un si
    #verificar la condicion
    if numeroquepediremos=="":
        print ("Listo, acabe de acumular por hoy :)")
        break
    else:
        #la verdad no entendi  mucho lo de la suma incluyente
        #lo busque pero no encontre forma de entenderle
        Totalacumulado+=int(numeroquepediremos)
        sumadenumuero="El total que llevas es de : {}"
        print(sumadenumuero.format(Totalacumulado))




