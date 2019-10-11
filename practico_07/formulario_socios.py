import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror,askokcancel,askyesno
from  practico_06.capa_negocio import NegocioSocio
from practico_05.ejercicio_01 import Socio

class Application(ttk.Frame):
    ns = NegocioSocio()

    def __init__(self, ventana):
        super().__init__(ventana)
        # self.ventana = ventana
        ventana.title("ABM Socios")
        self.crear_estructura(ventana)

        # self.ns = NegocioSocio()
        # self.marco = ttk.Frame(ventana,borderwidth =0,relief="raised",padding=(20,20),width=500,height=300)
        # self.marco.grid(column=0, row=1,sticky = tk.SW)
        # self.marco.columnconfigure(0,weight=1)
        # self.marco.rowconfigure(0,weight=1)
        # self.label1 =Label(ventana,  text ="Ciudad")
        # self.valor_1_txt =Entry(ventana, width=20)
        # self.label1.grid(row = 1, column = 0)
        # self.valor_1_txt.grid(row = 1, column = 1)
        # self.label2 =Label(ventana, text ="Codigo Postal")
        # self.valor_2_txt =Entry(ventana,width=6)
        # self.label2.grid(row = 2, column = 0)
        # self.valor_2_txt.grid(row = 2, column = 1)

        #self.boton_agregar = Button(text = "Insertar Ciudad", command = self.ventana_modificacion(ventana))
        #self.boton_agregar.grid(row = 3, column = 1)
        #self.boton_borrar = Button(text = "Borrar Ciudad", command = self.borrar_ciudad)
       # self.boton_borrar.grid(row = 3, column = 3)

        
        self.cargar_socios()

    # def fila_seleccionada(self,event):
    #     self.valor_1_txt.delete(0,END)
    #     self.valor_2_txt.delete(0,END)
    #     global row_selected
    #     self.fila = event.widget.focus()
    #     self.values = event.widget.item(self.fila)['values']
    #     self.valor_1_txt.insert(0,self.values[0])
    #     self.valor_2_txt.insert(0,self.values[1])


    def crear_estructura(self, ventana):

        self.header = ('Id', 'Dni','Nombre','Apellido')
        self.tree = ttk.Treeview(columns=self.header,
                            show="headings",
                            height=5)
        self.tree.grid(row=0, columnspan=4,sticky='nsew' )
        for col, text in enumerate(self.header):
            self.tree.heading(col, text=text)
        # self.tree.bind('<<TreeviewSelect>>', self.fila_seleccionada)
        self.btnAlta = ttk.Button(text="Alta",command=lambda: self.nueva_ventana(ventana,'Alta'))
        self.btnAlta.grid(column=0,row=1)
        #Baja no tiene ventana nueva
        self.btnBaja = ttk.Button(text="Baja",command=lambda: self.nueva_ventana(ventana,'Baja'))
        self.btnBaja.grid(column=1,row=1)
        self.btnModificar = ttk.Button(text="Modificar",command=lambda: self.modificar_socio(ventana))
        self.btnModificar.grid(column=2,row=1)

    def cargar_socios(self):
        for record in self.ns.todos():
            self.tree.insert('', 'end', values=record)


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

    
    def nueva_ventana(self,ventana, tipo):
        # self.modificacion_vent = Toplevel(ventana)
        # self.modificacion_vent.title = 'Modificación de Socio'
        titulo= tipo + ' de Socio'
        nueva_ventana = tk.Toplevel(ventana)
        nueva_ventana.geometry("300x150")
        nueva_ventana.title(titulo)
        nueva_ventana.focus_set()
        nueva_ventana.grab_set()

        nombre = StringVar()
        apellido = StringVar()
        dni = tk.IntVar()
        #id_socio = tk.IntVar() Es auto-increment
        #self.lbl_id_socio = Label(nueva_ventana, text='Id Socio:').grid(row=0, column=1)
        #self.txt_id_socio = Entry(nueva_ventana, textvariable=id_socio).grid(row=0, column=2)

        self.lbl_nombre= Label(nueva_ventana, text = 'Nombre:').grid(row = 1, column = 1)
        self.txt_nombre= Entry(nueva_ventana, textvariable=nombre).grid(row = 1, column = 2)
        self.lbl_apellido= Label(nueva_ventana, text = 'Apellido:').grid(row = 2, column = 1)
        self.txt_apellido= Entry(nueva_ventana, textvariable=apellido).grid(row = 2, column = 2)
        self.lbl_dni= Label(nueva_ventana, text = 'Dni:').grid(row = 3, column = 1)
        self.txt_dni = Entry(nueva_ventana, textvariable=dni).grid(row = 3, column = 2)

        if tipo =='Alta':
            text = 'Guardar'
        else:
            text = 'Aceptar'
            
        self.btn_aceptar_guardar = Button(nueva_ventana, text = text,command = lambda: self.aceptar_guardar(nueva_ventana, self.txt_dni.get(), self.txt_nombre.get(), self.txt_apellido.get(),tipo).grid(row = 5, column = 1, sticky = W))
        self.btn_cancelar = Button(nueva_ventana,text="Cancelar",command=nueva_ventana.destroy).grid(row = 5, column = 2, sticky = W)

    def aceptar_guardar(self,ventana,nombre,apellido,dni, tipo):
        if tipo=='Alta':
            self.alta_socio(ventana,nombre,apellido,dni)
        else:
            self.modificar_socio(ventana)

    def alta_socio(self, ventana, nombre, apellido, dni):

        if nombre == "" or apellido == "" or dni == 0:
            showerror("Error", "Se deben completar todos los campos")
        else:
            socio = Socio(nombre=nombre, apellido=apellido, dni=dni)
            alta = self.ns.alta(socio)

            if alta is True:
                self.cargar_tabla()
                self.cargar_datos()
                self.grid()
                ventana.destroy()
            else:
                showerror("Error", alta)

    def modificar_socio(self, ventana):
        id = self.tree.focus()
        print(id)
        # Item seleccionado en la ventana principal

        if id:
            self.nueva_ventana(ventana, 'Modificación')
            print(self.txt_apellido)
            selected_item = self.tree.selection()[0]
            # Lista con los datos del item seleccionado
            datos = self.tree.item(selected_item)
            id = datos['text']
            nombre = datos['values'][0]
            apellido = datos['values'][1]
            dni = datos['values'][2]
            self.txt_nombre.insert(1,nombre)

        else:
            showerror("Error","Debe seleccionar un socio")

