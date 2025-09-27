class Alumno:
    def __init__(self, nombre, apellidos, nota1, nota2, nota3, nota4, nota5):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 =nota5
    
    def promedio(self):
        return(self.nota1 + self.nota2 + self.nota3 + self.nota4 + self.nota5)/5
    
    def imprimir_datos(self):
        print(                       )
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Nota 3: {self.nota3}")
        print(f"Nota 4: {self.nota4}")
        print(f"Nota 5: {self.nota5}")
        print(                                         )    

Lista_alumnos = [
    Alumno("Carlos","Rodriguez", 40, 67, 90, 50, 70),
    Alumno("Ximena", "Palacios", 60, 50, 70, 82, 76),
    Alumno("Santiago", "Cerda", 78, 45, 80, 70, 60)
]

while True:

    print("Bienvenido")
    print("1. Calcular promedio")
    print("2. Mostrar todas las notas de los alumnos")
    print("3. Modificar alumno")
    print("4. Eliminar alumno")
    print("5. Salir")
    opcion = int(input("¿Que opcion desea elegir?"))
    
    if opcion == 1:
        ("Calcular promedio")
        nombre = input("Dame el nombre: ")
        apellidos = input("Dame los apellidos: ")
        nota1 = int(input("Dame la primera nota: "))
        nota2 = int(input("Dame la segunda nota: "))
        nota3 = int(input("Dame la tercera nota: "))
        nota4 = int(input("Dame la cuarta nota: "))
        nota5 = int(input("Dame la quinta nota: "))

        estudiante = Alumno(nombre, apellidos, nota1, nota2, nota3, nota4, nota5)
        print("El promedio es de: ", estudiante.promedio())  

    elif opcion == 2:
        print("Ver alumnos")
        if not Lista_alumnos:
            print("No hay alumnos registrados.")
        else:
            for alumno in Lista_alumnos:
                alumno.imprimir_datos()

    elif opcion == 3:
        print("Modificar alumno")
        
        nombre_modificar = input("Dame el nombre del alumno que modificar: ")
        encontrado = False

        for alumno in Lista_alumnos:
            if alumno.nombre == nombre_modificar:
                encontrado = True
                print("Alumno encontrado. Ingresa los nuevos datos.")
                
                nueva_nota1 = int(input("Dame la nueva nota 1: "))
                nueva_nota2 = int(input("Dame la nueva nota 2: "))
                nueva_nota3 = int(input("Dame la nueva nota 3: "))
                nueva_nota4 = int(input("Dame la nueva nota 4: "))
                nueva_nota5 = int(input("Dame la nueva nota 5: "))
                
                alumno.nota1 = nueva_nota1
                alumno.nota2 = nueva_nota2
                alumno.nota3 = nueva_nota3
                alumno.nota4 = nueva_nota4
                alumno.nota5 = nueva_nota5
                
                print("Alumno modificado")
                break  
        
        if not encontrado:
            print("Empleado no encontrado. Por favor, verifica el nombre.")

    elif opcion == 4:
        print("Eliminar alumno")
        nombre_eliminar = input("Dame el nombre del alumno que deseas eliminar: ")
        encontrado = False
        
        for alumno in Lista_alumnos:
            if alumno.nombre == nombre_eliminar:
                Lista_alumnos.remove(alumno)
                encontrado = True
                print("Alumno eliminado exitosamente.")
                break  
        
        if not encontrado:
            print("Alumno no encontrado. Por favor, verifica el nombre.")

    elif opcion == 5:
        print("Salir")

    break