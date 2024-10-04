"""Este módulo contiene funciones para realizar el juego 
"""
import random
import time
from jugador import Jugador
from funciones_utiles import resultado_comparacion

def turno(jugador, numero_azar, contador_turnos, min_num, max_num):
    adivinanza = jugador.elegir_numero(min_num, max_num)
    jugador.registrar_eleccion(contador_turnos, adivinanza)
    resultado = resultado_comparacion(adivinanza, numero_azar)
    return resultado

def jugar():
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

        resultado_computadora = turno(jugador_computadora, numero_azar, contador_turnos, min_num, max_num)
        if resultado_computadora == "ganador":
            print("La computadora ha ganado!")
            break
        elif resultado_computadora == "mayor":
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
