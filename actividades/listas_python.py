my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35,24,62,52,30,30,17]

print(my_list)
print(len(my_list))

my_other_list = [1,1.60,"Fabian","Lugo"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[3])
print(my_other_list[-1])#Último elemento
print(my_other_list[-2])#Penúltimo elemento

print(my_other_list.count("Fabian"))
print(my_list.count(30))


#Desempaquetado
age, height, name, surname = my_other_list
print(f'mi edad es: {age}, mi altura es {height} mi nombre es: {name} y mi apellido es {surname}')

name,heigth, age ,surname = my_other_list[2],my_other_list[1],my_other_list[0],my_other_list[3]

#Concatenación de listas
print(my_list + my_other_list)

my_list = "Hola Python"

print(my_list)
print(type(my_list))

my_list = [my_list]

print(type(my_list))

my_other_list.append("Ilerna")
print(my_other_list)

my_other_list.insert(1,"Azul")

print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

my_other_list.remove(1)
print(my_other_list)

print(my_other_list.pop())
print(my_other_list)

print(my_other_list.pop(2))
print(my_other_list)

del my_other_list[2]
print(my_other_list)

#Elimina todos los elementos que hay en una lista y la deja vacia
my_other_list.clear()
print(my_other_list)

#copia la lista  sin modificar la original
my_new_list = my_list.copy()
print(my_new_list)

#sort ordena la lista

my_list = [35,24,62,52,30,30,17]

my_list.sort()
print(my_list)

#reverse se utiliza para invertir el orden de los elementos de una
# lista exxistente

my_list.reverse()
print(my_list)
