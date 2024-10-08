"""Este módulo contiene funciones para realizar operaciones matemáticas ilógicas.
"""
def resultado_comparacion(consulta, numero):
    """Compara un número consultado con un número objetivo.

    Esta función verifica si el número consultado es mayor, menor o igual al número objetivo.
    También valida que ambos números sean enteros.

    Args:
        consulta (int): El número que el usuario desea comparar.
        numero (int): El número objetivo con el que se realiza la comparación.

    Returns:
        str:
            - "mayor" si la consulta es mayor que el número.
            - "menor" si la consulta es menor que el número.
            - "ganador" si la consulta es igual al número.
            - "error" si alguno de los argumentos no es un entero.
    """
    if not isinstance(consulta, int) or not isinstance(numero, int):
        return "error"
    if consulta > numero:
        return "mayor"
    elif consulta < numero:
        return "menor"
    else:
        return "ganador"
