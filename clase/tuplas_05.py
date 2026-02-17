my_tupla = tuple()

my_other_tupla = ()

my_tupla = (35, 1.60,"Geral", "Lopez")

print(my_tupla)
print(type(my_tupla))

print(my_tupla[0])
print(my_tupla[-1])

print(my_tupla.count("Geral"))

print(my_tupla.index("Geral"))

# my_tupla[1] = 1.80
print(my_tupla)

my_sum_tuple = my_tupla + my_other_tupla
print(my_sum_tuple)

my_tupla = list(my_tupla)
print(type(my_tupla))

my_tupla[2] = "Ilerna"
my_tupla.insert(1,"Verde")
print(my_tupla)

my_tupla = tuple(my_tupla)
print(my_tupla)
print(type(my_tupla))

del my_tupla
# print(my_tupla)