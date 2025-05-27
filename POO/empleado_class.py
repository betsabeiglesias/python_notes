import datetime
from POO.coche_class import Coche
import time
from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        
   
        self.ubicacion = "Rentería"
        self.fichajes = []
        self.bono_transporte = 0

        self.__trabajando = False
        self._sueldo_hora = sueldo_hora

    @property
    def trabajando(self):
        return self.__trabajando
        
    @trabajando.setter
    def trabajando(self, estado):
        if isinstance(estado, bool):
            self.__trabajando = estado
        else:
            raise ValueError ("El estado debe ser un booleano.")
    
    @property
    def sueldo_hora(self):
        return self._sueldo_hora
    
    @sueldo_hora.setter
    def sueldo_hora(self, valor):
        if valor > 0:
            self._sueldo_hora = valor
        else:
            raise ValueError ("El sueldo deber ser positivo")


    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.trabajando = not self.trabajando
        self.fichajes.append(datetime.datetime.now())
        self.bono_transporte += 1

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion


    def __calcula_trabajo(self):
        tiempo_inicial = datetime.timedelta(0)
        entradas = self.fichajes[::2]
        salidas = self.fichajes[1::2]
        tiempo_trabajado = sum([salida - entrada for entrada, salida in zip(entradas, salidas)], start=tiempo_inicial)
        print(f"Tiempo trabajado: {tiempo_trabajado}")
        return tiempo_trabajado
    
    @abstractmethod
    def calcula_sueldo(self):
        tiempo_trabajado = self.__calcula_trabajo()
        sueldo = tiempo_trabajado.total_seconds() / 3600 * self.sueldo_hora
        sueldo += self.bono_transporte
        print(f"Sueldo: {sueldo}")
        return sueldo

    def en_activo(self):
        if not self.trabajando:
            pass
          

class Directivo(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.coche_empresa = None
        self.gasolina = 0
        
    def en_activo(self):
        if self.trabajando:
            print("Soy el directivo")
            time.sleep(3)
            print("Mi trabajo es:")
            time.sleep(3)
            print("Organizar")
            time.sleep(3)
            print("Y mandar")
            time.sleep(3)
    
    def calcula_sueldo(self):
        print("ESTÁ ABSTRRAÍDO PARA EL JEFE")
        return super().calcula_sueldo()


class Oficinista(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.bonus = 0

    def calcula_sueldo(self):
        sueldo_base = super().calcula_sueldo()
        sueldo_con_bonus = sueldo_base + self.bonus
        print (f"Sueldo con bonus: {sueldo_con_bonus}")
        return sueldo_con_bonus
    
    def en_activo(self):
        if self.trabajando:
            print("Soy el oficinista")
            time.sleep(3)
            print("Mi trabajo es:")
            time.sleep(3)
            print("Gestionar documentos")
            time.sleep(3)
            print("Y coordinar tareas")
            time.sleep(3)


class Peon(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.guardias = 0

    def cuenta_guardias(self):
        hora_limite = datetime.time(21,0)
        guardias_contadas = 0
        entradas = self.fichajes[::2]
        for entrada in entradas:
            if entrada.time() > hora_limite:
                guardias_contadas += 1
        self.guardias = guardias_contadas
        print(f"Las guardias son:{self.guardias}")
    
    def ficha(self):
        super().ficha()
        self.cuenta_guardias()

    def calcula_sueldo(self):
        sueldo_base = super().calcula_sueldo()
        if self.guardias:
            sueldo_total = sueldo_base + (self.guardias * 7000)
            print (f"El sueldo con guardias es: {sueldo_total}")
        else: print("El sueldo NO tiene guardias")
        return sueldo_total
    
    def en_activo(self):
        if self.trabajando:
            print("Soy el peón")
            time.sleep(3)
            print("Mi trabajo es:")
            time.sleep(3)
            print("Realizar tareas manuales")
            time.sleep(3)
            print("Y apoyar al equipo")
            time.sleep(3)


jefe = Directivo("Juan", "Pérez", "López")
jefe.presentarse()
jefe.coche_empresa = Coche("Seat", "Leon", 4.5, 30000)
jefe.gasolina = 300
jefe.coche_empresa.presentarse()
jefe.gasolina
jefe.ficha()
jefe.ficha()
jefe.calcula_sueldo()


peon = Peon("Luis", "González", "Martínez")
peon.presentarse()
peon.ficha()
peon.cuenta_guardias()

#/***** SCRIPT PRUEBA OFICINISTA *****/
print(__name__)
if __name__ == "__main__":
    # Crear un oficinista
    oficinista = Oficinista("Ana", "García", "Martínez")
    
    # Mostrar presentación
    oficinista.presentarse()
    
    # Simular fichajes (entrada y salida)
    print("Fichando entrada...")
    oficinista.ficha()
    oficinista.bonus = 5000
    time.sleep(1)  # espera 1 segundo para simular tiempo trabajado
    print("Fichando salida...")
    oficinista.ficha()
    
    # Calcular sueldo con bonus
    oficinista.calcula_sueldo()


#/***** SCRIPT PRUEBA PEÓN *****/
import datetime
if __name__ == "__main__":
    peon = Peon("Luis", "Fernández", "Ruiz")
    peon.presentarse()

    # Simular fichaje temprano (antes de las 21h)
    print("\nFichaje temprano:")
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=20)  # forzar hora
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=20)  # salida
    
    # Simular fichaje tarde (después de las 21h)
    print("\nFichaje tarde (guardia):")
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=22)  # forzar hora
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=23)  # salida

    # Simular otro fichaje tarde
    print("\nOtro fichaje tarde (guardia):")
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=22)  # forzar hora
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=23)  # salida

    # Calcular sueldo final
    print("\n=== SUELDO FINAL ===")
    peon.calcula_sueldo()


#/***** SCRIPT PRUEBA POLIMORFISMO *****/

if __name__ == "__main__":
    jefe = Directivo("Juan", "Pérez", "López")
    oficinista = Oficinista("Ana", "García", "Martínez")
    peon = Peon("Luis", "Fernández", "Ruiz")

    jefe.ficha()
    print("\n=== DIRECTIVO EN ACTIVO ===")
    jefe.en_activo()

    print("\n=== OFICINISTA EN ACTIVO ===")
    oficinista.en_activo()

    print("\n=== PEÓN EN ACTIVO ===")
    peon.en_activo()

    print("\n¡Todos han mostrado sus tareas!")