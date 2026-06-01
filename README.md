# Proyecto Diabetes - Predicción con Random Forest

Aplicación monolítica desarrollada con Django y Bootstrap que utiliza un modelo de Random Forest entrenado con el dataset PIMA Indians Diabetes Database para predecir si un paciente tiene diabetes.

## Descripción del Proyecto

Esta aplicación web permite ingresar datos clínicos de un paciente y obtener una predicción sobre la probabilidad de que tenga diabetes. El modelo de Machine Learning fue entrenado con el dataset clásico de los indios PIMA, alcanzando una precisión aproximada del 75-80%.

### Características principales
- Formulario interactivo con validación de datos
- Predicción en tiempo real usando Random Forest
- Visualización de probabilidad de diabetes
- Interfaz responsive con Bootstrap 5
- Modelo persistente en archivo .pkl

## Estructura del Proyecto

```
proyecto_diabetes/
│
├── diabetes_app/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── diabetes/
│   │       ├── base.html
│   │       ├── formulario.html
│   │       └── resultado.html
│   ├── ml/
│   │   ├── __init__.py
│   │   ├── entrenar_modelo.py
│   │   └── modelo_diabetes.pkl
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── proyecto_diabetes/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md

```


## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes)
- Conexión a internet (para descargar el dataset)

## Instalación

### 1. Clonar o crear el proyecto

```bash
mkdir proyecto_diabetes
cd proyecto_diabetes
```

### 2. Crear y activar entorno virtual

##### Windows 

```bash
python -m venv venv
venv\Scripts\activate
```

##### Linux/Mac 

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalación de dependencias

```bash
pip install -r requirements.txt
```

### 4. Iniciar el servidor

```bash
python manage.py runserver
```