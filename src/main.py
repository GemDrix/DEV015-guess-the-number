import random
import time


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def elegir_numero(self, min_n, max_n):
        if self.nombre == "Computadora":
            return random.randint(min_n, max_n)
    
        else:
            return int(input(f"{self.nombre}, ingresa un número entre {min_n} y {max_n}: "))

    def registrar_eleccion(self, turno, eleccion):
        self.historial.append({"turno": turno, "elegido": eleccion})


def comparar_numeros(adivinanza, objetivo):
    if adivinanza > objetivo:
        return "mayor"
    elif adivinanza < objetivo:
        return "menor"
    else:
        return "ganador"


def jugar():
    numero_azar = random.randint(1, 100)
    print("¡Bienvenido al juego de adivinanza!")
    print("La computadora ha seleccionado un número entre 1 y 100.")
    print(numero_azar)

    jugador_humano = Jugador("Jugador")
    jugador_computadora = Jugador("Computadora")
    contador_turnos = 0
    min_num, max_num = 1, 100

    while True:
        contador_turnos += 1

        # Turno del jugador humano
        adivinanza_humana = jugador_humano.elegir_numero(min_num, max_num)
        jugador_humano.registrar_eleccion(contador_turnos, adivinanza_humana)
        resultado_humano = comparar_numeros(adivinanza_humana, numero_azar)

        if resultado_humano == "ganador":
            print("Felicidades, ganaste!")
            break
        elif resultado_humano == "mayor":
            max_num = adivinanza_humana
            print("El número que elegiste es mayor.")
        else:
            min_num = adivinanza_humana
            print("El número que elegiste es menor.")

        time.sleep(1)

        # Turno de la computadora
        adivinanza_computadora = jugador_computadora.elegir_numero(
            min_num, max_num)
        jugador_computadora.registrar_eleccion(
            contador_turnos, adivinanza_computadora)
        resultado_computadora = comparar_numeros(
            adivinanza_computadora, numero_azar)

        if resultado_computadora == "ganador":
            print("La computadora ha ganado!")
            break
        elif resultado_computadora == "mayor":
            max_num = adivinanza_computadora
            print("El número elegido por la computadora es mayor.")
        else:
            min_num = adivinanza_computadora
            print("El número elegido por la computadora es menor.")

    print(f"Juego finalizado en {contador_turnos} rondas.")
    print("Historial de elecciones:")
    print("", jugador_humano.historial)
    print("Computadora:", jugador_computadora.historial)


if __name__ == "__main__":
    jugar()
