from requests import get
import json
import matplotlib.pyplot as plt

def solicitar(URL: str):
    response = get(f'http://127.0.0.1:8000/{URL}/?telegram=True')
    return json.loads(response.text)


def crear_grafico(data: dict = {}, titulo: str = ''):

    x, y = data.get('columnas')

    xticks = []
    for value in data[x]:
        if ':00' in value:
            xticks.append(value)

    fig, ax = plt.subplots()
    ax.plot(data[x], data[y],alpha=0.5, color='m', linestyle = '-.', marker = 'o',markersize='5',markeredgecolor='blue',)
    ax.set_xlabel(x, color = 'm')
    ax.set_ylabel(y, color= 'm')
    ax.set_title(titulo, color='m')
    ax.set_xticks(xticks, rotation=60)

    fig.savefig('Foto.png')
    

    # plt.figure(figsize=(10,6))
    # plt.plot(data[x], data[y],alpha=0.5, color='m', linestyle = '-.', marker = 'o',markersize='5',markeredgecolor='blue',)
    # plt.xlabel(x, color = 'm')
    # plt.ylabel(y, color= 'm')
    # plt.title(titulo, color='m')
    # plt.set_xticks(xticks)
    # plt.xticks(rotation=60)
    
    # plt.savefig('Foto.png')

    




