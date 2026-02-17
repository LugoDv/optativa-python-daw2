def my_function():
    print("Hola desde mi función!")

my_function()
my_function()  

def sum_two_values(first_number, second_number):
    print(first_number + second_number)  

sum_two_values(5, 10)  

sum_two_values("5","7")  

def sum_two_values_with_return(first_number, second_number):
    return first_number + second_number

my_result = sum_two_values_with_return(10,5)
print(my_result)

name = "Juan"
surname = "Pérez"

def full_name(name, surname):
    print(f"{name} {surname}")

full_name(name, surname)    

full_name(name="Ana", surname="García")

def print_name_with_default(name,surname,alias="sin alias"):
    print(f"{name} {surname} ({alias})")

print_name_with_default("fabian","lugo")    

def print_upper_text(*texts):
    for text in texts:
        print(text.upper())

print_upper_text("hola","mundo","desde","funciones")
print_upper_text("python","es","genial")  