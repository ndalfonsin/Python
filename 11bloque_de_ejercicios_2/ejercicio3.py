""" PROGRAMA QUE COMPRUEBE SI UNA VARIABLE ESTA VACIA Y SI ES ASI RELLENARLA CON UN TEXTO EN
MINUSCULA Y QUE LO MUESTRE EN MAYUSCULA
"""
texto = ""

if len(texto.strip()) <= 0:
   texto = "asdghjsg"
   print(texto.upper())
else:
   print(f"la variable tiene contenido {texto}")

