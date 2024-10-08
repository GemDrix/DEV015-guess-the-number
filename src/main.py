"""Este módulo contiene funciones para realizar el juego 
"""
import random
import time
from jugador import Jugador
from funciones_utiles import resultado_comparacion

def turno(jugador, numero_azar, contador_turnos, min_num, max_num):
    """Realiza un turno de juego para un jugador.

    Esta función permite a un jugador elegir un número dentro de un rango 
    y registra su elección. Luego, compara la elección del jugador con el 
    número objetivo (número aleatorio) y devuelve el resultado de la comparación.
    """
    adivinanza = jugador.elegir_numero(min_num, max_num)
    jugador.registrar_eleccion(contador_turnos, adivinanza)
    resultado = resultado_comparacion(adivinanza, numero_azar)
    return resultado

def jugar():
    """Inicia el juego de adivinanza.

    Esta función genera un número aleatorio entre 1 y 100, da la bienvenida al 
    jugador y muestra el número que se debe adivinar. Luego, gestiona el flujo 
    del juego, permitiendo a los jugadores hacer sus elecciones hasta que uno de 
    ellos adivine el número correcto.
    """
    numero_azar = random.randint(1, 100)
    print("¡Bienvenido al juego de adivinanza!")
    print(numero_azar)

    jugador_humano = Jugador("Jugador")
    jugador_computadora = Jugador("Computadora")
    contador_turnos = 0
    min_num, max_num = 1, 100

    while True:
        contador_turnos += 1

        resultado_humano = turno(jugador_humano, numero_azar, contador_turnos, min_num, max_num)
        if resultado_humano == "ganador":
            print("Felicidades, ganaste!")
            break
        elif resultado_humano == "mayor":
            max_num = jugador_humano.historial[-1]["elegido"]
            print("El número que elegiste es mayor.")
        else:
            min_num = jugador_humano.historial[-1]["elegido"]
            print("El número que elegiste es menor.")

        time.sleep(1)

        resultado_compu = turno(jugador_computadora, numero_azar, contador_turnos, min_num, max_num)

        if resultado_compu == "ganador":
            print("La computadora ha ganado!")
            break
        elif resultado_compu == "mayor":
            max_num = jugador_computadora.historial[-1]["elegido"]
            print("El número elegido por la computadora es mayor.")
        else:
            min_num = jugador_computadora.historial[-1]["elegido"]
            print("El número elegido por la computadora es menor.")

    print(f"Juego finalizado en {contador_turnos} rondas.")
    print("Historial de elecciones:")
    print("Jugador:", jugador_humano.historial)
    print("Computadora:", jugador_computadora.historial)

if __name__ == "__main__":
    jugar()
