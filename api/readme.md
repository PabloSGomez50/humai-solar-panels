# Certificación de Ciencia de Datos Aplicada Humai:

La generación de electricidad, amigable con el medio ambiente es un factor fundamental para el crecimiento económico y social de cualquier país.

La instalación de sistemas generación fotovoltaicos se ha incrementado durante los últimos años, pero el rendimiento del mismo depende de muchos factores. Este proyecto busca realizar un analisis en los circuitos para demostrar el rendimiento del sistema, si tiene un margen de mejora y la prediccion del rendimiento.

Diseñaremos un plan de consumo, con predicciones, utilizando Machine Learning, brindaremos recomendaciones sobre qué cantidades utilizar para lograr un equilibrio, como por ejemplo, los horarios en que es conveniente utilizar dispositivos de alto consumo.


## Objetos

Crear una API REST que sirva de conexion entre los datos en S3 (formato .csv) y las interfaces de usuario:

- Pagina web
- Chat Bot de Telegram

## Conexion aws

Acceder a la configuracion de nginx
- sudo vim /etc/nginx/sites-enabled/fastapi_nginx

Reiniciar nginx
- sudo service nginx restart

Lista de conecciones activas del servidor
- ss -ltup 

Eliminar un proceso
- kill < pid >