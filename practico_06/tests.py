# Implementar los casos de prueba descriptos.

import unittest
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
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        #Valida regla
        #No se repite dni
        socio_valido = Socio(dni=12121212, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(socio_valido))

        #Se repite dni
        socio_invalido = Socio(dni=12345678, nombre='Pedro', apellido='Juarez')
        self.assertRaises(DniRepetido, self.ns.regla_1, socio_invalido)


    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        #Nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Francisco javier', apellido='Perez'
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        #Apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Pe')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # Apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Gonzalez Gonzalez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2,invalido)


    def test_regla_3(self):
        self.ns.alta(Socio(dni=12345678, nombre='Juan',apellido='Perez'))

        #Validar regla
        self.assertTrue(self.ns.regla_3())


    def test_baja(self):
        socio = self.ns.alta(Socio(dni=12345678, nombre='Juan',apellido='Perez'))
        self.assertTrue(self.ns.baja(socio.id))

    def test_buscar(self):
        socio = self.ns.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
        self.assertTrue(self.ns.buscar(socio.id) == socio)

    def test_buscar_dni(self):
        socio = self.ns.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
        self.assertTrue(self.ns.buscar_dni(socio.dni) == socio)

    def test_todos(self):
        socio = self.ns.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
        self.assertTrue(len(self.ns.todos()) == 1)

    def test_modificacion(self):
        #Socio que se crea
        socio_modificar = self.ns.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
        socio_modificar.nombre = 'Moria'
        socio_modificar.apellido = 'Casan'
        socio_modificar.dni = 13264587
        if self.ns.regla_2(socio_modificar):
            self.ns.modificacion(socio_modificar)
        socio_modificado = self.ns.buscar(socio_modificar.id)
        assert socio_modificado.id == socio_modificar.id
        assert socio_modificado.nombre == 'Moria'
        assert socio_modificado.apellido == 'Casan'
        assert socio_modificado.dni == 13264587