import pickle
import numpy as np

MODEL_PATH = '../obtener_predicciones/LSTM_BatchSize_2_Epochs_10_NumLayers_2_NumUnits_8_look_back_12.pkl'
SCALER_PATH = '../obtener_predicciones/scaler.pkl'

model = pickle.load(open(MODEL_PATH, 'rb'))
scaler = pickle.load(open(SCALER_PATH, 'rb'))

def hacer_predicciones(valores_entrada, cantidad_predicciones):
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