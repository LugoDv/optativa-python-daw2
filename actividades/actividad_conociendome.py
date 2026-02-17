# punto numero 1
name = "Fabian"
age = 29
isStudent = True
# 1.1
print(f"{name} {age} {isStudent} ")
# 1.2
print(f"{type(name)} {type(age)} {type(isStudent)} ")

# 1.3
name = "Andres"
print(f"{name}")

# 2

hobbys = []
# punto numero 2
for i in range(3):
    hobbys.append(input("ingrese tres hobbys"))


print(hobbys)
print(len(hobbys))

gusto_modificados = hobbys *2

 

    
print(gusto_modificados)

# muestra un array con la palabra duplicada en cada posicion

# punto numero 3
favoriteLunch = ("espaguetis","tamales","empandas")

# al momento de modificar la tupla me dice que no se puede porque es inmutable
# es decir que no puede cambiar su valor
# favoriteLunch[1]="hola"

print(len(favoriteLunch))

# punto numero 4

# 1
numbers = {1,2,3,4,5,5,6}

# 2
print(numbers)

numbers = numbers | {7}
print(numbers)

# las estructuras de datos de tipo set no mermiten duplicado

# punto numero 5
print(type(name))
print(type(hobbys))
print(type(favoriteLunch))
print(type(numbers))

resume = [hobbys,favoriteLunch,numbers]

# se creó una lista con tres tipos de esctructas diferentes
print(resume)

# punto número 6

if(age < 18):
    print("Eres menor de edad")
elif (age>=18 and age <=30):
    print("Eres joven")
else:
    print("Eres adulto")

# segunda la edad ingresada muestra un mensaje u otro gracias que 
# acotamos limites con los if else             



