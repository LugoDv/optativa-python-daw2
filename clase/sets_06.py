my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Geral","Lopez",35}
print(my_other_set)
print(type(my_other_set))


my_other_set.add("Geral")
print(my_other_set)

print("Geral" in my_other_set)

my_other_set.remove("Geral")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set
