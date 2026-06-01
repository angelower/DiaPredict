import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def entrenar_y_guardar_modelo():
    # 1. Cargar dataset PIMA (puedes descargarlo de Kaggle o usar este URL)
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    column_names = ['embarazos', 'glucosa', 'presion', 'grosor_piel', 'insulina', 
                    'imc', 'hist_familiar', 'edad', 'resultado']
    
    df = pd.read_csv(url, names=column_names)
    
    print("Primeras 5 filas:")
    print(df.head())
    print(f"\nDistribución de clases:\n{df['resultado'].value_counts()}")
    
    # 2. Separar características (X) y objetivo (y)
    X = df.drop('resultado', axis=1)
    y = df['resultado']
    
    # 3. Dividir entrenamiento/prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Entrenar Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 5. Evaluar modelo
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n✅ Precisión del modelo: {accuracy:.4f}")
    print("\nReporte de clasificación:")
    print(classification_report(y_test, y_pred))
    
    # 6. Guardar modelo en archivo .pkl
    modelo_path = os.path.join(os.path.dirname(__file__), 'modelo_diabetes.pkl')
    joblib.dump(model, modelo_path)
    print(f"\nModelo guardado en: {modelo_path}")
    
    return model

if __name__ == "__main__":
    entrenar_y_guardar_modelo()