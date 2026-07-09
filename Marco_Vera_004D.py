#hice lo que pude, gracias x todo

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")
    pass

def leer_opcion():
    try:
        opc= int(input("Ingrese una opción (1-6) \n:"))
        if opc >=1 and opc <=6:
            return opc
        else:
            print("Ingrese una opcion valida entre 1 y 6!")
    except ValueError:
        print("Error: Ingrese solo números enteros!")

def cupos_genero(gen, list_peliculas, cartelera): #OPCION 1
    cupos_disponibles=0
    for gen in list_peliculas:
        if list_peliculas[gen][1]== genero:
            cupos_disponibles += cartelera[gen][1]
    print(f"El total de cupos disponibles es: {cupos_disponibles}")
    pass

def buscar_codigo(codigo): 
    if codigo in cartelera:
        return True
    else:
        return False
    pass

def actualizar_precio(codigo, nuevo_precio): #OPCION 3
    buscar_codigo(codigo)
    if buscar_codigo(codigo)== True:
        cartelera[codigo][0]=nuevo_precio
        print("Precio actualizado correctamente!")
    else:
        print("El codigo no existe")
        return False
    
    pass

#validaciones
def validar_codigo(codigo):
    if codigo.strip=="" :
        return False
    else:
        if codigo in peliculas and cartelera:
            return False
        else:
            return True

def validar_titulo(titulo):
    if titulo.strip()=="":
        return False
    else: 
        return True

def validar_genero(genero):
    if genero.strip()=="":
        return False
    else: 
        return True

def validar_duracion(duracion):
    if duracion >0:
        return True
    else:
        return False
    
def validar_clasificacion(clasificacion):
    if clasificacion.upper() == "A" or  clasificacion.upper() == "B" or  clasificacion.upper() == "C":
        return True
    else:
        return False

def validar_idioma(idioma):

    if idioma.strip()=="":
        return False
    else:
        return True
    
def validar_3d(es_3d):
    if es_3d.lower()=="s":
        return True
    elif es_3d.lower()=="n":
        return False

def validar_precio(precio):
    if precio >0:
        return True
    else:
        return False

def validar_cupos(cupos):
    if cupos >=0:
        return True
    else:
        return False
#fin validaciones

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos): #OPCION 4
    if codigo in peliculas:
        return False
    else:
        peliculas[codigo]=[titulo, genero, duracion, clasificacion, idioma, es_3d]
        cartelera[codigo]=[precio, cupos]
        print("Pelicula agregada")
        return True

def eliminar_pelicula(codigo): #OPCION 5
    buscar_codigo(codigo)
    if buscar_codigo(codigo)==True:
        del peliculas[codigo]
        del cartelera[codigo]
        print("Se ha eliminado con exito la pelicula")
        return True
    
    else:
        print("El codigo no existe")
        return False
    
opc=0
peliculas = {#titulo, genero, duracion, clasificacion, idioma, es 3d
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}

cartelera = {#precio, cupo#
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}
while opc != 6:
    mostrar_menu()
    opc=leer_opcion()

    match opc:

        case 1: #listo
            genero= input("Ingrese género a consultar: ")
            cupos_genero(genero,peliculas,cartelera)
            pass

        case 2: #No pude realizarla debido a que se me complicó 
            pass

        case 3: #listo
            codigo_pelicula= input("Ingrese codigo de pelicula: ").upper()
            nuevo_precio= int(input("Ingrese nuevo precio: "))
            actualizar_precio(codigo_pelicula, nuevo_precio)
            

            pass

        case 4: #listo
            while True:
                codigo= input("Ingrese codigo de pelicula: ")
                validar_codigo(codigo)
                if validar_codigo(codigo)==True:
                    break
                else:
                    print("El codigo ya existe")
            while True:
                titulo= input("Ingrese titulo: ")
                validar_titulo(titulo)
                if validar_titulo(titulo)==True:
                    break
                else:
                    print("Ingrese un titulo valido! No espacios vacios!")
            while True:
                genero= input("Ingrese genero: ")
                validar_genero(genero)
                if validar_genero(genero)==True:
                    break
                else:
                    print("Ingrese un titulo valido! No espacios vacios!")
            while True:
                duracion= int(input("Ingrese duracion (minutos): "))
                validar_duracion(duracion)
                if validar_duracion(duracion)==True:
                    break
                else:
                    print("Ingrese una duracion valida mayor a 0!")
            while True:
                clasificacion= input("Ingrese clasificacion: ")
                validar_clasificacion(clasificacion)
                if validar_clasificacion(clasificacion)==True:
                    break
                else:
                    print("Ingrese una clasificacion valida! A, B o C!")
            while True:
                idioma= input("Ingrese idioma: ")
                validar_idioma(idioma)
                if validar_idioma(idioma)==True:
                    break
                else:
                    print("Ingrese un idioma valido! No espacios vacios!")
            while True:
                es_3d= input("¿Es 3d? (s/n): ")
                validar_3d(es_3d)
                if validar_3d(es_3d)==True:
                    break
                else:
                    break
            while True:
                precio= int(input("Ingrese precio: "))
                validar_precio(precio)
                if validar_precio(precio)==True:
                    break
                else:
                    print("Ingrese un precio valido mayor a 0!")
            while True:
                cupos= int(input("Ingrese cupos: "))
                validar_cupos(cupos)
                if validar_cupos(cupos)==True:
                    break
                else:
                    print("Ingrese una cantidad valida de cupos mayor o igual a 0!")  

            agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos)   
            print(peliculas)
            pass

        case 5: #listo
            codigo_eliminar= input("Ingrese el codigo de la pelicula a eliminar: ").upper()
            eliminar_pelicula(codigo_eliminar)
            pass
       
        case 6: #listo
            print("Programa finalizado.")
            break