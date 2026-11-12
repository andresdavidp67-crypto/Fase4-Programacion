from abc import ABC, abstractmethod
# Importamos la excepción personalizada del Módulo 1 (asumiendo que tu compañero la hará)
# Nota: Si al probarlo te da error de importación, puedes crear una clase temporal 
# class ServicioNoDisponibleError(Exception): pass  para hacer tus pruebas locales.
try:
    from modulo1_excepciones import ServicioNoDisponibleError
except ImportError:
    class ServicioNoDisponibleError(Exception):
        pass # Clase temporal por si el Módulo 1 aún no está subido

# ==========================================
# 1. CLASE ABSTRACTA BASE
# ==========================================
class Servicio(ABC):
    def __init__(self, nombre_servicio, tarifa_base, disponible=True):
        self.nombre_servicio = nombre_servicio
        self.tarifa_base = tarifa_base
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, duracion, *args, **kwargs):
        """Método abstracto que debe ser implementado por las clases hijas."""
        pass

    @abstractmethod
    def obtener_descripcion(self):
        """Método abstracto para describir el servicio."""
        pass

    def validar_disponibilidad(self):
        """Método general para validar si el servicio se puede usar."""
        if not self.disponible:
            raise ServicioNoDisponibleError(f"El servicio '{self.nombre_servicio}' no está disponible en este momento.")


# ==========================================
# 2. CLASES DERIVADAS (HERENCIA Y POLIMORFISMO)
# ==========================================

class ReservaSala(Servicio):
    def __init__(self, nombre_servicio, tarifa_base, capacidad_personas):
        super().__init__(nombre_servicio, tarifa_base)
        self.capacidad_personas = capacidad_personas

    # POLIMORFISMO: Implementación específica para Salas
    def obtener_descripcion(self):
        return f"Sala de estudio: {self.nombre_servicio} (Capacidad: {self.capacidad_personas} personas). Tarifa base: ${self.tarifa_base}/hora."

    # SOBRECARGA SIMULADA: *args y **kwargs permiten enviar parámetros extra opcionales
    def calcular_costo(self, duracion, *args, **kwargs):
        self.validar_disponibilidad()
        
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a cero.")

        costo_total = self.tarifa_base * duracion
        
        # Sobrecarga: Si se envía un descuento por kwargs
        if 'descuento' in kwargs:
            costo_total -= costo_total * (kwargs['descuento'] / 100)
            
        # Sobrecarga: Si se envía un recargo por args (ej. uso de proyector)
        if len(args) > 0:
            costo_total += args[0] # Se suma el valor extra
            
        return costo_total


class AlquilerEquipo(Servicio):
    def __init__(self, nombre_servicio, tarifa_base, tipo_equipo):
        super().__init__(nombre_servicio, tarifa_base)
        self.tipo_equipo = tipo_equipo

    def obtener_descripcion(self):
        return f"Alquiler de Equipo: {self.nombre_servicio} (Tipo: {self.tipo_equipo}). Tarifa base: ${self.tarifa_base}/hora."

    def calcular_costo(self, duracion, *args, **kwargs):
        self.validar_disponibilidad()
        
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a cero.")

        # Los equipos cobran un seguro obligatorio
        seguro = 10.0 
        costo_total = (self.tarifa_base * duracion) + seguro
        
        # Sobrecarga: Impuesto extra si se pasa por argumento
        if len(args) > 0:
            costo_total += args[0] 
            
        return costo_total


class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre_servicio, tarifa_base, area_conocimiento):
        super().__init__(nombre_servicio, tarifa_base)
        self.area_conocimiento = area_conocimiento

    def obtener_descripcion(self):
        return f"Asesoría Especializada: {self.nombre_servicio} (Área: {self.area_conocimiento}). Tarifa base: ${self.tarifa_base}/hora."

    def calcular_costo(self, duracion, *args, **kwargs):
        self.validar_disponibilidad()
        
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a cero.")

        costo_total = self.tarifa_base * duracion
        
        # Sobrecarga: Si el cliente es VIP (kwargs), se cobra un 20% más
        if kwargs.get('es_vip') == True:
            costo_total *= 1.20
            
        return costo_total