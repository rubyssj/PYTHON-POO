# Encapsulamiento
class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre    
        self.__precio = precio     
        self.__cantidad = cantidad  

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}, Precio: {self.__precio:.3f}, Stock: {self.__cantidad}")

    def disminuir_stock(self, cantidad):
        if cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
            print(f"Se compraron {cantidad} {self.__nombre}. Quedan {self.__cantidad}" "unidades de stock ")
        else:
            print(f"No hay suficiente stock de {self.__nombre}.")

    def get_precio(self):
        return self.__precio

    def get_nombre(self):
        return self.__nombre

# Herencia
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, tamaño):
        super().__init__(nombre, precio, cantidad)
        self.tamaño = tamaño

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.tamaño}")

class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, tamaño):
        super().__init__(nombre, precio, cantidad)
        self.tamaño = tamaño

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.tamaño}")

# Abstracción
class Inventario:
    def __init__(self):
        self.prendas = []  #guarda las prendas de la tienda

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        print("Inventario:")
        for prenda in self.prendas:
            prenda.mostrar_info()
            print("-" * 30)

    def buscar_prenda(self, nombre_prenda):
        for prenda in self.prendas:
            if prenda.get_nombre().lower() == nombre_prenda.lower():
                return prenda
        return None

# Polimorfismo 
class Tienda:
    def __init__(self, inventario):
        self.inventario = inventario

    def procesar_compra(self):
        self.inventario.mostrar_inventario()
        nombre_prenda = input("¿Qué prenda desea comprar?: ")
        prenda = self.inventario.buscar_prenda(nombre_prenda)
        
        if prenda:
            cantidad = int(input(f"¿Cuántas {nombre_prenda} desea comprar?: "))
            prenda.disminuir_stock(cantidad)
        else:
            print("Prenda no encontrada en el inventario.")

#indumentaria amistyles
print( " bienvenidos" )
print("---------------------------")
camisa = RopaHombre("Remera hombre", 250.000, 50, "M")
pantalon = RopaHombre("Pantalón de Hombre todo por 20", 20.000, 30, "L")
falda = RopaMujer("Falda d/ Mujer", 100.000, 15, "S")
blusa = RopaMujer("Blusa d/ Mujer", 100.000, 40, "M")
chaqueta = RopaHombre("Chaqueta de cuero Hombre", 900.000, 20, "XL")
vestido = RopaMujer("Vestido Zara", 45.00, 10, "M")
champium_hombre = RopaHombre("calzado hombre converser one star", 350.000, 25, "42")
champium_mujer = RopaMujer("calzado mujer nike", 50.000, 20, "38")

inventario = Inventario()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(falda)
inventario.agregar_prenda(blusa)
inventario.agregar_prenda(chaqueta)
inventario.agregar_prenda(vestido)
inventario.agregar_prenda(champium_hombre)
inventario.agregar_prenda(champium_mujer)

tienda = Tienda(inventario)
tienda.procesar_compra()