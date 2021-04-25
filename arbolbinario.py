class Nodo:
    def __init__(self, dato = None, izqui = None, derecho = None):
       self.dato = dato
       self.izqui = izqui
       self.derecho = derecho

    def _str_(self):
        return str(self.dato)
        
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
                if int(elemento.dato) >= int(aux.dato):
                    aux = aux.derecho
                else:
                    aux = aux.izqui
            if int(elemento.dato) >= int(padre.dato):
                    padre.derecho = elemento
            else:
                padre.izqui = elemento

 
    def preorden(self, elemento):
        if elemento != None:
            print(elemento.dato)
            self.preorden(elemento.izqui) 
            self.preorden(elemento.derecho) 

    def postorden(self, elemento):
        if elemento != None:
            self.postorden(elemento.izqui) 
            self.postorden(elemento.derecho) 
            print(elemento.dato)

    def inorden(self, elemento):
        if elemento != None: 
            self.inorden(elemento.izqui) 
            print(elemento.dato)
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
            dato = input("Ingrese dato: \n")
            nod = Nodo(dato)
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