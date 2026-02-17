# 2.lista de precios
precios = [100, 200, 300, 400, 500,500]
#3. Empleado
empleado = ["Fabian",29,"Desarrollador","Barcelona"]
#4. print de la lista de precios
print("4. Analiza las listas")
print("precios:",precios)
# print del empleado
print("empleado:",empleado)
# elementos de la lista precios
print(len(precios))
print(len(empleado))
print(type(empleado))
print(type(precios))
#5.Accede a elementetos específicos
print("#5.Accede a elementetos específicos")
print("Primer elemento: ",empleado[0])
print("Tercer elemento: ",empleado[2])
print("Ultimo elemento: ",empleado[len(empleado)-1])
print("penúltimo elemento",empleado[-2])
#6.Actuallizar Información
print("6. Actualizar información")
empleado[-1]="Madrid"
print("Nueva ciudad:",empleado)
empleado.append("Devops")
print("Nuevo elemento",empleado)
empleado.insert(1,1)
print("Nuevo elemento en la segunda posición:",empleado)
#7 Eliminar información
print("7 Eliminar información")
precios.remove(300)
print("lista sin un precio",precios)
print("precio eliminado",precios.pop())
del(precios[1])
print("lista con precio eliminado por del",precios)
#8Combina listas:
print("8 Combina listas:")
datos_empresa = empleado + precios
print("Listas combinadas",datos_empresa)
#9 Aplica métodos de listas
print("9.Aplica métodos de listas")
precios = [100, 200, 300, 400, 500,500]
print("cuanta veces se repite:",precios.count(500))

copy_precios = precios.copy()
precios.clear()
print("copia:",copy_precios)
print(precios)
#10.Ordena y reorganiza:
ventas = [2,4,1,6,10,12]
ventas.sort()
print("Lista ordenada",ventas)
ventas.reverse()
print("Lista invertida",ventas)

#Punto de lenguajes

lenguajes = ["Go","Python","C++","C#"]


print("Los dos primeros:",lenguajes[:2])
lenguajes[2]="Java"
print("Nuevo lenguaje",lenguajes)
lenguajes.append("JavaScript")
lenguajes.pop(0)
print(lenguajes)

