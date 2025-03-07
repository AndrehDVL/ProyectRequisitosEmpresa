from proyect1 import BaseDatos
from proyect1 import add
from proyect2 import change
from proyect3 import delete
from proyect4 import showone
from proyect5 import showall

def menu():
    print("-----------------------------------------------------------------------------------")
    print("  Bienvenido al programa de Administración de los Usuarios de la Compañía ACME.")
    print("-----------------------------------------------------------------------------------")
    while True:
     print("Opciones: \n1.Registrar\n2.Cambiar\n3.Eliminar\n4.MostrarUno\n5.MostrarTodo\n6.Salir")
     question=int(input("Que Opcion deseas utilizar?: "))
     if question == 1:
        add()
     if question == 2:
        change()
     if question == 3:
        delete()
     if question == 4:
        showone()
     if question == 5:
        showall()
     if question == 6:
        print("----------------------------------------------------------------------------------")
        print("  Saliendo del programa de Administracion de los Usuarios de la Compañia ACME.")
        print("----------------------------------------------------------------------------------")
        break

menu()