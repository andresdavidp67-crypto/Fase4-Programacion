# 🚀 Fase 4 - Sistema "Software FJ"
Hola compañeros, me apoye en la IA para hacer este documento y dividir el trabajo entre nosotros.

## Descripción
Proyecto colaborativo para la gestión de clientes, servicios y reservas. Enfoque: **POO + Manejo de Excepciones (`try/except`) + Registro de Logs**.

## 📌 Asignación
1. Elige el módulo de la lista que quieras desarrollar.
2. Edita este archivo `README.md` en GitHub.
3. Escribe tu nombre y usuario de GitHub en el módulo.
4. Guarda los cambios haciendo **Commit**.

---

## 🛠️ Repartición de Módulos

### Módulo 1: Logs y Excepciones Personalizadas
* **Encargado:** *(Camilo Esteban Riobamba Timana - @Camilo-Riobamba)*
* **Entregables:**
  * Módulo de registro de eventos/errores en `logs.txt`.
  * Clases de excepciones personalizadas (`ClienteInvalidoError`, `ReservaError`, `ServicioNoDisponibleError`).
  * Funciones base de logging para el resto del equipo.

### Módulo 2: Entidad Base y Clase Cliente
* **Encargado:** *(Nombre - @usuario_github)*
* **Entregables:**
  * Clase abstracta base para entidades del sistema.
  * Clase `Cliente` con encapsulación (atributos privados).
  * Validaciones de datos (cédula, correo) con lanzamiento de excepciones.

### Módulo 3: Jerarquía de Servicios
* **Encargado:** *(Andres David Paz Botina - @andresdavidp67)*
* **Entregables:**
  * Clase abstracta `Servicio` (métodos abstractos: `calcular_costo()`, `obtener_descripcion()`).
  * Clases derivadas: `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada`.
  * Polimorfismo y sobrecarga en métodos de cálculo de costos.

### Módulo 4: Gestión de Reservas
* **Encargado:** *(Nombre - @usuario_github)*
* **Entregables:**
  * Clase `Reserva` (relación Cliente-Servicio, duración, estado).
  * Métodos: `confirmar()`, `cancelar()`, `procesar_pago()`.
  * Control de excepciones para reservas o duraciones inválidas.

### Módulo 5: Menú Principal y Simulación (10 Operaciones)
* **Encargado:** *(Nombre - @usuario_github)*
* **Entregables:**
  * Archivo principal `main.py` con menú por consola.
  * Script de prueba con 10 operaciones (válidas e inválidas).
  * Verificación de captura de errores, escritura en `logs.txt` y continuidad del programa.

---

## ⚠️ Reglas de Trabajo
* **Evaluación:** La calificación individual depende exclusivamente de los *commits* registrados en GitHub.
* **Pruebas:** Validar la ejecución del código antes de hacer comit.
* **Documentación:** Comentar clases, métodos y bloques de excepciones.
