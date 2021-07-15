import serial
import tkinter as tk
from tkinter.constants import X

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

ventana = tk.Tk()
ventana.title("Enviar")
ventana = tk.Canvas(ventana, width = 200, height = 140, bg = "#0248ba")

ventana.pack()

entry = tk.Entry (ventana) 
ventana.create_window(100, 50, window=entry) 

def enviar ():

    x1 = entry.get()
    arduino.write(x1.encode('utf-8')) #Escritura de datos
         
boton = tk.Button(text='Enviar por Serial', command=enviar)
ventana.create_window(100, 100, window=boton)

ventana.mainloop()