
"""

def main():
    print("************************************************")
    print("Ingrese clave de producto (A, B, C): ")
    print("************************************************")
    datos()

def datos():
    try:
        tk = input()
        if (tk != "A") or (tk != "B") or (tk != "C"):
            break
        mp = int(input("Cual es el costo de la materia prima?: "))
    except:
        print("Datos incorrectos")
        main()
    else: 
        print(f"El precio total de venta es: {comprobacion(tk, mp)}")    
     

def comprobacion(tipo, costo):
    if tipo == "A":
        total = (costo * 1.8) + (costo * 0.2) + costo
        return total   
    elif tipo =="B":
        total = (costo * 1.9) + (costo * 0.3) + costo
        return total
    else:
        total = (costo * 2) + (costo * 0.4) + costo
        return total
    
main()
"""