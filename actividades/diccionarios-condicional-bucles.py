alumnos ={}

alumnos["ana"]={
    "edad": 19,
    "curso":"DAW2",
    "lenguajes":{"Python","Java"},
    "nota":7.5
    }
alumnos["luis"]={
    "edad": 15,
    "curso":"DAW1",
    "lenguajes":{"C#","JavaScript"},
    "nota":8.0
    }
alumnos["marta"]={
    "edad": 20,
    "curso":"DAW2",
    "lenguajes":{"Python","HTML"},
    "nota":6.0
    }

print("Alumnos:")
# print(alumnos)

# Parte 2 – Mostrar alumnos
print("Parte 2 – Mostrar alumnos")

for alumno in alumnos:
    print("Alumno:", alumno)
    print("edad:", alumnos[alumno]["edad"])
    print("Curso:",alumnos[alumno]["curso"])
    print("Lenguajes:",alumnos[alumno]["lenguajes"])
    print("Nota media:",alumnos[alumno]["nota"])
    print()
    

# Parte 3 – Condicionales sobre notas
print("Parte 3 – Condicionales sobre notas")
result = ""

for alumno in alumnos:

    nota = alumnos[alumno]["nota"]

    if nota < 5:
        result = "Suspenso"
    elif nota >=5 and nota<7:
        result="Aprobado"
    elif nota >= 7 and nota<9:
        result ="Notable"
    else:
        result="Sobresaliente"    
                

    print("Alumno:", alumno)
    print("edad:", alumnos[alumno]["edad"])
    print("Curso:",alumnos[alumno]["curso"])
    print("Lenguajes:",alumnos[alumno]["lenguajes"])
    print(f"Nota media: {nota} -> {result}")
    print()

    
#  Parte 4 – Filtrar alumnos
print("Parte 4 – Filtrar alumnos")

for alumno in alumnos:

    if alumnos[alumno]["edad"]>18 and alumnos[alumno]["nota"] >=7:
        print("Alumno:", alumno)
        print("edad:", alumnos[alumno]["edad"])
        print("Curso:",alumnos[alumno]["curso"])
        print("Lenguajes:",alumnos[alumno]["lenguajes"])
        print("Nota media:",alumnos[alumno]["nota"])
        print()

   
# Parte 5 – While con menú
print("Parte 5 – While con menú")        
option =""
while option != 5:
    print("1.Mostrar alumnos")
    print("2.Buscar alumno")
    print("3.Añadir alumno")
    print("4.Media de todos los alumnos")
    print("5.Salir")
    option = int(input("Ingrese una opcion"))

    if option ==1:
        for alumno in alumnos:
            print("Alumno:", alumno)
            print("edad:", alumnos[alumno]["edad"])
            print("Curso:",alumnos[alumno]["curso"])
            print("Lenguajes:",alumnos[alumno]["lenguajes"])
            print("Nota media:",alumnos[alumno]["nota"])
            print()

    if option == 2:
        # Parte 6 – Buscar alumno
        print("Parte 6 – Buscar alumno")
        name = input("nombre del estudiante: ")

        if name in alumnos:
            print(alumnos[name])
        else:
            print("Alumno no encontrado")    

    if option == 3:
        # Parte 7 – Añadir alumno
        print("Parte 7 – Añadir alumno")

        name = input("Nombre: ")
        if name == "salir":
            break 
        age = input("Edad: ") 
        curso = input("Curso: ") 
        lenguajes = input("Lenguajes, separados por ',': ")
        nota = float(input("Nota: ")) 

        alumnos[name]={
            "edad":age,
            "curso":curso,
            "lenguajes":set(lenguajes.split(",")),
            "nota":nota

            }

    if option == 4:
        # Muestra la media de notas de todos los alumnos.
        print("Muestra la media de notas de todos los alumnos.")

        media = 0

        for alumno in alumnos:
            
            media+=alumnos[alumno]["nota"]

        media=media/len(alumnos)     

        print("La media es:", media)    

            
        
        
            
else:
    print("Saliste :)")



