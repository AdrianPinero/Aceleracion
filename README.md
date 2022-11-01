# Adrián Piñero
<sub>Data Analyst entry-level</sub>


**Contacto:**
* [E-mail](adrianucv@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/adrián-piñero-feligueira/)



## Contenido:
El repositorio contiene los archivos creados durante el proceso de acelereación con la empresa argentina Alkemy.

El caso del proyecto fue el de el ministerio necesitaba que ordenemos los datos para obtener un archivo con sólo la
información necesaria de cierto periodo de tiempo y de determinados lugares geográficos de una base de datos SQL.

Los datos deben ser procesados de manera que se puedan ejecutar consultas a dos universidades del total disponible para hacer análisis parciales. 

Por último, la información procesada y transformada debía ser subido a un bucket de S3. Para ello se utilizó Airflow, se generó un dag en donde habia un operator que subía el archivo al bucket.

También tuvimos un procesamiento de big data con la librería MRJob.

En este repositorio solo están los archivos en los que trabaje yo, pero fuimos un equipo de 8 y un mentor.

**Utilizamos Jira para las metodologías ágiles Scrum con sprints de una semana de duración, haciendo las respectivas ceremonias segun correspondía: Planning, Daily, Review y Retro.**


El contenido de cada carpeta es:


- Airflow: DAGs que ejecutan un ETL cada hora.
- Big_data: archivos que procesan big_data con la libreria MRJob.
- files: archivos raw y modificados que han sido extraidos o modificados.
- src: carpeta que contienes los archivos .py y los archivos .sql


---
