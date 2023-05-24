class Controlador:
    def __init__(self,modelo,vista):
        self.modelo = modelo
        self.vista = vista
    
    def registrar(self,sensor,bateria):
        return self.modelo.registrar(sensor,bateria)
    
    def actualizar_bateria(self,sensorid,bateriaid):
        return self.modelo.actualizar_bateria(sensorid,bateriaid)
    
    def mostrar(self,sensorid):
        return self.modelo.mostrar(sensorid)
