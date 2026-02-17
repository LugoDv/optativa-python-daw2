my_dict = dict()
print(type(my_dict))

my_other_dict = {}
print(type(my_other_dict))

my_other_dict ={
    "Nombre":"Juan",
    "Apellido":"Perez",
    "Edad":28,
    1:"Python"}



my_dict={
    "Nombre":"Juan",
    "Apellido":"Perez",
    "Edad":28,
    "lenguajes":{"Python","Swift","Kotlin"}
    }

print(my_other_dict)
print(my_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_other_dict["Nombre"])

my_dict["Nombre"]="Fabian"
print(my_dict["Nombre"])

my_dict["Direccion"]="Calle Falsa 123"
print(my_dict)

del my_dict["Direccion"]
print(my_dict)

del my_dict

print("geraldo" in my_other_dict)
print("Nombre" in my_other_dict)

print(my_other_dict.items())
print(my_other_dict.keys())
print(my_other_dict.values())

my_new_dict = dict.fromkeys(("Nombre",1))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_other_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_other_dict,(my_other_dict,"fabian"))
print(my_new_dict)