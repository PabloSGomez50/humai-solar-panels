import pickle
import numpy as np
from keras.models import load_model

MODEL_PATH = './data/LSTM_BatchSize_2_Epochs_10_NumLayers_2_NumUnits_8_look_back_12.h5'
SCALER_PATH = './data/scaler.pkl'


def hacer_predicciones(valores_entrada, cantidad_predicciones):

    model = load_model(MODEL_PATH)
    
    with open(SCALER_PATH, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    
    # Escala los valores de entrada
    valores_entrada = np.array(valores_entrada).reshape(-1, 1)
    valores_entrada = scaler.transform(valores_entrada)

    predicciones = []
    for _ in range(cantidad_predicciones):
        # Redimensiona los valores de entrada para que coincidan con la entrada del modelo
        entrada = valores_entrada.reshape(1, 12, 1)
        # Realiza la predicción y la agrega a la lista de predicciones
        prediccion = model.predict(entrada)
        predicciones.append(prediccion[0][0])
        # Actualiza los valores de entrada con la nueva predicción
        valores_entrada = np.delete(valores_entrada, 0)
        valores_entrada = np.append(valores_entrada, prediccion)
        
    return predicciones

if __name__ == '__main__':

    valores_entrada = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.10, 0.11, 0.12])
    cantidad_predicciones = 24
    predicciones = hacer_predicciones(valores_entrada, cantidad_predicciones)
    print(predicciones)