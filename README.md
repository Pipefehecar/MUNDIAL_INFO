
# API Copa Mundial FIFA 2022 ⚽
Esta api registra información para los equipos, jugadores y directivos participantes del mundial 2022

## Tecnologias usadas 🔥
* [Django](https://www.djangoproject.com/): Un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como modelo–vista–controlador (MVC).
* [DRF](www.django-rest-framework.org/): Una herramienta estandarizada para la creación de APIs con Django
* [Postgresql](https://www.postgresql.org/): Un poderoso sistema de base de datos relacional de objetos de código abierto con más de 30 años de desarrollo
* [Swagger](https://www.postgresql.org/): Sistema gestor de documentacion
## Instalación 💡
* Empecemos clonando el este repositorio:
    ```bash
        $ git clone https://github.com/Pipefehecar/MUNDIAL_INFO.git
    ```
* Muevete al directorio del proyecto:
    ```bash
        $ cd MUNDIAL_INFO
    ```

* Asegúrese de tener Python instalado globalmente en su computadora. De no ser asi, puedes obtener python [aqui](https://www.python.org").

* Crea tu entorno virtual y activalo:
    ```bash
        $ py -m  venv venv
        $ venv/scripts/activate
    ``` 

* Instala postgresql y crea la base de datos:
    ```bash
        $ CREATE DATABASE mundialqatar2022;
    ``` 
* Configura la db en los settings de tu proyecto, deberia quedarte algo como esto:
    ```bash
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'mundialqatar2022',
                'USER': 'postgres',
                'PASSWORD': '1234',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }


* #### Dependencies

  
    3. Instala las dependencias de la aplicacion:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Realiza las migraciones
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Hora de correr esto 🚀 
    Despiega la api así:
    ```bash
        $ python manage.py runserver
    ```
    En esta ruta encontraras la documentacion, registra equipos, jugadores, directivos y pruebala!
    ```
        http://127.0.0.1:8000/docs/
    ```
