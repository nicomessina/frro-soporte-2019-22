# Implementar los casos de prueba descriptos.

import unittest
import names
from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado

class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):

        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        try:
            socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
            exito = self.ns.alta(socio)
        except:
            self.assertRaises(DniRepetido, self.ns.regla_1, exito)


    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        invalido = Socio(dni=12345678, nombre='Joaquín Ignacio', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Pe')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Gonzalez Gonzalez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2,invalido)


    def test_regla_3(self):
        for i in range(self.ns.MAX_SOCIOS):
            exito=self.ns.alta(self.ns.datos.generarSocio())
        socio = self.ns.datos.generarSocio()
        self.assertRaises(MaximoAlcanzado,self.ns.regla_3,socio)



    def test_baja(self):
        socio = self.ns.alta(self.ns.datos.generarSocio())
        self.assertTrue(self.ns.baja(socio.id))

    def test_buscar(self):
        socio = self.ns.alta(self.ns.datos.generarSocio())
        self.assertIsNotNone(self.ns.buscar(socio.id))

    def test_buscar_dni(self):
        socio = self.ns.alta(self.ns.datos.generarSocio())
        self.assertIsNotNone(self.ns.buscar_dni(socio.dni))

    def test_todos(self):
        socio = self.ns.alta(self.ns.datos.generarSocio())
        self.ns.todos()
        self.assertNotEqual(self.ns.todos(),[])

    def test_modificacion(self):
        #Socio que se crea
        socio_1 = self.ns.alta(self.ns.datos.generarSocio())
        cambios = self.ns.datos.generarSocio()
        socio_1.nombre = cambios.nombre
        socio_1.apellido = cambios.apellido
        socio_1.dni = cambios.dni
        self.assertTrue(self.ns.modificacion(socio_1))