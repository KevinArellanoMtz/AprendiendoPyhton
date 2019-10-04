#Kevin Luis Arellano Martinez
#Matricula 1878209
#en este programa haremos tablas de multiplicar, asi es volveremos ala escuela
#no pediremos datos al usuario solo las hara automaticamente

for x in range(0,11):
    titulo= "tabla del {}"
    print(titulo.format(x))
    #el siguiente es un print para que se ponga un "espacio" entre cada print
    print()
    for y in range(0,11):
        loquesemostrara="{}x{}={}"
        print(loquesemostrara.format(x,y,x*y))
    else:
        print()
