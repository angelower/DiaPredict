proyecto_diabetes/
│
├── diabetes_app/               # Aplicación Django
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   └── diabetes/
│   │       ├── base.html
│   │       └── formulario.html
│   │       └── resultado.html
│   └── ml/                     # Módulo de Machine Learning
│       ├── __init__.py
│       ├── entrenar_modelo.py
│       └── modelo_diabetes.pkl
│
├── proyecto_diabetes/          # Configuración Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
