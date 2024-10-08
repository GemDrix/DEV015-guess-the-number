"""Este módulo contiene clases y funciones para poder testear el codigo
"""
import unittest
from unittest.mock import patch
from jugador import Jugador

class TestJugador(unittest.TestCase):
    """Clase que contiene pruebas unitarias para la clase jugador
    """
    @patch('builtins.input', side_effect=['50'])  # Simula la entrada del usuario
    def test_elegir_numero_humano_valido(self, mock_input):
        """test_elegir_numero_humano_valido: Verifica que un jugador humano elija un número válido.
        """
        jugador = Jugador("Jugador")
        numero = jugador.elegir_numero(1, 100)
        self.assertEqual(numero, 50)  # Verifica que el número elegido sea 50
        mock_input.assert_called_once()

    @patch('builtins.input', side_effect=['150', 'not a number', '50'])  # Simula inputs inválidos
    def test_elegir_numero_humano_invalido(self, mock_input):
        """ test_elegir_numero_humano_invalido: Verifica que el manejo de entradas inválidas 
        funcione correctamente, asegurando que finalmente se elija un número válido.
        """
        jugador = Jugador("Jugador")
        numero = jugador.elegir_numero(1, 100)  # Ahora debe recibir un número válido
        self.assertEqual(numero, 50)  # Verifica que finalmente el número elegido sea 50
        mock_input.assert_called()

if __name__ == '__main__':
    unittest.main()
