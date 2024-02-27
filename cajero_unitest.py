import unittest

class CuentaBancaria:
    def __init__(self, persona, saldo=0):
        self.persona = persona
        self.saldo = saldo

    def consultar_saldo(self):
        return self.saldo

    def realizar_deposito(self, cantidad):
        self.saldo += cantidad
        return self.saldo

    def realizar_retiro(self, cantidad):
        if cantidad > self.saldo:
            return "Saldo insuficiente"
        else:
            self.saldo -= cantidad
            return self.saldo

class CajeroAutomatico:
    def __init__(self):
        self.cuentas = {}

    def agregar_cuenta(self, cuenta, pin):
        self.cuentas[pin] = cuenta

    def validar_pin(self, pin):
        return pin in self.cuentas

    def consultar_saldo(self, pin):
        if self.validar_pin(pin):
            cuenta = self.cuentas[pin]
            return cuenta.consultar_saldo()
        else:
            return "PIN inválido"

    def realizar_deposito(self, pin, cantidad):
        if self.validar_pin(pin):
            cuenta = self.cuentas[pin]
            return cuenta.realizar_deposito(cantidad)
        else:
            return "PIN inválido"

    def realizar_retiro(self, pin, cantidad):
        if self.validar_pin(pin):
            cuenta = self.cuentas[pin]
            return cuenta.realizar_retiro(cantidad)
        else:
            return "PIN inválido"

class TestCuentaBancaria(unittest.TestCase):
    def setUp(self):
        self.cuenta = CuentaBancaria("Jose Moscoso", 1000)

    def test_consultar_saldo(self):
        self.assertEqual(self.cuenta.consultar_saldo(), 1000)

    def test_realizar_deposito(self):
        self.assertEqual(self.cuenta.realizar_deposito(500), 1500)

    def test_realizar_retiro_suficiente(self):
        self.assertEqual(self.cuenta.realizar_retiro(500), 500)

    def test_realizar_retiro_insuficiente(self):
        self.assertEqual(self.cuenta.realizar_retiro(2000), "Saldo insuficiente")

class TestCajeroAutomatico(unittest.TestCase):
    def setUp(self):
        self.cuenta1 = CuentaBancaria("Jose Moscoso", 1000)
        self.cuenta2 = CuentaBancaria("Ana Ortiz", 2000)
        self.cajero = CajeroAutomatico()
        self.cajero.agregar_cuenta(self.cuenta1, "9876")
        self.cajero.agregar_cuenta(self.cuenta2, "0025")

    def test_validar_pin_existente(self):
        self.assertTrue(self.cajero.validar_pin("9876"))

    def test_validar_pin_inexistente(self):
        self.assertFalse(self.cajero.validar_pin("0000"))

    def test_consultar_saldo(self):
        self.assertEqual(self.cajero.consultar_saldo("9876"), 1000)

    def test_realizar_deposito(self):
        self.assertEqual(self.cajero.realizar_deposito("9876", 325), 1325)

    def test_realizar_retiro_suficiente(self):
        self.assertEqual(self.cajero.realizar_retiro("9876", 700), 300)

    def test_realizar_retiro_insuficiente(self):
        self.assertEqual(self.cajero.realizar_retiro("9876", 3000), "Saldo insuficiente")

if __name__ == '__main__':
    unittest.main()
