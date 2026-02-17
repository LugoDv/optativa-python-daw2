#String 

my_string = "hola"
my_other_string = "como estan?"

print(len(my_string))
print(len(my_other_string))

print(my_string + my_other_string)
print(my_string +" "+ my_other_string)

print("Este es un String\n con salto de linea")

print("\t agrego un tab")

my_scape_string = "\\t Este es un string \\n escapado"
print(my_scape_string)

name,surname,age = "fabian","lugo","29"

print("mi nombre es "+name+ ", mi apellido "+surname+" y mi edad " + age)

print("mi nombre es %s, mi apellido es %s y mi edad %s " % (name,surname,age))

print("mi nombre es {}, mi apellido es {} y mi edad es {}".format(name,surname,age))

print(f' hola como estan {my_other_string}')

#Desempaquetado

lenguaje = "python"

a,b,c,d,e,f = lenguaje

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#slicing
lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:]
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2:]
print(lenguaje_slice)

#Reverse
reversed_lenguaje = lenguaje[::-1]
print(reversed_lenguaje)

print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.count("t"))
print(lenguaje.isnumeric())
print("1".isnumeric())
print(lenguaje.lower())
print(lenguaje.upper().isupper())
print(lenguaje.startswith("py"))