-- Tercera Pre-Entrega del Proyecto Final en CoderHouse --
# 1- Instalar dependencias

# 2- Iniciar proyecto
- Escribir en la consola: 
    "python manage.py runserver"

# StudyHub
Considero interesante crear un sitio web (full-responsive) en el que pueda guardar y ordenar mis apuntes de clases. 
El proyecto se lleva a cabo utilizando Django y Bootstrap, con el fin de practicar dicho framework de python.

# Metodos GET
- Contamos con una barra de navegación en el navbar para buscar y abrir directamente la publicación que deseamos ver. El filtrado, de momento, es por el titulo de la publicación.

- En "/apuntes" obtendremos un listado de las carreras con sus respectivas materias. Podremos filtrarlas seleccionando una carrera en especifico.

- Al clickear sobre una materia, obtendremos una lista con todas las publicaciones pertenecientes a la misma. 

- A continuación, con tan solo clickear en la fila de la publicación que deseemos ver, podremos obtener la información detallada de dicha publicación, su contenido.

# Metodos POST, creación de objetos:
- En un primer momento deberiamos de crear una carrera universitaria o rama, en la que indicaremos a que universidad pertenece y su cantidad de materias.

- A continuacion podremos ir agregando las materias en las que guardaremos cada apunte o publicación.

- Finalmente solo resta crear la publicación indicando a qué materia pertenece.
(Los modelos de Subject y Publication dependerán del modelo Career jerarquicamente)


# Modelos en la aplicación de Blog
- 1 | Career
- 2 | Subject
- 3 | Publication


