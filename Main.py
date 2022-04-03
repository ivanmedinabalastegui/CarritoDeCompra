class color:
    NEGRITA = '\033[1m'
    SUBRAY = '\033[4m'
    FINAL = '\033[0m'

from datetime import datetime
now = datetime.now()

class Cliente:
    def __init__(self, idCliente, nombre, apellido, nif, cumple, fecRegistro, direccion):
        self.__idCliente = idCliente
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nif = nif
        self.__cumple = cumple
        self.__fecRegistro = fecRegistro
        self.__direccion = direccion


    def __str__(self):
        return "\n\t\tID: " + self.__idCliente + \
               "\n\t\tNombre: " + self.__nombre + \
               "\n\t\tApellido: " + self.__apellido + \
               "\n\t\tNIF: " + self.__nif + \
               "\n\t\tCumpleaños: " + self.__cumple + \
               "\n\t\tFecha de Registro: " + self.__fecRegistro + \
               "\n\t\tDireccion: " + self.__direccion


class Producto:

    def __init__(self, id_prod, cod_barra, nom_prod, fecha, precio, peso):
        self.__id_prod = id_prod
        self.__cod_barra = cod_barra
        self.__nom_prod = nom_prod
        self.__fecha = fecha
        self.__precio = precio
        self.__peso = peso

    def __str__(self):
        return "\n\t\tID: " + self.__id_prod +  \
               "\n\t\tCodigo de barras: " + self.__cod_barra + \
               "\n\t\tNombre del producto: " + self.__nom_prod + \
               "\n\t\tFecha: " + self.__fecha + \
               "\n\t\tPrecio: " + self.__precio + \
               "\n\t\tPeso: " + self.__peso + "\n"

    def lista(self):
        var = ""
        for p in lista:
            var = str(var) + str(p)
        return var

class CarritoCompra:

    def __init__(self, id, articulo, cliente, fecha):
        self.__id = id
        self.__articulo = articulo
        self.__cliente = cliente
        self.__fecha = fecha


    def __str__(self):
        return color.NEGRITA + "\t===================" + color.FINAL + "\n" +\
               "\n" + color.NEGRITA + "\t ID: " + color.FINAL + self.__id + \
               "\n" + color.NEGRITA + "\t Artículos: \n" + color.FINAL + self.__articulo + \
               "\n" + color.NEGRITA + "\t Cliente: " + color.FINAL + self.__cliente + \
               "\n" + color.NEGRITA + "\t Hora: " + color.FINAL + self.__fecha

class Direccion:
    def __init__(self, id_direc, calle, cod_postal, local, pais):
        self.__id_direc = id_direc
        self.__calle = calle
        self.__cod_postal = cod_postal
        self.__local = local
        self.__pais = pais

    def __str__(self):
        return "ID: " + self.__id_direc + " Calle: " + self.__calle + " Código Postal: " + self.__cod_postal + " Localidad: " + self.__local + " Pais: " + self.__pais



dir = Direccion( "001" , "Pino Montano", "41015", "Sevilla", "España")

cli = Cliente("001" , "Pepe" , "Carro", "835493759P", "11/12", "2021-03-04", str(dir))

p1 = Producto("001", "8632734948495", "Chopped", now.strftime('%d-%m-%Y'), "1.50€", "250g")
p2 = Producto("002", "8574643893738", "Plátanos", now.strftime('%d-%m-%Y'), "3.25€", "500g")
p3 = Producto("003", "7483376364796", "Galletas Oreo", now.strftime('%d-%m-%Y'), "2.10€", "300g")

lista = [p1, p2, p3]

carrito = CarritoCompra("001", str(Producto.lista(lista)), str(cli), now.strftime('%d-%m-%Y'))


print()
print(str(dir))
print(str(cli))
print(str(p1))
print(str(p2))
print(str(p3))

print()
print()
print()
print(color.NEGRITA + "\t\tCARRITO" + color.FINAL)
print(str(carrito))