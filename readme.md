# Certificación de Ciencia de Datos Aplicada Humai:

La generación de electricidad, amigable con el medio ambiente es un factor fundamental para el crecimiento económico y social de cualquier país.

La instalación de sistemas generación fotovoltaicos se ha incrementado durante los últimos años, pero el rendimiento del mismo depende de muchos factores. Este proyecto busca realizar un analisis en los circuitos para demostrar el rendimiento del sistema, si tiene un margen de mejora y la prediccion del rendimiento.

Diseñaremos un plan de consumo, con predicciones, utilizando Machine Learning, brindaremos recomendaciones sobre qué cantidades utilizar para lograr un equilibrio, como por ejemplo, los horarios en que es conveniente utilizar dispositivos de alto consumo.

## Miembros del proyecto

- [@Cristian Bossolasco](https://github.com/cristianbossolasco)
- [@Milagros Capriotti](https://github.com/milagroscapriotti)
- [@PabloSGomez50](https://github.com/PabloSGomez50)
## Objetivos principales

- Analizar los datos de producción actuales (última semana) y obtener los datos más relevantes para transmitirselo al usuario.

- Predicción de rendimiento a partir de datos futuros (pronóstico meteorológico) de una a dos semanas.

- Detección de fallas / anomalías, detectar disminución de la producción por defectos del panel o sistema.

## Etapas del proyecto 

    1. Seleccionar fuentes de datos que nos brinde la producción de un sistema específico, 
    en caso de ser posible, datos meteorológicos, calendario y feriados.
    
    2. Realizar la limpieza de los datos, eliminar valores nulos y normalizar 
    los datos para la aplicacion en el modelo.

    3. Visualizar la información previamente recopilada con matplotlib o seaborn.

    4. Crear un modelo de ML capaz de brindar recomendaciones al cliente, 
    a través de predicciones realizadas.

    5. Construir distintas interfaces de contacto con el usuario para mostrarle
    resultados obtenidos y graficos historicos.


## Datasets

Los datos de los sistemas de paneles solares que se utilizaron en el proyecto se obtuvieron de la empresa AusGrid: [Solar home half-hour data - 1 July 2012 to 30 June 2013](https://www.ausgrid.com.au/Industry/Our-Research/Data-to-share/Solar-home-electricity-data)

Los datos del clima se obtuvieron scrapeando la pagina , para recuperar los datos de los periodos analizados: [Time and date (Web)](https://www.timeanddate.com/weather/australia/sydney/historic?month=06&year=2012)

