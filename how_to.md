Nome do Projeto: 

Objetivo:

------------------------------------------------------
**CRIANDO O PROJETO**
------------------------------------------------------
# criando os diretórios em 
$ mkdir Dev
$ cd Dev
$ mkdir Projdocs 
$ cd Projdocs 

**criar e ativar a venv**
$ python3 -m venv env
$ source ./env/bin/activate

(venv) $ pip install django
(venv) $ django-admin startproject projdocs .

# abrindo o projeto no VSCode
(venv) $ code .

------------------------------------------------------
**CONFIGURAÇÕES INICIAIS**
------------------------------------------------------
- F1 > select interpreter (python)

no arquivo settings.py
 - import os
 - 'DIRS': ['templates'],
 - 'NAME': BASE_DIR / 'bi_portal.sqlite3',
 - LANGUAGE_CODE = 'pt-br'
 - TIME_ZONE = 'America/Sao_Paulo'
 - STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),)

# no arquivo Powershell:
> python manage.py migrate
> python manage.py createsuperuser
  > admin
  > Django@2021
> python manage.py runserver

------------------------------------------------------
**no VSCode: Configurações Iniciais do Projeto**
------------------------------------------------------

no arquivo Powershell:
> pip install django-admin-interface

no arquivo settings.py (antes do 'django.contrib.admin'):

INSTALLED_APPS = (
    'admin_interface',
    'colorfield',
    #...
    'django.contrib.admin',

> python manage.py migrate
> python manage.py collectstatic

-- Instalando os Temas:
> python manage.py loaddata admin_interface_theme_django.json
> python manage.py loaddata admin_interface_theme_foundation.json
> Run python manage.py loaddata admin_interface_theme_bootstrap.json
> python manage.py loaddata admin_interface_theme_uswds.json

> python manage.py runserver

href="{% url 'contact' %}"

------------------------------------------------------
-- Conectando DJAngo ao PostgreSQL
------------------------------------------------------
- Instalar o postgresql
- Criar um Database
- no arquivo settings.py
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'bi_portal',
    'USER': 'postgres',
    'PASSWORD': 'Filespy@010',
    'HOST': '127.0.0.1',
    'PORT': '5432'
    }
}

> pip install psycopg2
> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser

------------------------------------------------------
-- no VSCode: Criando Templates e URl's p/ as páginas
-- principais: index.html, sobre.html, portal.html
------------------------------------------------------
na raiz do projeto:
- criar a pasta \templates
  .index.html
  .base.html
  .sobre.html
  .portal.html
- criar a pasta \static
- criar a pasta \static, 
  .\css 
  .\img
  .\js


------------------------------------------------------
-- CRIANDO UM APP - BIADMIN
------------------------------------------------------

- python manage.py startapp bi_admin

Dentro da pasta do app bi_admin, criar a pasta templates
 - cd bi_admin
 - md templates
 - cd templates
 - md bi_admin

Dentro da pasta \bi_admin\templates\bi_admin, 
 - criar o arquivo: bi_admin_home.html
 - colar o conteudo base:
   {% extends 'base.html' %}
   {% load static %}

  {% block content %}
	<h2> BI AMIN - HOME </h2>
  {% endblock %}

#=======================================================
Dentro da pasta do app \bi_admin, 
 - criar o arquivo urls.py
 - dentro de url.py colar o código:

	from django.conf.urls import url
	from . import views

	urlpatterns = [
		url(r'^$', views.bi_admin_home),
	]

#=======================================================
Dentro da pasta do App em views.py (apagar tudo e) colar o código:

from django.shortcuts import render

def artigos_home(request):
  return render(request, 'bi_admin/bi_admin_home.html')

Registrar o App: Na pasta do projeto, 
 - no arquivo settings.py, 'bi_admin',

No Home do projeto, dentro do arquivo urls.py, registrar:
urlpatterns = [
    ...
    url(r'^artigos/', include('bi_admin_home.urls')),    


