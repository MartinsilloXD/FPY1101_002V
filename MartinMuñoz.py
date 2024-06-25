libros=[]
libros_vendidos=[]
generos=['ficcion','no ficcion','ciencia']

def registrar_libro():
    titulo=input("\n-- Ingrese titulo del libro: ").lower()
    while titulo=="":
        print("\nERROR: Debes ingresar el titulo del libro, reintente.")
        titulo=input("\n-- Ingrese titulo del libro: ").lower()
    autor=input("\n-- Ingrese autor del libro: ").lower()
    while autor=="":
        print("\nERROR: Debes ingresar el autor del libro, reintente.")
        autor=input("\n-- Ingrese titulo del libro: ").lower()
    print("\nGeneros de libro:\n- Ficcion\n- No Ficcion\n- Ciencia")
    genero=input("\n-- Ingrese uno de los generos mencionados: ").lower()
    while genero not in generos:
        print("\nERROR: El genero ingresado no existe, reintente.")
        genero=input("\n-- Ingrese uno de los generos mencionados: ").lower()
    try:
        precio=int(input("\n-- Ingrese el precio del libro: $"))
        stock=int(input("\n-- Ingrese cantidad stock del libro: "))
    except ValueError:
        print("\nERROR: Valor ingresado no valido, reintente.")
        return
    libros.append({
        'titulo' : titulo,
        'autor' : autor,
        'genero' : genero,
        'precio' : precio,
        'stock' : stock
    })
    print(f"\nEl libro '{titulo}' ha sido registrado con exito.")

def listar_libros():
    print("TITULO\t\tAUTOR\t\tGENERO\t\tPRECIO\t\tSTOCK")
    print("---------------------------------------------------------------------")
    for libro in libros:
        print(f"{libro['titulo']}\t\t{libro['autor']}\t\t{libro['genero']}\t\t${libro['precio']}\t\t{libro['stock']}")

def registrar_venta():
    stock_no_hay=0
    libro_vendido=input("\nIngrese titulo del libro vendido: ").lower()
    for libro in libros:
        if libro['titulo'] == libro_vendido:
            try:
                cantidad_vendida=int(input("\nIngrese cantidad vendida: "))
            except ValueError:
                print("\nERROR: Valor ingresado no valido, reintente.")
                return
            if libro['stock'] >= cantidad_vendida:
                libro['stock']-=cantidad_vendida
                venta_total=libro['precio']*cantidad_vendida
                print(f"""
        ---BOTELA---
                      
TITULO DEL LIBRO \t=\t{libro['titulo']}

CANTIDAD VENDIDA \t=\t{cantidad_vendida}

PRECIO X UNIDAD \t=\t${libro['precio']}

-----

VENTA TOTAL \t\t=\t${venta_total}

        --------------
""")
                print(f"\nVenta realizada, stock actual del libro: {libro['stock']}")

                libros_vendidos.append({
                    'titulo' : libro['titulo'],
                    'autor' : libro['autor'],
                    'genero' : libro['genero'],
                    'precio' : libro['precio'],
                    'stock' : libro['stock'],
                    'cantidad' : cantidad_vendida,
                    'total' : venta_total
                })
                stock_no_hay=1

            else:
                print(f"\nStock insuficiente, stock actual del libro {libro['titulo']}: {libro['stock']}")
                stock_no_hay=1
    if libro['titulo'] != libro_vendido and stock_no_hay==0:
        print(f"\nEl libro {libro_vendido} no existe.")


def imprimir_ventas():
    print("""
---REPORTE DE VENTAS---
[1] Imprimir todas las ventas
[2] Imprimir ventas por genero
""")
    try:
        opcion=int(input("\nIngrese opcion (1-2): "))
    except ValueError:
        print("\nERROR: Valor ingresado no valido, reintente.")
    if opcion==1:
        print("TITULO\tAUTOR\tGENERO\tPRECIO\tSTOCK\tCANT. VENDIDA\tVENTA TOTAL")
        print("-------------------------------------------------------------------------------------------")
        for libro in libros_vendidos:
            print(f"{libro['titulo']}\t{libro['autor']}\t{libro['genero']}\t${libro['precio']}\t{libro['stock']}\t{libro['cantidad']}\t\t${libro['total']}")
    elif opcion==2:
        print("\nGeneros de libro:\n- Ficcion\n- No Ficcion\n- Ciencia")
        genero_elido=input("\n-- Ingrese uno de los generos mencionados: ").lower()
        while genero_elido not in generos:
            print("\nERROR: El genero ingresado no existe, reintente.")
            genero_elido=input("\n-- Ingrese uno de los generos mencionados: ").lower()
        print("TITULO\tAUTOR\tGENERO\tPRECIO\tSTOCK\tCANT. VENDIDA\tVENTA TOTAL")
        print("-------------------------------------------------------------------------------------------")
        for libro in libros_vendidos:
            if libro['genero'] == genero_elido:
                print(f"{libro['titulo']}\t{libro['autor']}\t{libro['genero']}\t${libro['precio']}\t{libro['stock']}\t{libro['cantidad']}\t\t${libro['total']}")

def generar_archivo():
    nombre_archivo = 'Reporte de ventas.txt'
    with open(nombre_archivo,"w") as archivo:
        archivo.write("TITULO\tAUTOR\tGENERO\tPRECIO\tSTOCK\tCANT. VENDIDA\tVENTA TOTAL")
        archivo.write("\n-------------------------------------------------------------------------------------------")
        for libro in libros_vendidos:
            archivo.write(f"\n{libro['titulo']}\t{libro['autor']}\t{libro['genero']}\t${libro['precio']}\t{libro['stock']}\t{libro['cantidad']}\t\t${libro['total']}")

#main
while True:
    print(""" 
---MENU---
[1] Registrar libro
[2] Listar todos los libros
[3] Registrar venta
[4] Imprimir reporte de ventas
[5] Generar archivo '.txt'
[6] Salir del Programa
 """)
    try:
        opcion=int(input("Ingrese opcion (1-6): "))
    except ValueError:
        print("\nERROR: Opcion ingresada no valida, reintente.")
    if opcion==1:
        registrar_libro()
    elif opcion==2:
        listar_libros()
    elif opcion==3:
        registrar_venta()
    elif opcion==4:
        imprimir_ventas()
    elif opcion==5:
        generar_archivo()
    elif opcion==6:
        print("Terminando este fabuloso programa :)")
        break
    else:
        print("\nERROR: Solo ingrese opcion entre el 1 al 6, reintente.")
