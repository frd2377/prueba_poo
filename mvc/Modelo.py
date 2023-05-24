class Modelo:
    sensores = []
    baterias = []
    def registrar(self,sensor,bateria):
        if bateria >= 0:
            self.sensores.append(sensor)
            self.baterias.append(bateria)
            
    def actualizar_bateria(self,sensorid,bateriaid):
        for i in range(len(self.sensores)):
            if self.sensores[i] == sensorid:
                self.baterias[i] = bateriaid

    def mostrar(self,sensorid):
        for i in range(len(self.sensores)):
            if self.sensores[i] == sensorid:
                return self.baterias[i]
