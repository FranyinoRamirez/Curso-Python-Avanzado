"""
¡Hola a todos! 🚀💻 Espero que estén listos para programar. Aquí les dejo el reto técnico de hoy enfocado en Python y Programación Orientada a Objetos. 🐍🔥

Vamos a practicar herencia, clases, listas, bucles y condicionales. ¡Cero excusas, vamos a codear! 🛠️

Nivel: Fácil 🟢
Ejercicio 1: Gestión de Inventario Tecnológico
Enunciado: Crear un sistema básico para llevar el registro de dispositivos en un almacén tecnológico. El sistema debe distinguir entre un dispositivo genérico y un teléfono inteligente.
Requerimientos:
1️⃣ Definir una clase Dispositivo con un atributo de clase cantidad_total_registrada (inicia en 0).
2️⃣ Atributos de instancia: marca, modelo y encendido (booleano, por defecto Falso). Al instanciar, aumentar cantidad_total_registrada en 1.
3️⃣ Método cambiar_estado() que invierta el valor de encendido usando un condicional.
4️⃣ Clase Telefono que herede de Dispositivo y agregue el atributo aplicaciones (lista vacía).
5️⃣ Método instalar_app(nombre_app) en Telefono que agregue la cadena a la lista de aplicaciones.
6️⃣ Función externa mostrar_telefonos_encendidos(lista_telefonos) que reciba una lista de teléfonos, y con un bucle y condicional, imprima marca y modelo solo de los que estén encendidos.

Nivel: Intermedio 🟡
Ejercicio 2: Sistema de Puntuación de Videojuego
Enunciado: Desarrollar la lógica base para personajes de un videojuego, con jugadores normales y VIP.
Requerimientos:
1️⃣ Clase Jugador con atributo de clase puntuacion_base.
2️⃣ Atributos de instancia: nombre_usuario y puntos_actuales (inicia con el valor de puntuacion_base).
3️⃣ Método ganar_puntos(cantidad) que sume los puntos recibidos.
4️⃣ Clase JugadorVIP que herede de Jugador, añadiendo el atributo de instancia multiplicador.
5️⃣ Método ganar_puntos_vip(cantidad) en JugadorVIP que multiplique la cantidad por el multiplicador y lo sume a los puntos actuales.
6️⃣ Función externa filtrar_mejores_jugadores(lista_jugadores, puntaje_minimo) que recorra la lista con un bucle y retorne una nueva lista con los nombres de quienes superen o igualen el puntaje mínimo.

Nivel: Avanzado 🔴
Ejercicio 3: Simulador de Flota de Vehículos
Enunciado: Simular el consumo de combustible de una flota de reparto (vehículos estándar y camiones).
Requerimientos:
1️⃣ Clase Vehiculo con atributo de clase costo_por_litro.
2️⃣ Atributos de instancia: matricula, combustible_litros y en_ruta (booleano).
3️⃣ Método viajar(kilometros) que reste 1 litro por cada 10km si hay combustible. Si llega a 0, fijar en 0, cambiar en_ruta a Falso y avisar que no hay gasolina.
4️⃣ Clase Camion que herede de Vehiculo con el atributo cargas_entregadas (lista de cadenas).
5️⃣ Método entregar_carga() en Camion que elimine el último elemento de la lista si no está vacía.
6️⃣ Función externa simular_jornada(lista_vehiculos, distancias_a_recorrer) que use bucles para hacer que cada vehículo viaje una distancia. Si es un camión y sigue en ruta tras viajar, debe entregar una carga.

¡Éxito con el código, equipo! Muestren de qué están hechos. 💪🧠 #Python #CodingChallenge #OOP
"""

# Nivel: Fácil 🟢


class Dispositivo:
    cantidad_total_registrada = 0

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

        Dispositivo.cantidad_total_registrada += 1

    def modelos_marcas(self):

        print(
            f"Este modelo {self.modelo} de la marca {self.marca} es de la buena, te la recomiendo. "
        )

    def cambiar_estado(self):
        if self.encendido:
            self.encendido = False
        else:
            self.encendido = True


