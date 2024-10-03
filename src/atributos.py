import random

NUMERO_A_DIVINAR: int = random.randint(1, 100) #se usan variables en mayusculas para que sean globales

def resultado_comparacion(consulta, numero):
    # Validamos que sean enteros
    if not isinstance(consulta, int) or not isinstance(numero, int):
        return "error"
    
    if consulta > numero:
        return "mayor"
    elif consulta < numero:
        return "menor"
    else:
        return "ganador"

def validacion_jugador(tipo_jugador, numero, min_n, max_n):
    if tipo_jugador == "Jugador":
        turno = int(input("Te toca jugar, por favor ingresa un número:\n"))
        jugador = "Jugador"
        
    elif tipo_jugador == "computadora":
        print("\nComputadora jugando " + "-"*10)
        turno = random.randint(min_n, max_n)
        print({turno})
        jugador = tipo_jugador.title()
        print(f"Computadora ha elegido el número:{turno}")

    comparacion = resultado_comparacion(turno, numero)

    if comparacion == "ganador":
        print("Felicidades, acertaste al número correcto.")
    else:
        if comparacion == "menor":
            if tipo_jugador == "computadora":
                min_n = turno
            print(f"{jugador}, el número que elegiste es menor.")
        else:
            if tipo_jugador == "computadora":
                max_n = turno
            print(f"{jugador}, el número que elegiste es mayor.")
    
    return comparacion, min_n, max_n, turno
