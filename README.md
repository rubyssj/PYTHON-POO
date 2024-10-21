# Programa de sistema de compra de ropas (deposito)

## Descripción
El proposito de este programa es basicamente la implementacion de los 4 pilares de POO en python y utilizamos un sistema de compra de articulos de compras de ropas, calzados, etc. , permitiendo a los usuarios seleccionar productos y procesar compras utilizando Programación Orientada a Objetos (POO).

## Clases
- **Prenda**: Clase base que representa un producto general.
- **RopaHombre** y **RopaMujer**: Clases que heredan de Prenda y representan ropa específica para hombres y mujeres.
- **Inventario**: Clase que gestiona las prendas disponibles en la tienda.
- **Tienda**: Clase que maneja la interacción con el usuario y el proceso de compra.

## Características
- **Encapsulamiento**: Los atributos de las clases están encapsulados.
- **Herencia**: RopaHombre y RopaMujer heredan de Prenda.
- **Polimorfismo**: Método `mostrar_info` sobrescrito en las clases derivadas.
- **Abstracción**: Se ocultan detalles internos del proceso de compra.

## Cómo Ejecutar
1. Asegúrate de tener Python instalado en tu sistema.
2. Clona este repositorio o descarga el archivo `ropas.py`.
3. Ejecuta el siguiente comando en la terminal:
4.    python ropas.py
