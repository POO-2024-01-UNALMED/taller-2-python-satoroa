class Asiento:
    def __init__(self, color, precio, registro):
        self.colores_permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in self.colores_permitidos:
            self.color = color
        else:
            self.color = "negro"  # color por defecto si el color dado no es permitido
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevo_color):
        if nuevo_color in self.colores_permitidos:
            self.color = nuevo_color

class Motor:
    def __init__(self, cilindros, tipo, registro):
        self.cilindros = cilindros
        self.tipos_permitidos = ["electrico", "gasolina"]
        if tipo in self.tipos_permitidos:
            self.tipo = tipo
        else:
            self.tipo = "gasolina"  # tipo por defecto si el tipo proporcionado no es permitido
        self.registro = registro

    def cambiarRegistro(self, nuevo_registro):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo):
        if nuevo_tipo in self.tipos_permitidos:
            self.tipo = nuevo_tipo

class Auto:
    cantidadCreados = 0 #atributo de clase

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos  # esto es una lista de objetos Asiento
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        return len([asiento for asiento in self.asientos if asiento is not None])

    def verificarIntegridad(self):
        registros = [asiento.registro for asiento in self.asientos if asiento is not None]
        registros.append(self.motor.registro)
        registros.append(self.registro)
        if len(set(registros)) == 1:
            return "Auto original"
        else:
            return "Las piezas no son originales"
    
    
