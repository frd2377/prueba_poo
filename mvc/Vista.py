import tkinter as tk

class Vista:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.variable_sensorid = tk.StringVar(value='')
        self.variable_bateriaid = tk.DoubleVar(value=0)

        self.label_sensorid = tk.Label(self.root,text='ID Sensor: ').pack()
        self.entry_sensorid = tk.Entry(self.root,textvariable=self.variable_sensorid).pack()
        self.label_bateriaid = tk.Label(self.root,text='Nivel de Bateria: ').pack()
        self.entry_bateriaid = tk.Entry(self.root,textvariable=self.variable_bateriaid).pack()
        
        self.registrar_sensor = tk.Button(self.root,text='Registrar Sensor',command=self.registrar).pack()
        self.actualizar_bateria_boton = tk.Button(self.root,text='Actualizar Bateria',command=self.actualizar_bateria).pack()
        self.mostrar_bateria = tk.Button(self.root,text='Mostrar Estado',command=self.mostrar).pack()
        
        self.estado_bateria_sensor = tk.Label(self.root,text='Estado de la bateria del sensor ID: ').pack()
        self.textoid = tk.Label(self.root,text='id',textvariable=self.variable_sensorid).pack()
        self.bateria_sensorid = tk.Label(self.root,text='nivel bateria: ').pack()
        self.bateriaid = tk.Label(self.root,text=50,textvariable=self.variable_bateriaid).pack()
    def registrar(self):
        self.controlador.registrar(self.variable_sensorid.get(),self.variable_bateriaid.get())
        return 
    
    def actualizar_bateria(self):
        self.controlador.actualizar_bateria(self.variable_sensorid.get(),self.variable_bateriaid.get())

    def mostrar(self):
        return self.variable_bateriaid.set(self.controlador.mostrar(self.variable_sensorid.get()))
    
    def run(self):
        self.root.mainloop()
        return 
