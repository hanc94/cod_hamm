import serial as s
import sys
import time
if sys.version_info[0] < 3:
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk
    from tkinter import *
    from tkinter import ttk,font

class InterfazHamm():
    def __init__(self):
       self.raiz = Tk()
       self.raiz.config(bg="light blue")
       self.raiz.resizable(0,0)
       self.raiz.geometry("550x450")
       #Variable
       self.Emisor = StringVar()
       self.Receptor = StringVar()
       self.cadena = StringVar()
       self.men=StringVar()
       self.ser = s.Serial('/dev/ttyACM1',9600)
       self.time=time.sleep(2)
       #Fuentes
       self.Arial50 = font.Font(family="Arial",size=50)
       self.Arial30 = font.Font(family="Arial",size=30)
       self.Arial15 = font.Font(family="Arial",size=15)
       #Widgets
       self.cuerpo = ttk.Frame(self.raiz,borderwidth=2,relief="ridge",)
       self.cuerpo_menu_principal = Frame(self.raiz,background="light blue")
       self.cuerpo_principal1 = ttk.Frame(self.raiz,borderwidth=3,relief="ridge")
       self.cuerpo_principal2 = ttk.Frame(self.raiz,borderwidth=3,relief="ridge")
       self.panel_principal1 = PanedWindow(self.cuerpo_principal1,width=690,height=500,background="light blue")
       self.panel_principal2 = PanedWindow(self.cuerpo_principal2,width=690,height=500,background="light blue")
       self.creditos = ttk.Label(self.raiz,font=self.Arial15,text="Creado por:\n Changua\n Campeche\n Borracho",foreground="orange red",background="light blue")
       self.ingreso_text = ttk.Label(self.panel_principal1,text="Mensaje: ",font=self.Arial15,foreground="orange red",background="light blue",borderwidth=43)
       self.texto = ttk.Entry(self.panel_principal1,textvariable=self.Emisor,foreground="orange red")
       self.enviar = ttk.Button(self.panel_principal1,text="Enviar",command=self.chat)
       self.limpiar = ttk.Button(self.raiz,text="limpiar chat",command=self.clean)
       self.panel_chat = Listbox(self.panel_principal2,height=14,width=38,font=self.Arial15,foreground="orange red",background="white")
       #poscionamiento de elementos
       self.cuerpo.grid(column=0,row=0)
       self.cuerpo_menu_principal.grid(column=1,row=0,sticky="n")
       self.cuerpo_principal1.grid(column=0,row=0,sticky="w")
       self.cuerpo_principal2.grid(column=0,row=1)
       self.panel_principal1.grid(column=0,row=0)
       self.panel_principal2.grid(column=0,row=0)
       self.creditos.grid(column=1,row=1,sticky="s,e")
       self.limpiar.grid(column=1,row=0,padx=10,pady=10)
       self.ingreso_text.grid(column=0,row=1,sticky="e")
       self.texto.grid(column=1,row=1,sticky="w,e")
       self.enviar.grid(column=2,row=1,sticky="e")
       self.panel_chat.grid(column=0,row=0,sticky="n,w")
       #inicio de interfaz
       self.aux=100
       self.raiz.mainloop()
    def chat(self):
        self.time
        self.panel_chat.insert(self.aux,self.Emisor.get())
        self.men=self.Emisor.get()
        self.aux=self.aux-1
        self.ser.write(str(self.men).encode('ascii'))
        #self.cadena=self.ser.readline() 
    def clean(self):
        self.panel_chat.delete(0,100)
        self.aux=100
if __name__== '__main__':
    mi_interfaz = InterfazHamm()
