def Menor(a,b):
    return a<b

def DuplicarTexto(texto):
    return texto*2

def sumaHastaN(n):
    suma=0
    for x in range(0,n):
        suma+=x
    return suma
    

class Persona(object):
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.__edad=edad
    def __repr__(self) -> str:
        return f""" Persona:
        Nombre:{self.nombre}
        Edad:{self.__edad}
        """
    def getNombre(self) -> str:
        return self.nombre

    def getEdad(self) ->int:
        return self.__edad

per= Persona("Braslyn",22)
print(Menor(1,2))
print(DuplicarTexto("Hola"))
print(sumaHastaN(10))
print("var",12,sep='->',end='******\n')
print(per.nombre)
