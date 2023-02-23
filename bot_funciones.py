from requests import get
import json
import matplotlib.pyplot as plt

def solicitar(URL: str, ID:int=1):
    response = get(f'http://127.0.0.1:8000/{URL}?telegram=True&user_id={ID}')
    # response = get(f'https://spg50.site/{URL}?telegram=True&user_id={ID}')
    return json.loads(response.text)
    


def crear_grafico(data: dict = {}, titulo: str = ''):

    x, y = data.get('columnas')

    # xticks = []
    # for value in data[x]:
    #     if ':00' in value:
    #         xticks.append(value)

    fig, ax = plt.subplots(figsize=(8,10))
    ax.plot(data[x], data[y],alpha=0.5, color='m', linestyle = '-.', marker = 'o',markersize='5',markeredgecolor='blue',)
    ax.set_xlabel(x, color = 'm')
    ax.set_ylabel(y, color= 'm')
    ax.set_title(titulo, color='m')
    ax.set_xticklabels(data[x],rotation=90)
    fig.set_size_inches(8,6)

    fig.savefig('Foto.png', bbox_inches='tight')
    

  

    




