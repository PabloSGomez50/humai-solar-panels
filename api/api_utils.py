from datetime import datetime, timedelta

DAYS_DIFF = 2 + 365 * 10

def get_datetimes(months = 0, days = 0, hours = 0, minutes = 0):
    """
    Funcion para obtener los registros de interes, de una semana o varios meses
    """
    
    today = datetime.utcnow() - timedelta(days=DAYS_DIFF, hours=3)

    if months != 0:
        mes = today.month + 1
        # dia = today.day
        anio = today.year
        
        if mes - months < 1:
            mes += 12
            anio -= 1 

        min_day = datetime(year=anio, month=mes - months, day=1)
    else:
        min_day = today - timedelta(days=days, minutes = minutes, hours=hours)


    lim_min = min_day.strftime('%Y-%m-%d %H:%M')
    # lim_max = today.strftime('%Y-%m-%d') + ' 23:59'
    lim_max = today.strftime('%Y-%m-%d %H:%M')

    return (lim_min, lim_max)

def get_time_predict():
    """ Fucion que devuelve los limites para utilizar las horas correspondientes"""
    today = datetime.utcnow() - timedelta(days=DAYS_DIFF, hours=3)
    # today = datetime(year=today.year, month=today.month, day=today.day)
    # print(today.minute, today.hour)

    if today.minute <= 30:
        today = today - timedelta(hours=1)

    l_max = today.strftime('%Y-%m-%d %H:00')
    t_min = today - timedelta(hours=11)
    l_min = t_min.strftime('%Y-%m-%d %H:00')

    print(l_min, l_max)

    return l_min, l_max


def get_time_future_predict():
    """ Fucion que devuelve los limites para utilizar las horas correspondientes"""
    values = []
    today = datetime.utcnow() - timedelta(days=DAYS_DIFF, hours=3) 
    # today = datetime(year=today.year, month=today.month, day=today.day)
    # print(today.minute, today.hour)

    if today.minute <= 30:
        today = today - timedelta(hours=1)

    today = today + timedelta(hours=1)
    # l_min = today.strftime('%Y-%m-%d %H:00')
    for i in range(0, 24):
        t_max = today + timedelta(hours=i)
        values.append(t_max.strftime('%Y-%m-%d %H:00'))

    # l_max = t_max.strftime('%Y-%m-%d %H:00')

    # print(l_min, l_max)

    return values

def get_index_group(sample, telegram):

    # print('El valor de span:', span, 'no esta en uso')
    if sample.endswith('W'):
        index = '%m-%d'
        group = '%Y'

    elif sample.endswith('D'):
        index = '%d'
        group = '%m'

    elif sample.endswith('H'):
        if telegram:
            index = 'Dia %d %HHs'
        else:
            index = 'Dia %d %H:%M'
        group = '%m'

    else:
        index = '%H:%M'
        group = '%d'

    return index, group