import pandas as pd


def format_linea(df_):
    """
    Alterar df en lista formateada para grafico de linea
    Columnas: Datetime | Produccion (suma del dia)
    """
    df_['Mes'] = df_['Datetime'].dt.strftime('%b')
    df_['Datetime'] = df_['Datetime'].dt.strftime('%d')

    data = df_.to_records(index=False)
    mes = data[0][2]
    final = []
    value = []
    count = 0
    colors = ['hsl(218, 70%, 50%)',"hsl(154, 70%, 50%)", 'hsl(276, 70%, 50%)', 
        'hsl(99, 70%, 50%)', 'hsl(105, 70%, 50%)', 
        ]

    for x in data:
        if x[2] != mes:
            final.append({'id': mes, 'color': colors[count],'data': value})
            count += 1
            mes = x[2]
            value = []

        value.append({'x': x[0], 'y': x[1]})

    final.append({'id': mes, 'color': colors[count],'data': value})
    return final

def format_calendario(df_):
    """
    Alterar df en lista formateada para grafico de calendario
    Columnas: Datetime | Produccion (suma del dia)
    """
    df_['Datetime'] = df_['Datetime'].dt.strftime('%Y-%m-%d')

    data = df_.to_records(index=False)

    return [{'day': x[0], 'value': round(x[1], 2)} for x in data]