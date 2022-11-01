import logging
from pathlib import Path

import pandas as pd
import psycopg2
from decouple import config


def extraer_univ_jfk():
    """Extrae los datos de la Universidad J.F. Kennedy y guarda la información
    en un archivo .csv"""
    logging.info("Extrayendo datos de la Universidad J.F. Kennedy")
    # Creo la conexión a la base de datos (PostgreSQL)
    conn = psycopg2.connect(
        database=config("DB_NAME"),
        user=config("DB_USER"),
        password=config("DB_PASS"),
        host=config("DB_HOST"),
        port=config("DB_PORT"),
    )

    ruta = Path(__file__).parent.parent.parent / "src" / "sql"
    # Ejecuto la query de SQL para seleccionar los datos a extraer
    with open(ruta / "query_universidad_j_f_kennedy.sql", "r") as archivo:
        comando = archivo.read()
    data = pd.read_sql_query(comando, conn)
    # Guardo el archivo .csv
    ruta_csv = Path.cwd() / "files" / "raw" / "univ_jfk_raw.csv"
    data.to_csv(ruta_csv, index=False)
