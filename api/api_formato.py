# import pandas as pd

# TIMEZONE = 'America/Argentina/Buenos_Aires'
COLORS = ['#80558C', '#E4D192', '#6096B4', 
          '#BFDB38', '#FC7300', '#FCF9BE',
          '#FF9F9F', '#9F8772', '#90A17D']
# colors = ['hsl(218, 70%, 50%)',"hsl(154, 70%, 50%)", 'hsl(276, 70%, 50%)', 
    #     'hsl(99, 70%, 50%)', 'hsl(105, 70%, 50%)', 
    #     ]


def format_linea_semana(df_) -> list:
    """
    Alterar df en lista formateada para grafico de linea
    Columnas: Datetime | Produccion (suma del semana)
    Retorna: datos clasificados por semanas
    """

    print(df_)

    return []


def format_linea_dia(df_, format) -> list:
    """
    Alterar df en lista formateada para grafico de linea
    Columnas: Datetime | Produccion (suma del dia)
    Retorna: datos clasificados por dias
    """

    # df_.index = df_.index.tz_localize(TIMEZONE)
    
    df_['group'] = df_.index.strftime('%b')
    df_['index'] = df_.index.strftime('%d')

    # Data es lista de tuplas (valor, mes, dia)
    data = df_.to_records(index=False)
    mes = data[0][1]
    final = []
    value = []
    count = 0

    for x in data:
        if x[1] != mes:
            final.append({'id': mes, 'color': COLORS[count], 'data': value})
            count += 1
            mes = x[1]
            value = []

        value.append({'x': x[2], 'y': x[0]})

    final.append({'id': mes, 'color': COLORS[count], 'data': value})

    return final


def format_linea_horas(df_):
    """
    Alterar df en lista formateada para grafico de linea
    Columnas: Datetime | Produccion (suma del dia)
    Retorna: datos clasificados por horas y minutos
    """



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


def format_summary(df_):
    # semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    semana = ['Lun', 'Mar', 'Mier', 'Jue', 'Vie', 'Sab', 'Dom']
    data = df_.to_records(index=False)
    
    total = round(sum(map(lambda x: x[1], data)), 2)
    response = [{
        'x': semana[x[0]], 
        'y': round(x[1], 2)
        } 
        for x in data ]

    # response.append({'day': 'Total', 'value': total})

    return {'total': total, 'dias': response}

# def format_summary(df_):
#     semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
#     data = df_.to_records(index=False)
    
#     total = round(sum(map(lambda x: x[1], data)), 2)
#     response = [{
#         'day': semana[x[0]], 
#         'value': round(x[1], 2)
#         } 
#         for x in data ]

#     # response.append({'day': 'Total', 'value': total})

#     return {'total': total,'dias': response}

