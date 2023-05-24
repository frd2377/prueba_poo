from Modelo import Modelo 
from Vista import Vista
from Controlador import Controlador

modelo = Modelo()
vista = Vista()
controlador = Controlador(modelo,vista)
vista.controlador = controlador
vista.run()