# class Ventana_modificacion(ttk.Frame):
#     def __init__(self, ventana):
#         super().__init__(ventana)
#         self.modificacion_vent = Toplevel()
#         self.modificacion_vent.title = 'Modificación de Socio'
#         Label(self.modificacion_vent, text = 'Nuevo Dni:').grid(row = 1, column = 1)
#         nuevo_dni = Entry(self.modificacion_vent)
#         nuevo_dni.grid(row = 1, column = 2)
#         Label(self.modificacion_vent, text = 'Nuevo Nombre:').grid(row = 2, column = 1)
#         nuevo_nombre= Entry(self.modificacion_vent)
#         nuevo_nombre.grid(row = 2, column = 2)
#         Label(self.modificacion_vent, text = 'Nuevo Apellido:').grid(row = 3, column = 1)
#         nuevo_apellido= Entry(self.modificacion_vent)
#         nuevo_apellido.grid(row = 3, column = 2)
#         Button(self.modificacion_vent, text = 'Actualizar', command = lambda: self.realizar_modificacion(id, nuevo_dni.get(), nuevo_nombre.get(), nuevo_apellido.get())).grid(row = 4, column = 2, sticky = W)

def main():
    ventana = tk.Tk()
    app = Application(ventana)
    app.mainloop()
    return 0

if __name__ == '__main__':
    main()