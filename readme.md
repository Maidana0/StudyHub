# StudyHub

1. Se trata de un sitio web (responsive) para guardar y ordenar apuntes y/o resúmenes de materias universitarias.
2. Su objetivo es el de practicar el uso de Django, y algunas librerías (pillow y django-tinymce).

------------
## Funcionalidad

- Cuenta con Login, Logout, Register, ChangePassword, ForgotPassword, ChangePassword, expireSession, etc.

- Las rutas cuentan con verificaciones para mayor seguridad.

- Podrás subir y editar una imagen para tu perfil, la misma se guardará en la carpeta media y solamente una por usuario, ajustando el tamaño de la imagen automáticamente.

- Solamente los administradores pueden eliminar los objetos de Career y Subject, ya que si se borrará alguna, también se borrará todo lo que dependa de estas.

- El proyecto cuenta con un CRUD personalizado para los modelos de Career, Subject, Publication, Comment, Profile. Los primeros 4 están conectados entre sí con un ForeignKey, con la siguiente estructura y nivel jerárquico:

```
Career
	Subject
		Publication
			Comment
```

```
User
	Profile
```

- El objeto Profile se crea automáticamente después de crear un usuario y básicamente contiene la siguiente estructura:

```python
user = OneToOneField(User...)
avatar = ImageField(...)
user_publications = Publications.objects
```

## Nueva Implementación
- Gestión de Cursos:
  - Listar cursos del usuario con conteo de ausencias y exámenes pendientes.
  - Crear, editar y eliminar cursos.
  - Ocultar o mostrar cursos.

- Gestión de Faltas de cada curso:
  - Listar faltas de un curso específico.
  - Crear y eliminar faltas.

- Gestión de Exámenes de cada curso:
  - Listar exámenes de un curso específico con conteo de exámenes pendientes.
  - Crear, editar y eliminar exámenes.


```
Course (for each user)
	Absence
	Exam
```

## Instalación de Dependencias
_Recomendamos continuar dentro de un entorno virtual._

**Primero que nada debes adquirir el repositorio!**

Puedes descargar la carpeta .ZIP del repositorio o clonarlo. Para clonar este repositorio en tu máquina local, sigue estos pasos:

1. Abre una terminal o símbolo del sistema en tu computadora.
2. Navega al directorio donde deseas clonar el repositorio (por ejemplo, `cd ruta/del/directorio`).
3. Copia el siguiente comando: 

```bash
$ git clone https://github.com/Maidana0/StudyHub.git
```

**A continuación, instalaremos las dependencias:**

Asegúrate de tener Python instalado en tu sistema. Luego, desde la línea de comandos, ejecuta:


```bash
$ pip install -r requirements.txt
```

Este comando incluirá los siguientes paquetes. Si lo deseas, puedes instalarlos individualmente.

asgiref==3.8.1
Django==5.0.2
django-tinymce==3.7.1
pillow==11.1.0
python-decouple==3.8
python-dotenv==1.0.1
setuptools==76.0.0
sqlparse==0.5.3
tzdata==2025.1
wheel==0.45.1

## Iniciar Aplicación
Una vez instaladas las dependencias, deberás ejecutar los siguientes comandos en la consola para iniciar el servidor.

```bash
$ python manage.py collectstatic
$ python manage.py runserver
```

Con el primer comando, estamos recolectando todos los archivos estáticos del proyecto en un solo lugar, especificamente para el DEBUG = False
Con el "runserver" estamos inicializando el servidor en nuestro local host con el puerto estandar de django "8000":
También, podras acceder desde la siguiente url:
http://127.0.0.1:8000/

Puedes ver el siguiente video en YouTube para visualizar la navegación y funcionalidades del sitio (no incluye la última app study_manager):
https://youtu.be/IKm1dGJ566s  

------------

## Información para clonar app

Los valores de SECRET_KEY, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, DATABASE en settins.py han sido guardadas como variables de entorno en un archivo .env para mejorar la seguridad de estas. Debes configurarlas para tu proyecto.

Recuerda crear un super user (admin) y realizar las migraciones.

## Base de Datos

El proyecto en este repositorio, cuenta con una base de datos SQLite3 con algunos datos cargados para facilitar la demostración. Sin embargo puedes borrarla y crear tu propia base de datos.

El usuario administrador en la base de datos cargada es el siguiente:
	-Usuario:		  woldehtes
	-Contraseña:	StudyHub