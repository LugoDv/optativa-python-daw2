# bucle infinito 
my_condition = 0
# while my_condition < 0:
#     print("Estoy en un bucle infinito")

while my_condition <10:
    print(my_condition)
    my_condition +=2

else:
    print("Mi condición es mayor o igual que 10")

while my_condition < 10:
    print(my_condition)
    my_condition += 2

if my_condition ==10:
    print("Mi condición es igual a 10")

else:
    print("Mi condición es mayor o igual a 10")

print("La ejecución continúa aquí")      

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")


    print(my_condition)   

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
    break

    print(my_condition)

print("la ejecución continúa")

# Bucle for

my_list = [35, 24, 62, 52, 30,30,17]

for element in my_list:
    print(element)

my_set ={"fabian","lugo",29}
for element in my_set:
    print(element)                   

my_tupla = (35,1.77,"fabian","lugo","colombia")
for element in my_tupla:
    print(element)

my_dict = {
    "name":"fabian",
    "lastname":"lugo",
    "age":29,
    "country":"colombia"
}    
for element in my_dict:
    print(element)

for element in my_dict.values():
    print(element)

for element in my_dict.items():
    print(element)       


for element in my_dict:
    print(element)

    if element == "age":
        continue
else:
    print("El bucle for ha finalizado")    
        