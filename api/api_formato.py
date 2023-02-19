# TIMEZONE = 'America/Argentina/Buenos_Aires'
COLORS = ['#80558C', '#E4D192', '#6096B4', 
          '#BFDB38', '#FC7300', '#FCF9BE',
          '#FF9F9F', '#9F8772', '#90A17D']
# colors = ['hsl(218, 70%, 50%)',"hsl(154, 70%, 50%)", 'hsl(276, 70%, 50%)', 
    #     'hsl(99, 70%, 50%)', 'hsl(105, 70%, 50%)', 
    #     ]

SEMANA_LONG = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
SEMANA = ['Lun', 'Mar', 'Mier', 'Jue', 'Vie', 'Sab', 'Dom']
# MES = ['Enero', 'Febrero', 'Marzo', 'abril',
#         'mayo', 'junio', 'julio', 'agosto', 
#         'septiembre', 'octubre', 'noviembre', 'diciembre']

def format_linea_hist(df, index, group):
    """
    Alterar df en lista formateada para grafico de linea
    Columnas: Datetime | Produccion (suma del dia)
    Retorna: datos clasificados segun index y group (DateTime Formaters)
    """

    df['x'] = df.index.strftime(index)
    df['group'] = df.index.strftime(group)
    df.rename(columns={'Produccion': 'y'}, inplace=True)

    response = []

    for i, key in enumerate(df['group'].unique()):
        df_ = df[df['group'] == key][['x', 'y']]
        response.append({
            'id': key,
            'color': COLORS[i],
            'data': df_.to_dict(orient='records')
        })

    return response


def format_calendario(df_):
    """
    Alterar df en lista formateada para grafico de calendario
    Columnas: Datetime | Produccion (suma del dia)
    """

    data = df_.to_records(index=False)
    
    return [{
        'day': x[1], 
        'value': round(x[0], 2)
    } for x in data]


def format_summary(df_, week=True):
    """
    Crear un diccionario con el total y la lista
    Se utiliza para resumir una semana de una variable particular
        Input: DataFrame ->
            Datetime: dayofweek
            Total: float (sum)
    """
    # data = df_.to_records(index=False)
    data = df_.to_dict(orient='records')
    
    response = [{
        'x': SEMANA[x['Datetime']] if week else x['Datetime'], # MES[x['Datetime'] - 1]
        'y': round(x['Total'], 2)
        } 
        for x in data ]

    if week:
        total = round(df_['Total'].sum(), 2)
    else:
        total = data[-1].get('Total')

    return {'total': total, 'dias': response}


def format_clima(df) -> list:

    df['dia'] = df['Datetime'].apply(lambda x: SEMANA[x.dayofweek])
    df['Datetime'] = df['Datetime'].dt.strftime('%d/%m/%Y')

    df.rename(inplace=True, columns={
        'Datetime': 'fecha',
        'Temp': 'temp',
        'Wind': 'viento',
        'Weather': 'clima',
        'Humidity': 'humedad',
        'Barometer': 'presion'
    })

    df['icon'] = df['clima'].apply(lambda x: 'clouds' in x)

    return df.to_dict(orient='records')