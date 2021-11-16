# Lenguaje Tipado Dinamico Duck typing)

car = "tesla"
print("modelo:", car)

car = "vw"
print("modelo:", car)

resultado = 2+2
print("res:", resultado)

resultado = 2.2-3.12 # floatante 
print("res:", resultado)

resultado = 2.2 > 3.12 # booleno falso/verdadero 
print("res:", resultado)

# nueva_variable = 12
# print("nueva", nueva_variable)

nueva_variable = 23 # pregunta de entrevistas 
# igual de asignacion =
# igual de comparacion ==
print("nueva", nueva_variable)

my_name="Isaias"
last_name="G"
num = 5
print(f"Lets talk about {my_name} {last_name}")
print(f"R {3+3} {7/num}")

texto = """
fsdfdsfds
   sdfdsf  dsf
s df  dsfdsfds
sdfd  sfsd
"""
# print(texto)


texto2 = "dzdsfdsfds" \
"fww dsfsdfds \n" \
"f dsfsdcxvfds "
print(texto2)
print("String {}".format("👽 alien"))

print("String {2}".format("👽",  "🤖", "😎"))

print("String {alien} {robot}".format(alien="👽", robot="🤖"))

print("*" * 33)

print( my_name +' '+ last_name)

formatter = "{}{}{}"
print(formatter.format(1,2,3))


formatter = "{2}{0}{1}"
print(formatter.format(1,2,3))