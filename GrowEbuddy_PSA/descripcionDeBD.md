# Diagrama de la Base de Datos Actualizado

## 1. Usuarios
- **Tabla principal** para almacenar la información de los usuarios.
- **Campos**:
  - `id (PK)`: Identificador único del usuario.
  - `nombre`: Nombre del usuario.
  - `email`: Dirección de correo electrónico del usuario.
  - `ultimo_log_in`: Fecha y hora del último inicio de sesión del usuario.
  - `fecha_creacion`: Fecha en la que se creó el usuario.

## 2. Relación de Usuarios con Vpets
- Un Usuario puede tener múltiples Vpets, por lo que la relación es 1 entre la tabla Usuarios y Vpets.
- Esto permite que cada usuario tenga uno o más Vpets que gestionan independientemente.

### Descripción de Relaciones Clave:
- **Usuarios a Vpets**: Cada usuario tiene uno o más Vpets, y cada Vpet está vinculado a un único usuario.
- **Vpets a Historial_Puntos**: Un Vpet puede tener múltiples registros en Historial_Puntos que rastrean las acciones del usuario que generan puntos.
- **Historial_Puntos a Notas**: Cuando se crea o completa una nota, se registra en Historial_Puntos y se asocian los puntos ganados al Vpet del usuario.

## Proceso de Actualización del Estado del Vpet:
- Al iniciar sesión, la fecha y hora de `ultimo_log_in` se compara con la fecha y hora actual.
- Dependiendo del tiempo transcurrido, se aplican cambios en los atributos del Vpet (como estado de ánimo, hambre, energía, etc.) y su edad.
- La lógica de actualización se manejará mediante consultas SQL y/o lógica en el backend para reflejar estos cambios al inicio de sesión del usuario.

## Descripción Simplificada del Sistema de Base de Datos y sus Entidades Principales:

### Entidades Principales:
1. **Usuarios**:
   - Representa a cada persona que utiliza la aplicación.
   - Almacena información básica como nombre, correo electrónico y la última vez que inició sesión.
   - **Relación clave**: Un usuario puede tener múltiples mascotas virtuales (Vpets).

2. **Vpets (Mascotas Virtuales)**:
   - Es la entidad que representa a la mascota virtual de cada usuario.
   - Contiene datos como el nombre de la mascota, su nivel, experiencia, estado (ej. hambre, energía), puntos acumulados, y fechas de creación y modificación.
   - **Relación clave**: Cada Vpet pertenece a un único usuario, pero un usuario puede tener varios Vpets.
   - Los puntos que obtiene la mascota dependen de las acciones realizadas por el usuario en las notas.

3. **Notas**:
   - Son la base del sistema, y representan tanto notas simples como proyectos.
   - Una Nota puede actuar como un simple texto, un proyecto, o una etiqueta, dándole versatilidad.
   - Cada vez que se crea o se completa una nota, el usuario gana puntos que afectan al Vpet.
   - **Relación clave**: Las notas pueden tener relaciones entre ellas, como subnotas o pertenecer a proyectos.

4. **Historial_Puntos**:
   - Registra todas las acciones del usuario que generan puntos para su Vpet.
   - Almacena información sobre qué acción se realizó (ej. crear nota, completar nota), cuántos puntos se otorgaron y la fecha en que ocurrió.
   - **Relación clave**: Cada entrada en esta tabla está vinculada a un Vpet específico y, opcionalmente, a una Nota específica, permitiendo rastrear el origen de los puntos ganados.

5. **Necesidades_Vpet**:
   - Define las necesidades de cada Vpet, como hambre, energía, o estado de ánimo.
   - Ayuda a determinar el estado actual de la mascota y qué acciones son necesarias para su cuidado.
   - **Relación clave**: Cada Vpet tiene sus propias necesidades, que cambian con el tiempo.

6. **Acciones_Vpet**:
   - Especifica las acciones que el usuario puede realizar para satisfacer las necesidades del Vpet (ej. alimentar, jugar).
   - Cada acción tiene un efecto sobre una o más necesidades del Vpet.
   - **Relación clave**: Las acciones están asociadas a un Vpet y afectan a sus necesidades.

## Resumen del Sistema:
- Los usuarios crean Notas que pueden ser simples o proyectos, y ganan puntos al interactuar con ellas (crearlas o completarlas).
- Los puntos ganados se registran en la tabla Historial_Puntos, afectando al estado de las Vpets del usuario.
- Cada Vpet tiene sus propias Necesidades que deben ser atendidas por medio de Acciones_Vpet realizadas por el usuario.
- El último inicio de sesión del usuario se utiliza para calcular el tiempo transcurrido y ajustar el estado de la mascota virtual (edad, estado de ánimo, etc.).

Este sistema permite que la aplicación tenga una estructura versátil y conectada, donde las notas actúan no solo como elementos de gestión personal, sino que también impactan directamente en el desarrollo de la mascota virtual del usuario.