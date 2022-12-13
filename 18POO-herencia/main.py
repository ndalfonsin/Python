"""
import clases

persona = clases.persona()
persona.setNombre("Nicolas")
persona.setApellidos("Alfonsin")
persona.setEdad("22 años")
persona.setAltura("1,78")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()} tiene {persona.getEdad()} y mide {persona.getAltura()} mts. ")
print(persona.hablar())

informatico= clases.informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martinezz")
informatico.setEdad("35 años")
informatico.setAltura("1,85")

mecanico = clases.mecanico()
mecanico.setNombre("Cristian")
mecanico.setApellidos("Martinezz")
mecanico.setEdad("19 años")
mecanico.setAltura("1,65")

print(f"La persona es: {informatico.getNombre()} {informatico.getApellidos()} tiene {informatico.getEdad()} y mide {informatico.getAltura()} mts. ")
print(informatico.getLenguajes())
print(f"La persona es: {mecanico.getNombre()} {mecanico.getApellidos()} tiene {mecanico.getEdad()} y mide {mecanico.getAltura()} mts. ")

"""