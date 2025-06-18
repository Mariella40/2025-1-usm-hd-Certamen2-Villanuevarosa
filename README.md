# Certamen 2 - Aplicación Django

1. Creación del entorno virtual Certamen2
```bash
python -m venv Certamen2
```
2. Activación del entorno virtual

En Windows:

```bash
Certamen2\Scripts\activate
```

En macOS/Linux:

```bash
source Certamen2/bin/activate
```

3. Instalación de Django 5.1.3 y sus extensiones
```bash
pip install -r requirements.txt
```

4. Creación del proyecto Django
```bash
django-admin startproject certamenes2
```

5. Creación de la aplicación dentro del proyecto Django
```bash
cd certamenes2
python manage.py startapp MisComunas
```