from django import forms

class DiabetesPrediccionForm(forms.Form):
    embarazos = forms.IntegerField(label="Número de embarazos", min_value=0, max_value=20)
    glucosa = forms.FloatField(label="Glucosa (mg/dL)", min_value=0, max_value=300)
    presion = forms.FloatField(label="Presión arterial (mm Hg)", min_value=0, max_value=150)
    grosor_piel = forms.FloatField(label="Grosor de piel (mm)", min_value=0, max_value=100)
    insulina = forms.FloatField(label="Insulina (µU/mL)", min_value=0, max_value=900)
    imc = forms.FloatField(label="Índice de masa corporal (IMC)", min_value=0, max_value=70)
    hist_familiar = forms.FloatField(label="Historia familiar (función diabetes)", min_value=0, max_value=3)
    edad = forms.IntegerField(label="Edad (años)", min_value=0, max_value=120)