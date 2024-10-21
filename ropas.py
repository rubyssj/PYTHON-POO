# Encapsulamiento
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre    
        self.__precio = precio     
        self.__cantidad = cantidad  

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}, Precio: Gs.{self.__precio:.3f}, Stock: {self.__cantidad}")

    def disminuir_stock(self, cantidad):
        if cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
            print(f"Se compraron {cantidad} {self.__nombre}. Quedan {self.__cantidad} unidades de stock.")
            return self.__precio * cantidad  # Retornar el total de la compra
        else:
            print(f"No hay suficiente stock de {self.__nombre}.")
            return 0

    def get_precio(self):
        return self.__precio

    def get_nombre(self):
        return self.__nombre

# Herencia
class RopaHombre(Producto):
    def __init__(self, nombre, precio, cantidad, tamaño):
        super().__init__(nombre, precio, cantidad)
        self.tamaño = tamaño

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.tamaño}")

class RopaMujer(Producto):
    def __init__(self, nombre, precio, cantidad, tamaño):
        super().__init__(nombre, precio, cantidad)
        self.tamaño = tamaño

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.tamaño}")

# Abstracción
class Inventario:
    def __init__(self):
        self.prendas = []  # Guarda las prendas de la tienda

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

# creamos la clase carrito
class Carrito:
    def __init__(self):
        self.productos_seleccionados = []

    def agregar_producto(self, prenda, cantidad):
        total_precio = prenda.disminuir_stock(cantidad)
        if total_precio > 0:  # Solo agregar si la compra fue exitosa
            self.productos_seleccionados.append((prenda.get_nombre(), cantidad, total_precio))

    def mostrar_resumen(self):
        print("Resumen de Compra:")
        total = 0
        for nombre, cantidad, precio in self.productos_seleccionados:
            print(f"{cantidad} x {nombre}: Gs.{precio:.3f}")
            total += precio #acumula
        print(f"Total a Pagar: Gs. {total:.3f}")

# Polimorfismo 
class Tienda:
    def __init__(self, inventario):
        self.inventario = inventario
        self.carrito = Carrito()  #carrito de compras

    def procesar_compra(self):
        self.inventario.mostrar_inventario()
        while True:
            nombre_prenda = input("¿Qué prenda desea comprar? (o escriba 'salir' para terminar de comprar el producto): ")
            if nombre_prenda.lower() == 'salir': #palabra clave
                break
            prenda = self.inventario.buscar_prenda(nombre_prenda)
            
            if prenda:
                cantidad = int(input(f"¿Cuántas {nombre_prenda} desea comprar?: "))
                self.carrito.agregar_producto(prenda, cantidad)
            else:
                print("Prenda no encontrada en el inventario.")
        self.carrito.mostrar_resumen()  # Muestra el resumen al finalizar la compra
        
print("Bienvenidos")
print("---------------------------")
camisa = RopaHombre("Remera hombre", 250.000, 50, "M")
pantalon = RopaHombre("Pantalón de Hombre todo por 20", 20.000, 30, "L")
falda = RopaMujer("Falda d/ Mujer", 100.000, 15, "S")
blusa = RopaMujer("Blusa d/ Mujer", 100.000, 40, "M")
chaqueta = RopaHombre("Chaqueta de cuero Hombre", 900.000, 20, "XL")
vestido = RopaMujer("Vestido Zara", 45.00, 10, "M")
calzado_hombre = RopaHombre("Calzado hombre Converser One Star", 350.000, 25, "42")
calzado_mujer = RopaMujer("Calzado mujer Nike", 50.000, 20, "38")
botin_hombre = RopaHombre("Botin de futbol adidas x messi" , 300.000, 10, "40")

#en este apartado podas agregar o sacar las ropas o accesorios que desees vender o tener
inventario = Inventario()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(falda)
inventario.agregar_prenda(blusa)
inventario.agregar_prenda(chaqueta)
inventario.agregar_prenda(vestido)
inventario.agregar_prenda(calzado_hombre)
inventario.agregar_prenda(calzado_mujer)
inventario.agregar_prenda(botin_hombre)

tienda = Tienda(inventario)
tienda.procesar_compra()
