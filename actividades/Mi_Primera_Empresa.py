# Nonmbre: Johan Sebastian Neiva Martinez , Fabian Andres Lugo Muñoz
# Nombre empresa:  Otra vida
# Tipo de tienda: Libreria

def menu():
    print(
        """
==========================================
	1. Agregar Libro
	2. Buscar Libro
	3. Vender Libro
	4. Mostrar todos los libros 
	5. Mostrar datos de la empresa
	6. Mostrar datos del usuario
        7. Dejanos un comentario
	0. Salir
==========================================
		"""
    )

name_company = "OTRA VIDA"
type_company = "Libreria"
year_company = 2025
monthly_income = 5000
is_internatyonal = True

info_company = {
    name_company,
    type_company,
    year_company,
    monthly_income,
    is_internatyonal,
}

print(
    "\n==========================================================================================="
)
print(
    "============================ Bienvenido a: ",
    name_company,
    " ====================================",
)
print(
    "==========================================================================================="
)

username = input("\nIngrese nombre: ")
user_age = input("Ingrese edad: ")

while not (user_age.isnumeric()):
    user_age = input(
        "Error: La edad ingresada tiene que ser de tipo numerica, por favor, ingrese una edad correcta nuevamente: "
    )

print(
    "\nBienvenido",
    username.upper(),
    "a una de las mejores librerias del mundo.\n"
    "Estas preparado para una gran experiencia? ",
)

inventario_libros = [
    {
        "id": 101,
        "autor": "Gabriel García Márquez",
        "titulo": "Cien años de soledad",
        "genero": "Realismo Mágico",
        "precio": 18.50,
        "fragmento": "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo.",
    },
    {
        "id": 102,
        "autor": "Jane Austen",
        "titulo": "Orgullo y Prejuicio",
        "genero": "Novela Romántica",
        "precio": 12.99,
        "fragmento": "Es una verdad mundialmente reconocida que un hombre soltero, poseedor de una gran fortuna, necesita una esposa.",
    },
    {
        "id": 103,
        "autor": "George Orwell",
        "titulo": "1984",
        "genero": "Distopía",
        "precio": 15.00,
        "fragmento": "El Gran Hermano te está vigilando.",
    },
    {
        "id": 104,
        "autor": "Haruki Murakami",
        "titulo": "Tokio Blues (Norwegian Wood)",
        "genero": "Ficción Contemporánea",
        "precio": 19.99,
        "fragmento": "La muerte no es lo opuesto a la vida, sino una parte de ella.",
    },
    {
        "id": 105,
        "autor": "J.K. Rowling",
        "titulo": "Harry Potter y la Piedra Filosofal",
        "genero": "Fantasía Juvenil",
        "precio": 14.75,
        "fragmento": "El señor y la señora Dursley, de Privet Drive número cuatro, estaban orgullosos de poder decir que eran perfectamente normales, afortunadamente.",
    },
]

menu()
option = int(input("Seleccione la opcion a realizar: "))

while option != 0:
    if option == 1:
        print("Ingrese los siguientes datos del libro")

        book_id = input("Id: ")
        book_autor = input("Autor: ")
        book_title = input("Titulo: ")
        book_tipe = input("Genero: ")
        book_price = input("Precio: ")
        book_fragment = input("Pequeño fragmento del libro: ")

        nuevo_libro = {
            "id": int(book_id),
            "autor": book_autor,
            "titulo": book_title,
            "genero": book_tipe,
            "precio": float(book_price),
            "fragmento": book_fragment,
        }

        inventario_libros.append(nuevo_libro)

        print("\nLibro ingresado correctamente.")

    elif option == 2:
        book_title_find = input("Ingrese el titulo del libro que desea buscar: ")
        print(f"Buscando el libro: {book_title_find}...")
        encontrado = False
        titulo_buscar = book_title_find.lower().strip()
        for libro in inventario_libros:
            if titulo_buscar == libro["titulo"].lower().strip():
                print(
                    f"ID: {libro['id']} \nAutor: {libro['autor']} \nTítulo: {libro['titulo']} \nGenero: {libro['genero']} \nPrecio: ${libro['precio']:.2f} \nFragmento: {libro['fragmento']} \nCantidad Caracteres fragmento: {len(libro['fragmento'])}\n"
                )
                encontrado = True
                break
                
        if not encontrado:
            print("Libro no encontrado")
    elif option == 3:
        book_sale = int(input("Ingrese el id: "))
        vendido = False
        
        for libro in inventario_libros:
            if  book_sale == libro['id']:
                inventario_libros.remove(libro)
                print('Libro vendido con éxito')
                
                vendido = True
                break
            
        if not vendido:
            print('Ocurrio un problema en la venta del libro')
    elif option == 4:
        print("\n--- INVENTARIO DE LIBROS ---\n")
        for libro in inventario_libros:
            print(
                f"ID: {libro['id']} \nAutor: {libro['autor']} \nTítulo: {libro['titulo']} \nGenero: {libro['genero']} \nPrecio: ${libro['precio']:.2f} \nFragmento: {libro['fragmento']} \nCantidad Caracteres fragmento: {len(libro['fragmento'])}\n"
            )
    elif option == 5:
        print("\nDatos de la empresa: ", info_company)
    elif option == 6:
        print(f"\n--- DATOS DEL USUARIO ---\n")
        print(f"Nombre: {username.upper()}")
        print(f"Edad: {user_age}")
        print("\n---------------------------\n")
    elif option == 7:
        comment = input('\nIngrese tu comentario: ')
        letter_commet = input('\nGracias por tu comentario, ahora ingresa la letra que quieras saber que mas se repita en tu comentario: ')
        print('\nEn tu comentario existen ' , comment.count(letter_commet) , ' letras ' , letter_commet)
    else:
        print("Opción no válida. Intente de nuevo.")

    menu()
    option = int(input("Seleccione la opcion a realizar: "))

print("Fin del programa")
