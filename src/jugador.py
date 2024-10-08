"""Este módulo contiene las funciones y clases básicas para el juego.
"""
import random


class Jugador:
    """Clase que representa a un jugador en el juego.

    Esta clase almacena el nombre del jugador y un historial de sus elecciones durante el juego.

    Atributos:
        nombre (str): El nombre del jugador.
        historial (list): Una lista que contiene el historial 
        de elecciones, cada entrada es un diccionario que registra el turno y el número elegido.

    Métodos:
        __init__(nombre): Inicializa una nueva instancia de la 
        clase Jugador con el nombre proporcionado.
        registrar_eleccion(turno, eleccion): Registra la elección del jugador en su historial.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def elegir_numero(self, min_n, max_n):
        """Permite al jugador (humano o computadora) elegir un número dentro de un rango dado.

    Esta función genera un número aleatorio si el jugador es la computadora, 
    o solicita al jugador humano que ingrese un número. 
    """
        if self.nombre == "Computadora":
            numero = random.randint(min_n, max_n)
            print(f"{self.nombre} ha elegido el número {numero}")
            return numero
        else:
            while True:
                try:
                    numero = int(
                        input(f"{self.nombre}, ingresa un número entre {min_n} y {max_n}: "))
                    if min_n <= numero <= max_n:
                        return numero
                    else:
                        print(f"Por favor, ingresa un número válido entre {
                              min_n} y {max_n}.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingresa un número entero.")

    def registrar_eleccion(self, turno, eleccion):
        """Registra la elección de un jugador en su historial.

    Esta función añade un registro a la lista de historial del jugador, 
    incluyendo el turno actual y la elección hecha.
    """
        self.historial.append({"turno": turno, "elegido": eleccion})
