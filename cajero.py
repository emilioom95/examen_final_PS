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


# Ejemplo de uso del cajero automático
if __name__ == "__main__":
    # Crear cuentas
    cuenta1 = CuentaBancaria("Jose Moscoso", 1000)
    cuenta2 = CuentaBancaria("Ana Ortiz", 2000)

    # Inicializar el cajero automático
    cajero = CajeroAutomatico()

    # Agregar cuentas al cajero automático con PINs asociados
    cajero.agregar_cuenta(cuenta1, "9876")
    cajero.agregar_cuenta(cuenta2, "0025")

    # Simulación de operaciones en el cajero automático
    pin = input("Ingrese su PIN: ")
    if cajero.validar_pin(pin):
        print("Bienvenido al cajero automático")
        opcion = input("Seleccione una opción:\n1. Consultar saldo\n2. Realizar depósito\n3. Realizar retiro\nOpción: ")
        if opcion == "1":
            print("Saldo actual:", cajero.consultar_saldo(pin))
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            print("Nuevo saldo:", cajero.realizar_deposito(pin, cantidad))
        elif opcion == "3":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            print("Nuevo saldo:", cajero.realizar_retiro(pin, cantidad))
        else:
            print("Opción inválida")
    else:
        print("PIN inválido")
