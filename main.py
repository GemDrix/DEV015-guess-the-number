import random

# Generar un número  entre 1 y 100
random_number = random.randint(1, 100)
print("¡He pensado en un número entre 1 y 100!")
print(random_number) #para saber que numero se generó y poder testear

# Variables para el juego
jugadora_adivinando = True
turno_jugadora = True

while jugadora_adivinando:
    if turno_jugadora:
        
        intento_jugadora = int(input("Adivina el número: "))
            
        if intento_jugadora < 1 or intento_jugadora > 100:
            print("Por favor, ingresa un número entre 1 y 100.")
               
        if intento_jugadora == random_number:
            print("¡Felicidades! Has adivinado el número.")
            break  
        elif intento_jugadora < random_number:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")
        
    
    else:
        # Turno del ordenador
        if intento_jugadora < random_number:
            intento_computador = random.randint(intento_jugadora + 1, 100)
            
        else:
            intento_computador = random.randint(1, intento_jugadora - 1)
        
        print(f"El ordenador adivina: {intento_computador}")
        
        if intento_computador == random_number:
            print("¡El ordenador ha adivinado el número!")
            break  # Terminar el juego
        elif intento_computador < random_number:
            print("El número secreto es mayor que la adivinanza del ordenador.")
        else:
            print("El número secreto es menor que la adivinanza del ordenador.")

    # Alternar turnos
    turno_jugadora = not turno_jugadora #cambia turno con la computadora 

print("¡Fin del juego!")


