import tkinter as tk

class Vista:
    sensores = []
    baterias = []
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.variable_sensorid = tk.StringVar(value='')
        self.variable_bateriaid = tk.DoubleVar(value=0)
        self.mensaje = tk.StringVar(value='Estado de la bateria del sensor')
        self.label_sensorid = tk.Label(self.root,text='ID Sensor: ').pack()
        self.entry_sensorid = tk.Entry(self.root,textvariable=self.variable_sensorid).pack()
        self.label_bateriaid = tk.Label(self.root,text='Nivel de Bateria: ').pack()
        self.entry_bateriaid = tk.Entry(self.root,textvariable=self.variable_bateriaid).pack()
        
        self.registrar_sensor = tk.Button(self.root,text='Registrar Sensor',command=self.registrar).pack()
        self.actualizar_bateria = tk.Button(self.root,text='Actualizar Bateria',command=self.actualizar_bateria).pack()
        self.mostrar_bateria = tk.Button(self.root,text='Mostrar Estado',command=self.mostrar).pack()
        
        self.estado_bateria_sensor = tk.Label(self.root,textvariable=self.mensaje).pack()
        self.bateria_sensorid = tk.Label(self.root,textvariable=self.variable_bateriaid).pack()
    def registrar(self):
        if self.variable_bateriaid.get() >= 0:
            self.sensores.append(self.variable_sensorid.get())
            self.baterias.append(self.variable_bateriaid.get())
            print(self.sensores)
            print(self.baterias)
        return
    def actualizar_bateria(self):
        print(self.sensores)
        print(self.baterias)
        for i in range(len(self.sensores)):
            if self.sensores[i] == self.variable_sensorid.get():
                self.baterias[i] = self.variable_bateriaid.get()
                return
    def mostrar(self):
        print(self.sensores)
        print(self.baterias)
        for i in range(len(self.sensores)):
            if self.sensores[i] == self.variable_sensorid.get():
                return self.mensaje.set(f'Estado de la bateria del sensor {self.sensores[i]}')
    
    def run(self):
        self.root.mainloop()
        return 
