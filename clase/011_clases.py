
# Defininión de una clase vacía
class MyEmptyPerson:

    pass

print(MyEmptyPerson)

print(MyEmptyPerson())

class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"

    def walking(self):
        print(f"{self.name} {self.surname} está caminando")    


fabian = Person("fabian","lugo")
print(f"{fabian.name} {fabian.surname}")

print(fabian.full_name)

fabian.walking()


fabian.full_name = "Andres (el loco de los gatos)"

print(fabian.full_name)




