from tienda import *

t= Tienda()

t.agregar_animales(Perro("Boxer", 2, 7))
t.agregar_animales(Gato("Angora", 2, 0.5))
t.agregar_animales(Gato("Persa", 2, 0.7))
t.agregar_animales(Pez("Golden", 0.5, 0.1 ))
t.agregar_animales(Pez("Coridora", 0.1, 0.01))
t.agregar_animales(Ave("Loro", 1, 0.5))
t.agregar_animales(Ave("Peirco", 1, 0.5))
t.agregar_animales(Ave("Cacatua", 1, 0.5))

for i in range(5):
    a=t.entregar_animal()
    print(a.saludar(), a.mostrar_informacion())
