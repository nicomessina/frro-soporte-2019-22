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
        self.btnBaja = ttk.Button(text="Baja",command=lambda: self.fila_seleccionada(ventana,'Baja'))
        self.btnBaja.grid(column=1,row=1)
        self.btnModificar = ttk.Button(text="Modificar",command=lambda: self.fila_seleccionada(ventana,'Modificacion'))
        self.btnModificar.grid(column=2,row=1)

    def cargar_socios(self):
        self.tree.delete(*self.tree.get_children())
        for record in self.ns.todos():
            self.tree.insert('', 'end', values=record)


    def nueva_ventana(self,ventana, tipo, dni_anterior = False):
        titulo= tipo + ' de Socio'
        nueva_ventana = tk.Toplevel(ventana)
        nueva_ventana.geometry("300x150")
        nueva_ventana.title(titulo)
        nueva_ventana.focus_set()
        nueva_ventana.grab_set()

        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = tk.IntVar()
        
        self.lbl_nombre= Label(nueva_ventana, text = 'Nombre:').grid(row = 1, column = 1)
        self.txt_nombre= Entry(nueva_ventana, textvariable=self.nombre)
        self.lbl_apellido= Label(nueva_ventana, text = 'Apellido:').grid(row = 2, column = 1)
        self.txt_apellido= Entry(nueva_ventana, textvariable=self.apellido)
        self.lbl_dni= Label(nueva_ventana, text = 'Dni:').grid(row = 3, column = 1)
        self.txt_dni = Entry(nueva_ventana, textvariable=self.dni)
        
        self.txt_nombre.grid(row = 1, column = 2)
        self.txt_apellido.grid(row = 2, column = 2)
        self.txt_dni.grid(row = 3, column = 2)
        
        if tipo =='Alta':
            text = 'Guardar'
        else:
            text = 'Aceptar'

        self.btn_aceptar_guardar = Button(nueva_ventana, text = text,command = lambda: self.aceptar_guardar(nueva_ventana,tipo,dni_anterior)).grid(row = 4, column = 2, sticky = W)
        self.btn_cancelar = Button(nueva_ventana,text="Cancelar",command=nueva_ventana.destroy).grid(row = 5, column = 2, sticky = W)

    def aceptar_guardar(self, ventana,tipo, dni_anterior):
        dni = self.dni.get()
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        if tipo=='Alta':
            self.alta_socio(ventana, dni, nombre, apellido)
        else:

            print(dni_anterior)
            self.modificar_socio(ventana, dni, nombre, apellido,dni_anterior)

    def hay_campos_vacios(self, dni, nombre, apellido):
        if nombre == "" or apellido == "" or dni == 0:
            showerror("Error", "Hay campos sin completar")
            return True
        else:
            return False

    def alta_socio(self, ventana, dni, nombre, apellido):
        if not self.hay_campos_vacios(dni, nombre, apellido):
            socio = Socio(nombre=nombre, apellido=apellido, dni=dni)
            alta = self.ns.alta(socio)
            if alta:
                self.cargar_socios()
                ventana.destroy()
            else:
                showerror("Error", 'Hay ocurrido un error')

    def modificar_socio(self, ventana , dni, nombre, apellido,dni_anterior):
        if not self.hay_campos_vacios(dni, nombre, apellido):
            print(dni_anterior)
            socio_id = self.ns.buscar_dni(dni_anterior).id
            socio = Socio(id=socio_id, dni=dni, nombre=nombre, apellido=apellido)
            modificacion = self.ns.modificacion(socio)
            print(socio)
            print(modificacion)
            if modificacion:
                self.cargar_socios()
                ventana.destroy()
            else:
                showerror("Error", 'Hay ocurrido un error')

    def fila_seleccionada(self, ventana, tipo):
        seleccion = self.tree.focus()
        if seleccion:
            fila = self.tree.selection()[0]
            datos = self.tree.item(fila)
            id = datos['values'][0]
            if tipo=='Modificacion':
                dni_anterior = datos['values'][1]
                self.nueva_ventana(ventana, 'Modificación', dni_anterior)
                self.dni.set(datos['values'][1])
                self.apellido.set(datos['values'][2])
                self.nombre.set(datos['values'][3])

            # Lista con los datos del item seleccionado
            else:
                print('se eligio baja', id)
                res = self.ns.baja(id)
                print(res)
            self.cargar_socios()

        else:
            showerror("Error","Debe seleccionar un socio")

def main():
    ventana = tk.Tk()
    app = Application(ventana)
    app.mainloop()
    return 0

if __name__ == '__main__':
    main()
