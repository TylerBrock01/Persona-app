
class Persona:
    
    def agregar_persona(self,id , nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_persona(self):
        return print("ID: ",self.id,"\n Nombre:",self.nombre," Edad: ", self.edad)
    
class Proceso:
    
    def __init__(self):
        self.personas = []
        self.id = 0
           
    def crear_persona(self, nombre ,edad ):
        nueva_persona = Persona()
        nueva_persona.agregar_persona(self.id, nombre,edad)
        self.personas.append(nueva_persona)
        self.id+=1
               
    def modificar_persona (self, id, nombre, edad):
        if id >= id <= len(self.personas):
            # Modificar directamente los atributos de la persona en el índice proporcionado
            self.personas[id].nombre = nombre
            self.personas[id].edad = edad
        else:
            print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nÍndice fuera de rango\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
            
    def eliminar_persona(self, id):
        if id >= id <= len(self.personas):           
            if id == id:
                del self.personas[id]
                
    def mostrar_persona(self):
        print("============================================\nLista de personas:")
        for persona in self.personas:
            persona.mostrar_persona()
        print("============================================\n\n")
class Ejecucion:
               
    def agregar(self, procesos):
        try:
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            procesos.crear_persona(nombre, edad)
            procesos.mostrar_persona()
        except ValueError:
            print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nIngrese los valores correctamente\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
            self.agregar(procesos)
            
    def modificar(self, procesos):
        try:
            print("Ingrese la informacion que se les solicita")
            id = int(input("ID: "))
            nombre = input("Ingrese nuevo nombre: ")
            edad = int(input("Ingrese nueva edad: "))
            procesos.modificar_persona(id, nombre, edad)
            
        except ValueError:
            print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nIngrese los valores correctamente\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")           
            self.modificar(procesos)
    
    def eliminar (self, procesos):
        try:
            id = int(input("Ingrese la ID para eliminar: "))
            procesos.eliminar_persona(id)
        except ValueError:
            print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nIngrese los valores correctamente\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
            self.eliminar(procesos)

class Bucle:

    def bucle_agregar(self):
        while True:
            if funciones.salir():
                break
            else:
                ejecuciones.agregar(procesos) # agregar
                if funciones.repetir_operacion():
                    break
                else:
                    continue
        self.bucle_home()
        
    def bucle_modificar(self):
        while True:
            if funciones.salir():
                break
            else:
                procesos.mostrar_persona()
                ejecuciones.modificar(procesos) #modificar
                procesos.mostrar_persona()
                if funciones.repetir_operacion():
                    break
                else:
                    continue
        self.bucle_home()
            
    def bucle_eliminar(self):
        while True:
            if funciones.salir():
                break
            else:
                procesos.mostrar_persona()
                ejecuciones.eliminar(procesos) #eliminar
                procesos.mostrar_persona()
                if funciones.repetir_operacion():
                    break
                else:
                    continue
        self.bucle_home()
            
    def bucle_home(self):
        funciones.opciones()
        
class Funcion:
    
    def opciones(self):
        try:
            print("##################\n#\tIngresa valores enteros\t#")
            self.opcion = int(input("#[1]== Agregar persona\n#[2]== Modificar persoba\n#[3]== Eliminar persona\n#[4] salir\n\n#  Ingrese una opcion: "))
        
            if self.opcion == 1:
                bucles.bucle_agregar()
            elif self.opcion == 2:
                 bucles.bucle_modificar()
            elif self.opcion == 3:
                 bucles.bucle_eliminar()
            else:
                print("\n\nRealmente pusiste ", self.opcion," de todas las opciones!?")
        except ValueError:
            print("\n\nIngresa valores enteros!!\n\n")
            bucles.bucle_home()
    
    def salir(self):
        self.abandonar = int(input("\nDesea cancelar la operacion\n[1]==No\n[0]== Si: "))
        if self.abandonar ==0:
              bucles.bucle_home()
        else:
            pass
        
    def parar_bucles(self):
        try:
            self.intrucciones = int(input("\nDesea continuar la operacion:\n [0]== No \n [1]== Continuar: "))
            return self.intrucciones == 0
        except vars.ValueError:
            print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nIngrese valores correctamente\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
            self.parar_bucles()
            
    def repetir_operacion(self):
        try:
            self.repetir = int(input("\nDesea repetir operacion?\n[0]== No\n[1]== Si: "))
            return self.repetir == 0
        except ValueError:
            print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nIngrese valores correctamente\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
            self.repetir_operacion()
#
funciones = Funcion()
bucles = Bucle()
ejecuciones = Ejecucion()
procesos = Proceso()

# Iniciar el bucle
bucles.bucle_home()