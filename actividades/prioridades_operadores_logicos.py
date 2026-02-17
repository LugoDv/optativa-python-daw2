# 5 ejemplos de prioridades de operadores lógicos (Python)

print(3 < 4 or ("Hola" > "Word" and 4 == 4))   
print((3 == 3) and (2 > 1) or (1 > 5))          
print(not 5 == 5 or 2 > 3)                     
print((1 > 0) and not ("a" < "b") or (3 != 3))  
print("b" > "a" and 2 < 3 and not (4 < 2))      

# Ejemplo de NOT
print("Ejemplo not 1:", not False)
print("Ejemplo not 2:", not (5 == 5))
print("Ejemplo not 3:", not (3 > 4))
print("Ejemplo not 4:", not ("a" in "abc"))
print("Ejemplo not 5:", not (True and False))