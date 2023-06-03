"""
crear un script que tenga 4 variables, una lista un string, un entero, un boolean y que imprima un
 mensaje segun el tipo de dato de cada variable
"""
def traducirTipo(tipo):
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "string"
    elif tipo == int:
        result = "entero"
    elif tipo == bool:
        result = "boolean"
    return result
    
def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test:
        print(f"este dato es tipo: {traducirTipo(dato)}")
    else:
        result = None

    return result


mi_lista = ["hola mundo", 77]
titulo = "master en python"
numero = 100
verdadero = True

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))


