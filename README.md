# MilaBlog - Django Blog Application

Este es un blog simple creado con Django que incluye tres modelos: Author, Category y Post. Permite agregar, listar y buscar publicaciones.

## Paso a paso del proyecto:

1. **Crear el proyecto Django:**
   - Ejecuta el siguiente comando para iniciar un nuevo proyecto Django:
     ```bash
     django-admin startproject milablog
     cd milablog/
     ```

2. **Crear la aplicación Blog:**
   - Ejecuta el siguiente comando para crear una nueva aplicación llamada "blog":
     ```bash
     python3 manage.py startapp blog
     ```

3. **Configurar los Modelos:**
   - En `blog/models.py`, crea tres clases: Author, Category y Post.

4. **Realizar Migraciones y Aplicarlas:**
   - Ejecuta los siguientes comandos para gestionar las migraciones y aplicarlas:
     ```bash
     python3 manage.py makemigrations
     python3 manage.py migrate
     ```

5. **Crear Formularios:**
   - En `blog/forms.py`, crea los formularios necesarios.

6. **Configurar las Vistas:**
   - En `blog/views.py`, configura las vistas para las operaciones principales.

7. **Configurar las URLs:**
   - En `blog/urls.py`, configura las URL para las vistas creadas.

8. **Crear los Templates:**
   - Crea un directorio `blog/templates/blog/` y agrega los templates necesarios:
     - `base.html`
     - `post_list.html`
     - `add_post.html`
     - `search_form.html`
     - `search_results.html`

9. **Configurar la Búsqueda:**
   - En `blog/forms.py`, agrega el formulario de búsqueda.
   - Modifica `blog/views.py` para manejar la búsqueda.

10. **Configurar las URLs del Proyecto:**
    - En `milablog/urls.py`, incorpora las URLs de la aplicación Blog.

11. **Configurar la Aplicación en `settings.py`:**
    - En `myblog/settings.py`, añade la aplicación Blog a `INSTALLED_APPS`.

12. **Realizar Migraciones y Aplicarlas:**
    - Ejecuta los siguientes comandos para gestionar las migraciones y aplicarlas:
      ```bash
      python3 manage.py makemigrations
      python3 manage.py migrate
      ```

13. **Agregar Autores y Categorías:**
    - Usa el shell de Django para agregar algunos autores y categorías.
      ```bash
      python3 manage.py shell
      ```
      ```python
      from blog.models import Author, Category

      Author.objects.create(name='Milagros Reyna Marchesi')
      # Agrega más autores si es necesario, como en mi caso

      Category.objects.create(name='Literatura')
      # Agrega más categorías si es necesario, como en mi caso
      ```

14. **Ejecutar el Servidor de Desarrollo:**
    - Ejecuta el siguiente comando para iniciar el servidor de desarrollo:
      ```bash
      python3 manage.py runserver
      ```

## Modo de Uso

1. **Agregar Posts:**
   - Visita [http://127.0.0.1:8000/blog/add_post/](http://127.0.0.1:8000/blog/add_post/)

2. **Ver Publicaciones:**
   - Visita [http://127.0.0.1:8000/blog/posts/](http://127.0.0.1:8000/blog/posts/)

3. **Realizar una Búsqueda:**
   - Visita [http://127.0.0.1:8000/blog/search/](http://127.0.0.1:8000/blog/search/)
   - Las búsquedas se realizan por titulares.


## Agregados para el proyecto final

Ahora utilizo blog en vez de post ya que aumentaron los requisitos y necesito modificar el esquema de la db. 
1. **Agrego un nuevo model:**
   - En el archivo models.py, agrega un modelo llamado CreatorInfo:
     ```python
      class CreatorInfo(models.Model):
         name = models.CharField(max_length=255)
         bio = models.TextField()
         project_description = models.TextField()

         def __str__(self):
            return self.name
     ```

     Ejecuto las migraciones correspondientes: 
      ```bash
      python3 manage.py makemigrations
      python3 manage.py migrate
      ```

      Superusuario (admin): mila/mila2023