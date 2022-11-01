from extract_fac_latam import extraer_latinoam
from extract_univ_jfk import extraer_univ_jfk


def extrac_fac_y_univ():
    """Ejecuta la extracción de datos de la universidad J.F. Kennedy y de la
    Facultad Latinoamericana de Ciencias Sociales"""
    extraer_latinoam()
    extraer_univ_jfk()
