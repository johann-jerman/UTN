# String -> es cade caracteres declaran con doble comilla ""
variableTexto = "este es un string"
# Number -> es un tipo de dato numerico
variableNumerica = 2
# Boolean -> los buleanos son tipos de dato verdadero TRUE o falso FALSE
variableBuleano = True
# para saber que tipo de dato es podes usar type(ACA VA EL TIPO QUE QUERES SABER)
type(variableBuleano)
# Arrays son un un conjunto de elementos guardados separados por coma
variableArray = [1, 2, 3, 4, 5, 6]
# Tuplas son un array que no se puede modificar
# Los array y tuplas tienen metodos propios
variableTupla = (1, 2, 3, 4, 5, 6)
# Sets
myset = {
    "este es la clave": " este es el valor"
}
print(myset["este es la clave"])
# Declaracion de variables
saludo = "juan dijo 'andrea dijo' 'andrea miente'"

# Condicionales
edad = 18
if edad < 18:
    print("es menor de edad")
elif edad > 18:
    print("es mayor de edad")
else:
    print("tenes 18")
# Declaracion de funciones


def nombreFuncion(parametro):
    return parametro


print(nombreFuncion("hola soy el parametro"))
# Declaracion de iteradores
