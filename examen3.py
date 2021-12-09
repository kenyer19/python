
from _typeshed import Self
from abc import ABC, abstractmethod

class cuentasdeahorro(ABC):
    def reralizardepositos(self,nombre, apellido, cedula):
        self.nombre = nombre    
        self.apellido = apellido
        self.cedula = cedula
        self.saldo = 0
        self.retiro = 0
        self.contador = 0
        self.cuentodedepositos = 0 
        print("Su cuenta ha sido creada")
    
    @abstractmethod
    def realizardeposito(self):
        self.vdepositos = [30,420,57,58,7,45,26,35,83,56,57,97,28,115,53,35,99,62,78,29,98,8,42,56,86,95,26,28,67,21,815,869,104,58,512,24,92,89,67,53,81,79,83,496,44,132,77,98,73,57]

    @abstractmethod
    def realizarretiro(self, retiro):
        self.retiro = retiro
        self.saldo -= self.retiro


class cuentas(cuentasdeahorro):
    def realizardeposito(self):
        super().realizardeposito
        while(self.contador < 52):
            self.contador += 1
            self.saldo += self.vdepositos
            self.vdepositos += 1




