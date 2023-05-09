import pymongo
from bson import ObjectId

class Agenda:
    def __init__(self,nombre_bd,nombre_coleccion):
        self.cliente = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.cliente[nombre_bd]
        self.coleccion = self.db[nombre_coleccion]
        self.contactos = []

    def insertar_contacto(self, nombre, apellido, telefono, email):
         if self.coleccion.find_one({"telefono": telefono}):
            print("Error: el número de teléfono ya existe en la base de datos")
            return
         
         nuevo_contacto = {
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
            "email": email
        }
         self.coleccion.insert_one(nuevo_contacto) #inserta el nuevo contacto
         print("Se ha insertado el contacto correctamente")


    def borrar_contacto(self, id):
        resultado = self.coleccion.delete_one({"_id": ObjectId(id)}) 
        if resultado.deleted_count == 1:
            print("Se ha eliminado el contacto con éxito.")
        else:
            print("No se ha encontrado el contacto con ese ID.")


    def actualizar_contacto(self, id, nombre=None, apellido=None, telefono=None, email=None):
        filtro = {"_id": ObjectId(id)}
        actualizacion = {}
        if nombre:
            actualizacion["nombre"] = nombre
        if apellido:
            actualizacion["apellido"] = apellido
        if telefono:
            actualizacion["telefono"] = telefono
        if email:
            actualizacion["email"] = email
        resultado = self.coleccion.update_one(filtro, {"$set": actualizacion})
        if resultado.matched_count == 1:
            print("Se ha actualizado el contacto con éxito.")
        else:
            print("No se ha encontrado el contacto con ese ID.")
