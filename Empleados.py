class Empleado:
    def __init__(self, nombre, sueldo, antiguedad, departamento, diasdescanzo):
        self.nombre = nombre
        self.sueldo = sueldo
        self.antiguedad =antiguedad
        self.departamento = departamento
        self.diasdescanzo = diasdescanzo

    def imprimir_datos(self):
        print(                       )
        print(f"Nombre: {self.nombre}")
        print(f"Sueldo: {self.sueldo}")
        print(f"Antigüedad: {self.antiguedad} años")
        print(f"Departaamento: {self.departamento}")
        print(f"Dias de descazo usados: {self.diasdescanzo}")
        print(                                         )
        
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")
    
    def ingresar_departamento(self):
        print("Departamento: ", self.departamento)
        print("Antiguedad: ", self.antiguedad)

    def sueldo_mensual(self):
        sueldomensual = self.sueldo * 3
        print("Sueldo mensual: ", sueldomensual)

    def vacaciones(self):
        diasvacaciones = 25

        if self.diasdescanzo>25:
            print("Debes dias de trabajo")
        else:
            print("Te quedan estos dias de vacaciones: ", diasvacaciones - self.diasdescanzo)

Lista_empleados = [
    Empleado("Oliver", 2000, 5, "Ventas", 0),
    Empleado("Sandra", 3500, 3, "Ventas", 5),
    Empleado("Roberto", 4000, 10, "Contador", 3)
]

while True:
   print("Bienvenido al Menú")
   print("1. Agregar Empleado")
   print("2.- Modificar empleado")
   print("3.- Eliminar empleado")
   print("4.- Ver empleados")
   print("5.- Salir")
   opcion = int(input("¿Qué opción desea elegir? "))
   
   if opcion==1:
       print("Agregar empleado")

       nombre = input("Dame el nombre del empleado: ")
       sueldo = int(input("Dame el suelo del empleado:"))
       antiguedad = int(input("Dame el dia que entro: "))
       departamento = input("Dame el departamento al que pertenece: ")
       diasdescanzo = int(input("Dame los dias que a descanzado: "))

       nuevo_empleado = Empleado(nombre, sueldo, antiguedad, departamento, diasdescanzo)
       Lista_empleados.append(nuevo_empleado)
       print("empleado agregado")
       print("Aqui esta su registro: ")
       nuevo_empleado.imprimir_datos()
    
   elif opcion == 2:
        print("Modificar empleado")
        
        nombre_modificar = input("Dame el nombre del empleado que modificar: ")
        encontrado = False

        for empleado in Lista_empleados:
            if empleado.nombre == nombre_modificar:
                encontrado = True
                print("Empleado encontrado. Ingresa los nuevos datos.")

                nuevo_sueldo = int(input(f"Dame el sueldo para {empleado.nombre}: "))
                nueva_antiguedad = int(input("Dame el día en que entró: "))
                nuevo_departamento = input("Dame el departamento al que pertenece: ")
                nuevos_dias_descanso = int(input("Dame los días que ha descansado: "))
                
                empleado.sueldo = nuevo_sueldo
                empleado.antiguedad = nueva_antiguedad
                empleado.departamento = nuevo_departamento
                empleado.diasdescanso = nuevos_dias_descanso
                
                print("Empleado modificado")
                break  
        
        if not encontrado:
            print("Empleado no encontrado. Por favor, verifica el nombre.")

   elif opcion == 3:
        print("Eliminar empleado")
        nombre_eliminar = input("Dame el nombre del empleado que deseas eliminar: ")
        encontrado = False
        
        for empleado in Lista_empleados:
            if empleado.nombre == nombre_eliminar:
                Lista_empleados.remove(empleado)
                encontrado = True
                print("Empleado eliminado exitosamente.")
                break  
        
        if not encontrado:
            print("Empleado no encontrado. Por favor, verifica el nombre.")

   elif opcion == 4:
        print("Ver empleados")
        if not Lista_empleados:
            print("No hay empleados registrados.")
        else:
            for empleado in Lista_empleados:
                empleado.imprimir_datos()

   elif opcion== 5:
       print("Salir") 
       
   break