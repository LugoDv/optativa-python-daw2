# 1. condición simple
print("1. condición simple \n") 
work_hours = 40
if work_hours > 0:
    print("Las horas fueron registradas correctamente")

# 2. uso del if y else
print("2. uso del if y else \n")
time_arrived = 8
if time_arrived <=8:
    print("Llegaste a tiempo")
else:
    print("Llegaste tarde")

# 3.Operadores lógicos (and)
print("3.Operadores lógicos (and) \n")
work_hours = 8
if work_hours >=0 and work_hours <=12:
    print("Las horas son correctas")

# 4. uso de elif
print("4. uso de elif \n")
minutes_delay = 20

if minutes_delay == 0:
    print("Llegaste a tiempo")
elif minutes_delay <=15:
    print("Llegaste un poco tarde")
else:
    print("Llegaste muy tarde")

        
# 5.String en condicionales
print("5.String en condicionales \n")
excuse = "Tráfico"
if excuse:
    print("Se ha registrado tu excusa:", excuse)   

# 6.Uso de not
print("6.Uso de not \n")
time_to_finish = "5:00 PM"

if not time_to_finish:
    print("No has registrado la hora de finalización")
else:
    print("La hora de finalización es:", time_to_finish)

    

             