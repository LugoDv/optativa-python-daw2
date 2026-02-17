# Actividad – Métodos de cadenas en Python
# capitalize(), upper(), count(), isnumeric(), lower(), isupper(), startswith()




# Escribe un programa en Python que almacene una palabra en la variable language y muestre por pantalla la siguiente
# información utilizando métodos de cadenas:

# 1.     La palabra con la primera letra en
# mayúscula.

word = "lenguaje"
print(word.capitalize())

# 2.     La palabra completamente en mayúsculas.
print(word.upper())
# 3.     Cuántas veces aparece la letra en la
# palabra.
word = "lenguaje"
print(word.count('e'))
# 4.     Si la palabra está formada únicamente
# por números.
print(word.isnumeric())
# 5.     Una comprobación numérica usando el
# texto "1".
print("1".isnumeric())
# 6.     La palabra en minúsculas.
print(word.lower())
# 7.     Si la palabra está completamente en
# mayúsculas.
print(word.upper().isupper())

# 8.     Si la palabra comienza con "py".
print(word.startswith("py"))
# Nota: Todos
# los resultados deben mostrarse con print().