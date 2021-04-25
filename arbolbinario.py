class Nodo:
    def __init__(self, nombre = None, edad = None, izqui = None, derecho = None):
       
       self.nombre = nombre
       self.edad = edad
       self.izqui = izqui
       self.derecho = derecho

    def _str_(self):
        return str(self.nombre, self.edad)
        
class binarios: 
    def __init__(self):
        self.raiz = None

    def agregar(self, elemento):
        if self.raiz == None:
            self.raiz = elemento
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if int(elemento.edad) >= int(aux.edad):
                    aux = aux.derecho
                else:
                    aux = aux.izqui
            if int(elemento.edad) >= int(padre.edad):
                    padre.derecho = elemento
            else:
                padre.izqui = elemento

 
    def  preorden(self, elemento):
        if elemento != None:
            print(elemento)
            self.preorden(elemento.izqui) 
            self.preorden(elemento.derecho) 

    def  postorden(self, elemento):
        if elemento != None:
            self.postorden(elemento.izqui) 
            self.postorden(elemento.derecho) 
            print(elemento)

    def  inorden(self, elemento):
        if elemento != None: 
            self.inorden(elemento.izqui) 
            print(elemento)
            self.inorden(elemento.derecho) 
                    
    def getRaiz(self):
        return self.raiz

if __name__ == "__main__":
    ab = binarios()
    while(True):
        print("---MENU---\n" +  
            "1. Agregar\n" +
            "2. preorden\n" + 
            "3. postorden\n" + 
            "4. inorden\n")

        num = input("Ingrese Opcion:\n")
        if num == "1":
            nombre = input("Ingrese nombre: \n")
            edad = input("Ingrese edad: \n")
            nod = Nodo(nombre, edad)
            ab.agregar(nod)
        elif num == "2":
            print("Impreso por preorden")
            ab.preorden(ab.getRaiz())
        elif num == "3":
            print("Impreso por postorden")
            ab.postorden(ab.getRaiz())
        elif num == "4":
            print("Impreso por inorden")
            ab.inorden(ab.getRaiz())