class Telefono(Dispositivo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.aplicaciones = []

    def instalar_app(self, nombre_app):
        self.aplicaciones.append(nombre_app)

    def mostrar_apps(self):
        print(self.aplicaciones)


def mostrar_telefonos_encendidos(lista_telefonos):
    for telefono in lista_telefonos:
        if telefono.encendido:
            print(f"{telefono.marca} {telefono.modelo}")


telefono_1 = Telefono("Motorola", "G75")
telefono_2 = Telefono("Samsung", "Galaxy S23")


activar_dispositivo = Dispositivo("Motorola", "G75")
activar_dispositivo.modelos_marcas()
activar_dispositivo.cambiar_estado()
telefono_1.cambiar_estado()
mi_lista_de_telefonos = [telefono_1, telefono_2]
mostrar_telefonos_encendidos(mi_lista_de_telefonos)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Nivel: Intermedio 🟡


class Jugador:
    puntuacion_base = 100

    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self.puntos_actuales = self.puntuacion_base

    def ganar_puntos(self, cantidad):
        self.puntos_actuales += cantidad


class JugadorVIP(Jugador):
    def __init__(self, nombre_usuario, multiplicador):
        super().__init__(nombre_usuario)
        self.multiplicador = multiplicador

    def ganar_puntos_vip(self, cantidad):
        self.puntos_actuales += cantidad * self.multiplicador


def filtrar_mejores_jugadores(lista_jugadores, puntaje_minimo):

    mejores_nombres = []

    for jugador in lista_jugadores:
        if jugador.puntos_actuales >= puntaje_minimo:
            mejores_nombres.append(jugador.nombre_usuario)

    return mejores_nombres


j1 = Jugador("Jugador ")
j2 = JugadorVIP("Jugador 2", 2)
j3 = Jugador("Jugador 3")
j4 = JugadorVIP("Jugador 4", 3)

lista_jugadores = [j1, j2, j3, j4]

j1.ganar_puntos(50)
j2.ganar_puntos_vip(100)
j3.ganar_puntos(200)
j4.ganar_puntos_vip(150)

mejores_jugadores = filtrar_mejores_jugadores(lista_jugadores, 200)
print(mejores_jugadores)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Nivel: Avanzado 🔴


class Vehiculo:

    costo_por_litro = 1.5

    def __init__(self, matricula, combustible_litros):
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.en_ruta = True

    def viajar(self, kilometros):
        if not self.en_ruta:
            print(f"El vehículo {self.matricula} no puede viajar, ya no está en ruta.")
            return

        litros_consumidos = kilometros / 10
        self.combustible_litros -= litros_consumidos

        if self.combustible_litros <= 0:
            self.combustible_litros = 0
            self.en_ruta = False
            print(
                f"¡Alerta! El vehículo {self.matricula} se ha quedado sin gasolina en el trayecto."
            )
        else:
            print(
                f"Vehículo {self.matricula} recorrió {kilometros}km y le quedan {self.combustible_litros} litros."
            )


class Camion(Vehiculo):
    def __init__(self, matricula, combustible_litros, cargas_entregadas):
        super().__init__(matricula, combustible_litros)
        self.cargas_entregadas = cargas_entregadas

    def entregar_carga(self):
        if len(self.cargas_entregadas) > 0:
            carga_entregada = self.cargas_entregadas.pop()
            print(
                f"El camión {self.matricula} ha entregado exitosamente: {carga_entregada}"
            )
        else:
            print(f"El camión {self.matricula} ya no tiene cargas para entregar.")


def simular_jornada(lista_vehiculos, distancias_a_recorrer):
    print("\n--- INICIO DE LA JORNADA ---")

    for vehiculo, distancia in zip(lista_vehiculos, distancias_a_recorrer):
        print(f"\n-> Turno de {vehiculo.matricula}:")

        vehiculo.viajar(distancia)

        if isinstance(vehiculo, Camion) and vehiculo.en_ruta:
            vehiculo.entregar_carga()


vehiculo_estandar = Vehiculo("V-123", 5)
camion_reparto = Camion("C-999", 50, ["Televisor", "Refrigerador", "Lavadora"])

lista_v = [vehiculo_estandar, camion_reparto]
distancias = [60, 100]

simular_jornada(lista_v, distancias)
