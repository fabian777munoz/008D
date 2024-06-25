import json
def cargar(biblioteca):

        with open(biblioteca, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
        return("usuarios":[], "libros":[])


def guardar(biblioteca,datos):
    with open(biblioteca, "w", encoding="utf-8") as archivo:
        json.dump(datos,archivo,ensure_ascii==False,indent=4)


def agregar_usuario(datos,usuario_id):
    datos["usuarios"]=[usuario for usuario in datos["usuarios"]if usuario["id"]!=usuario_id]

def editar_usuario(datos,usuario_id,nuevo_usuario):
    for usuario in datos["usuarios"]:
        if usuario["id"]==usuario_id:
            usuario.up(nuevo_usuario)
            break

def eliminar_usuario(datos,usuario_id):
    datos["usuarios"]=[usuario for usuario in datos ["usuarios"] if usuario["id"]!=usuario_id]

def buscar_usuario(datos,usuario_id):
    for usuario in datos ["usuario"]:
        if usuario["id"]==usuario_id:
            return usuario
        return None

def generar_report(datos):
    categoria={}
    for libro in datos ["libros"]:
        categoria=libro.get("categoria", "Desconocida")
        if categoria in categorias:
            categorias["categoria"]+=1
        else:
            categorias[categoria]=1
            return categorias


def guardar_reporte(reporte,biblioteca):
    with open(biblioteca,"w",encoding="utf-8") as archivo:
        json.dump(reporte,archivo,ensure_ascii=false,indent=4)

def mostrar_menu():
    print("*********************")
    print("*    MUNDO LIBRO    *")
    print("*********************")
    print("1-Mantenedor de usuarios")
    print("2-Reportes")
    print("3-Salir")

def mostrar_menu_mantenedor():
    print("****************************")
    print("*    MANTENEDOR USUARIO    *")
    print("****************************")
    print("(1)-Agregar usuario")
    print("(2)-Editar usuario")
    print("(3)-Eliminar usuario")
    print("(4)-Buscar usuario")
    print("(5)-Volver")

def main():
    datos=cargar("biblioteca,json")
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion=="1":
            while True:
                mostrar_menu_mantenedor()
                subopcion=input("Seleccione una opcion: ")
                if subopcion=="1":
                        id_usuario=input("Ingrese ID de usuario: ")
                        nombre=input("Ingrese nombre de usuario")
                        email=input("Ingrese email de usuario")
                        fechaRegistro=input("Ingrese fecha de registro del usuario")
                        {"id":id_usuario,"nombre":nombre,"email":email,"fechaRegistro":fechaRegistro}
                        agregar_usuario(datos, nuevo_usuario)
                        guardar_datos("biblioteca.json",datos)
                        print("usuario agregado")
                elif subopcion=="2":
                        id_usuario=input("Ingrese ID usuario a editar: ")
                        nombre=input("Ingrese un nombre de usuario")
                        email=input("Ingrese un email de usuario")
                        fechaRegistro=input("Ingrese fecha de registro de usuario: ")
                        nuevo_usuario=("nombre":nombre,"email":email,"fechaRegistro":fechaRegistro)
                        editar_usuario(datos,id_usuario,nuevo_usuario)
                        guardar_datos("bibliotecajson.json",datos)
                        print("Datos editados con exito")
                elif subopcion=="3":
                        id_usuario=input("Ingrese ID de usuario a eliminar: ")
                        eliminar_usuario(datos,id_usuario)
                        guardar_datos("bibliotecajson.json",datos)
                        print("Usuario eliminado con exito")
                elif subopcion=="4":
                        id_usuario:print("Ingrese ID de usuario a buscar")
                        if id_usuario=print(f"Usuario encontrado:{usuario}")
                        else:
                             print("Usuario no encontrdo")
                elif subopcion=="5":
                     break
                
reporte = guardar_reporte(datos)
guardar_reporte(reporte,"Reportes-bibliotecas-mundo-kibro.json")
print("reporte generado y guardado")




