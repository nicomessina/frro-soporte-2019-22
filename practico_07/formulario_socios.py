import tkinter as tk
from tkinter import ttk
from tkinter import *
from  practico_06.capa_negocio import NegocioSocio

class Application(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)
        # self.ventana = ventana
        ventana.title("Ciudades Argentinas")
        self.ns = NegocioSocio()
        self.cargar_socios()

        self.DATA = [('ROSARIO', '2000'),
        ('CORDOBA', '5000'),
        ('BUENOS AIRES', '1675'),
        ('SALTA', '4400'),
        ('PARANA', '3100'),
        ]


        self.header = ('Ciudad', 'Codigo Postal')
        self.label1 =Label(ventana,  text ="Ciudad")
        self.valor_1_txt =Entry(ventana, width=20)
        self.label1.grid(row = 1, column = 0)
        self.valor_1_txt.grid(row = 1, column = 1)
        self.label2 =Label(ventana, text ="Codigo Postal")
        self.valor_2_txt =Entry(ventana,width=6)
        self.label2.grid(row = 2, column = 0)
        self.valor_2_txt.grid(row = 2, column = 1)

        self.boton_agregar = Button(text = "Insertar Ciudad", command = Ventana_modificacion(ventana))
        self.boton_agregar.grid(row = 3, column = 1)
        self.boton_borrar = Button(text = "Borrar Ciudad", command = self.borrar_ciudad)
        self.boton_borrar.grid(row = 3, column = 3)

        self.tree = ttk.Treeview(columns=self.header,
                            show="headings",
                            height=5)
        self.tree.grid(row=4, columnspan=4,sticky='nsew' )
        for col, text in enumerate(self.header):
            self.tree.heading(col, text=text)
        self.tree.bind('<<TreeviewSelect>>', self.fila_seleccionada)


    def fila_seleccionada(self,event):
        self.valor_1_txt.delete(0,END)
        self.valor_2_txt.delete(0,END)
        global row_selected
        self.fila = event.widget.focus()
        self.values = event.widget.item(self.fila)['values']
        self.valor_1_txt.insert(0,self.values[0])
        self.valor_2_txt.insert(0,self.values[1])

    def agregar_ciudad(self):
        """
        Insertion method.
        """
        self.tree.insert('', 'end',values=(self.valor_1_txt.get(), self.valor_2_txt.get()))
        # Increment counter
        self.valor_1_txt.delete(0,END)            
        self.valor_2_txt.delete(0,END)
        
    def borrar_ciudad(self):
        self.tree.delete(self.fila)
        self.valor_1_txt.delete(0,END)            
        self.valor_2_txt.delete(0,END)

    def cargar_socios(self):
        for record in self.ns.todos():
            self.tree.insert('', 'end', values=record)

    # def ventana_modificacion(self):
    #     self.modificacion_vent = Toplevel()
    #     self.modificacion_vent.title = 'Modificación de Socio'

    #     Label(self.modificacion_vent, text = 'Nuevo Dni:').grid(row = 1, column = 1)
    #     nuevo_dni = Entry(self.modificacion_vent)
    #     nuevo_dni.grid(row = 1, column = 2)

    #     Label(self.modificacion_vent, text = 'Nuevo Nombre:').grid(row = 2, column = 1)
    #     nuevo_nombre= Entry(self.modificacion_vent)
    #     nuevo_nombre.grid(row = 2, column = 2)

    #     Label(self.modificacion_vent, text = 'Nuevo Apellido:').grid(row = 3, column = 1)
    #     nuevo_apellido= Entry(self.modificacion_vent)
    #     nuevo_apellido.grid(row = 3, column = 2)

    #     Button(self.modificacion_vent, text = 'Actualizar', command = lambda: self.realizar_modificacion(id, nuevo_dni.get(), nuevo_nombre.get(), nuevo_apellido.get())).grid(row = 4, column = 2, sticky = W)


class Ventana_modificacion(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.modificacion_vent = Toplevel()
        self.modificacion_vent.title = 'Modificación de Socio'
        Label(self.modificacion_vent, text = 'Nuevo Dni:').grid(row = 1, column = 1)
        nuevo_dni = Entry(self.modificacion_vent)
        nuevo_dni.grid(row = 1, column = 2)
        Label(self.modificacion_vent, text = 'Nuevo Nombre:').grid(row = 2, column = 1)
        nuevo_nombre= Entry(self.modificacion_vent)
        nuevo_nombre.grid(row = 2, column = 2)
        Label(self.modificacion_vent, text = 'Nuevo Apellido:').grid(row = 3, column = 1)
        nuevo_apellido= Entry(self.modificacion_vent)
        nuevo_apellido.grid(row = 3, column = 2)
        Button(self.modificacion_vent, text = 'Actualizar', command = lambda: self.realizar_modificacion(id, nuevo_dni.get(), nuevo_nombre.get(), nuevo_apellido.get())).grid(row = 4, column = 2, sticky = W)


if __name__ == '__main__':
    ventana = tk.Tk()
    app = Application(ventana)
    app.mainloop()

