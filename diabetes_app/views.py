from django.shortcuts import render
from .forms import DiabetesPrediccionForm
import joblib
import os
import numpy as np

# Cargar el modelo al iniciar (una sola vez)
MODEL_PATH = "diabetes_app/ml/modelo_diabetes.pkl"
modelo = joblib.load(MODEL_PATH)

def predecir_diabetes(request):
    resultado = None
    form = DiabetesPrediccionForm()
    
    if request.method == 'POST':
        form = DiabetesPrediccionForm(request.POST)
        if form.is_valid():
            # Extraer datos del formulario
            datos = [
                form.cleaned_data['embarazos'],
                form.cleaned_data['glucosa'],
                form.cleaned_data['presion'],
                form.cleaned_data['grosor_piel'],
                form.cleaned_data['insulina'],
                form.cleaned_data['imc'],
                form.cleaned_data['hist_familiar'],
                form.cleaned_data['edad']
            ]
            
            # Convertir a array numpy y predecir
            entrada = np.array(datos).reshape(1, -1)
            prediccion = modelo.predict(entrada)[0]
            probabilidad = modelo.predict_proba(entrada)[0][1]  # Probabilidad de clase 1
            
            resultado = {
                'prediccion': 'Positivo (Diabetes)' if prediccion == 1 else 'Negativo (Sin diabetes)',
                'probabilidad': round(probabilidad * 100, 2)
            }
    
    return render(request, 'diabetes/formulario.html', {
        'form': form,
        'resultado': resultado
    })