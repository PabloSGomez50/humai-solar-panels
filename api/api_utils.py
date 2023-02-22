from datetime import datetime, timedelta

DAYS_DIFF = 2 + 365 * 10

def get_datetimes(months = 0, days = 0, hours = 0, minutes = 0):
    """
    Funcion para obtener los registros de interes, de una semana o varios meses
    """
    
    today = datetime.today() - timedelta(days=DAYS_DIFF)

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


def get_index_group(span, sample):

    print('El valor de span:', span, 'no esta en uso')
    if sample.endswith('W'):
        index = '%m-%d'
        group = '%Y'

    elif sample.endswith('D'):
        index = '%d'
        group = '%m'

    elif sample.endswith('H'):
        index = 'Dia %d %H:%M'
        group = '%m'

    else:
        index = '%H:%M'
        group = '%d'

    return index, group