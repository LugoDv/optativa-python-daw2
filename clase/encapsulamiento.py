class CajaFuerte:
		def __init__(self, pin, ubicacion):
				self.ubicacion = ubicacion
				self.__pin = pin
				self._abierta = False
				self._registro = []

		def abrir(self, pin_intentado, usuario):
				if not self._validar_pin(pin_intentado):
						self._registrar(usuario, "PIN invalido")
						return False
				self._abierta = True
				self._registrar(usuario, "abierta")
				return True

		def cerrar(self, usuario):
				self._abierta = False
				self._registrar(usuario, "cerrada")

		def estado(self):
				return "abierta" if self._abierta else "cerrada"

		def ver_registro(self):
				return list(self._registro)

		def _validar_pin(self, pin_intentado):
				return self.__pin == pin_intentado

		def _registrar(self, usuario, evento):
				self._registro.append((usuario, evento))


caja = CajaFuerte(pin="1234", ubicacion="sala norte")
caja.abrir("0000", "ana")
caja.abrir("1234", "luis")
print(caja.estado())
print(caja.ver_registro())


    