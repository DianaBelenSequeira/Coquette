# Coquette Online Store

## DESCRIPCION DEL PROYECTO

Este proyecto se basa en una tienda online, Coquette Shop, es una aplicación web diseñada para permitir a los administradores gestionar su inventario de productos de manera eficiente y sencilla. A traves de la interfaz el administrador puede visualizar la vista de la pagina web de sus clientes mas funcionalidades en el que tiene la posibilidad de editar, crear y eliminar sus productos, asi actualizando su inventario a traves de formularios creados para cada  Carousel de Productos. Desarrollado con Python, utiliza Flask como framework, SQLAlchemy para la gestión de la base de datos, y HTML con Tailwind CSS para el diseño estéticamente adaptable en dispositivos de diferentes tamaños..


## ENFOQUE Y METODOLOGIA 

Esta interfaz fue diseñada de manera que se pueda captar la esencia de la marca y un enfoque agil de usar tanto para los usuarios como los administradores. 

### Planificación

Se inició esta fase para definir los requisitos del proyecto, priorizar las funcionalidades y planificar las vistas.

### Desarrollo

El desarrollo se basó en principios de programación, manteniendo el código bien organizado y facilitando la escalabilidad del proyecto.

- Modelos de SQLAlchemy definen la estructura de la base de datos.
- Las plantillas HTML con Tailwind CSS, se usan para diseñar una interfaz de usuario limpia y responsiva.
- Flask se encargó de la lógica de aplicación, desde el manejo de rutas hasta la interacción con la base de datos.

### Pruebas

Se realizaron para asegurar la calidad del código. Esto incluyó pruebas en los modelos de datos y las funcionalidades clave de la aplicación.        


## TECNOLOGIAS UTILIZADAS

- **Flask**: Un framework de Python para desarrollar aplicaciones web. Utilizado para manejar las solicitudes del servidor, las rutas, y la lógica de la pagina.
- **SQLAlchemy**: Utilizado para interactuar con la base de datos de manera más eficiente.
- **HTML**: Utilizado para estructurar el contenido de la página web.
- **Tailwind CSS**: Se utilizó para estilizar la interfaz de la tienda online personalizada.


## EJECUCION DEL PROYECTO 

Este proyecto se ejecuta de la siguiente manera:

### Requisitos Previos

- Python 3.
- pip para la instalación de paquetes

### Instalación

1. Clonar el repositorio.
2. Instalar las dependencias pip install `-r requirements.txt` en la terminal. 
3. Iniciar la aplicación `flask run`. 


## ARQUITECTURA 
 
- `/static` : Archivos estáticos como imágenes de productos.
- `/templates` : Plantillas HTML para las vistas de la aplicación personalizadas con Tailwind CSS.
- `app.py` : El archivo principal de la aplicación Flask que configura la aplicación y define las rutas, gestionando las actualizaciones del administrador. 
- `models.py` : Define los modelos para la reacion de la base de datos.
