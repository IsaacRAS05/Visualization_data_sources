"""
Script maestro de diagnostico y resumen de los 18 datasets disponibles (Fuente A + Fuente B).
Organizado por estructura: data/fuente_a/ y data/fuente_b/
"""
import os
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")

FUENTES = [
    # FUENTE A
    {"num": "01-A", "grupo": "Fuente A", "tema": "INEGI / DENUE", "folder": "fuente_a/01_inegi_denue", "archivo": "denue_merida_alimentos_real.csv", "tipo": "CSV Oficial INEGI", "desc": "7,520 comercios de canasta básica en Mérida"},
    {"num": "02-A", "grupo": "Fuente A", "tema": "datos.gob / PROFECO", "folder": "fuente_a/02_datos_gob_profeco", "archivo": "profeco_merida_2026_real.csv", "tipo": "CSV Oficial PROFECO", "desc": "28,288 precios reales en Mérida (QQP 2026)"},
    {"num": "03-A", "grupo": "Fuente A", "tema": "SIEGY Yucatán", "folder": "fuente_a/03_siegy_yucatan", "archivo": "indicadores_socioeconomicos_merida_siegy.csv", "tipo": "CSV Socioeconómico", "desc": "PEA, Salario IMSS y Canasta Urbana CONEVAL"},
    {"num": "04-A", "grupo": "Fuente A", "tema": "Geoportal Mérida", "folder": "fuente_a/04_geoportal_merida", "archivo": "mercados_municipales_merida.geojson", "tipo": "GeoJSON SIG", "desc": "8 mercados públicos municipales permanentes"},
    {"num": "05-A", "grupo": "Fuente A", "tema": "Solicitud PNT", "folder": "fuente_a/05_solicitud_pnt", "archivo": "solicitud_formal_merida.md", "tipo": "Trámite PNT", "desc": "Solicitud ingresada a Ayto. Mérida sobre padrón locatarios"},
    {"num": "06-A", "grupo": "Fuente A", "tema": "Web Scraping", "folder": "fuente_a/06_scraping_autoservicios", "archivo": "precios_canasta_scraping.csv", "tipo": "CSV Python Scraper", "desc": "18 alimentos en autoservicios (Súper Akí, Chedraui, Dunosusa)"},
    {"num": "07-A", "grupo": "Fuente A", "tema": "Self-Produced", "folder": "fuente_a/07_encuesta_hogares", "archivo": "encuesta_campo_merida_piloto.csv", "tipo": "CSV Encuesta", "desc": "25 encuestas de hogares en colonias de Mérida"},
    {"num": "08-A", "grupo": "Fuente A", "tema": "LiDAR 3D", "folder": "fuente_a/08_lidar_mercado", "archivo": "lidar_mercado_merida_sample.csv", "tipo": "CSV Nube 3D ASPRS", "desc": "Puntos clasificados techumbre/terreno Mercado Lucas de Gálvez"},
    {"num": "09-A", "grupo": "Fuente A", "tema": "AR Geospatial", "folder": "fuente_a/09_ar_anclas", "archivo": "spatial_anchors_merida.geojson", "tipo": "GeoJSON VPS", "desc": "4 anclas espaciales con semáforos de precios 3D en fachadas"},

    # FUENTE B
    {"num": "01-B", "grupo": "Fuente B", "tema": "INEGI / SAIC", "folder": "fuente_b/01_inegi_saic", "archivo": "censos_economicos_saic_merida.csv", "tipo": "CSV Censos INEGI", "desc": "Ingresos y personal ocupado en alimentos Mérida/Yucatán"},
    {"num": "02-B", "grupo": "Fuente B", "tema": "datos.gob / SNIIM", "folder": "fuente_b/02_datos_gob_sniim", "archivo": "sniim_mayoreo_central_abasto_merida.csv", "tipo": "CSV Mayorista SNIIM", "desc": "Precios mayoreo en Central de Abasto de Mérida"},
    {"num": "03-B", "grupo": "Fuente B", "tema": "SIEGY / CONAPO", "folder": "fuente_b/03_conapo_marginacion", "archivo": "marginacion_urbana_colonias_merida.csv", "tipo": "CSV Marginación", "desc": "Índice de marginación por colonia en Mérida (Norte vs Sur)"},
    {"num": "04-B", "grupo": "Fuente B", "tema": "Geoportal Mérida", "folder": "fuente_b/04_tianguis_geoportal", "archivo": "tianguis_comercio_via_publica_merida.geojson", "tipo": "GeoJSON SIG", "desc": "Tianguis sobre ruedas autorizados en colonias de Mérida"},
    {"num": "05-B", "grupo": "Fuente B", "tema": "Solicitud PNT", "folder": "fuente_b/05_solicitud_central_abasto", "archivo": "solicitud_pnt_central_abasto_merida.md", "tipo": "Trámite PNT", "desc": "Solicitud formal a Central de Abasto Mérida (toneladas/pesaje)"},
    {"num": "06-B", "grupo": "Fuente B", "tema": "Web Scraping", "folder": "fuente_b/06_scraping_farmacias", "archivo": "precios_farmacias_conveniencia_merida.csv", "tipo": "CSV Python Scraper", "desc": "Canasta complementaria en Farmacias Guadalajara y OXXO"},
    {"num": "07-B", "grupo": "Fuente B", "tema": "Self-Produced", "folder": "fuente_b/07_bitacora_tienditas", "archivo": "bitacora_precios_tienditas.csv", "tipo": "CSV Auditoría", "desc": "Auditoría de precios en 5 tienditas de esquina de Mérida"},
    {"num": "08-B", "grupo": "Fuente B", "tema": "LiDAR / CEM", "folder": "fuente_b/08_lidar_cem_mde", "archivo": "inegi_cem_mde_merida_grid.csv", "tipo": "CSV Malla MDE", "desc": "Malla CEM 3.0 INEGI Mérida con pendientes y encharcamientos"},
    {"num": "09-B", "grupo": "Fuente B", "tema": "AR Geospatial", "folder": "fuente_b/09_ar_modelos_3d", "archivo": "catalogo_modelos_3d_canasta.json", "tipo": "JSON Catálogo 3D", "desc": "Modelos 3D glTF/GLB de alimentos y tarjetas HUD holográficas"},

    # FUENTE C
    {"num": "01-C", "grupo": "Fuente C", "tema": "INEGI / ENOE", "folder": "fuente_c/01_enoe_microdatos", "archivo": "0_indice_tablas_enoe_2025_1t.csv", "tipo": "Microdatos INEGI", "desc": "Microdatos ENOE 2025 1T Hogares/Viviendas y 45 catálogos"},
    {"num": "02-C", "grupo": "Fuente C", "tema": "SEGALMEX / DICONSA", "folder": "fuente_c/02_diconsa_segalmex", "archivo": "DICONSA_8_Listado_de_articulos_por_proveedor.csv", "tipo": "CSV Oficial DICONSA", "desc": "4,064 artículos canasta básica y proveedores Diconsa"},
    {"num": "03-C", "grupo": "Fuente C", "tema": "Inspección / Sanidad", "folder": "fuente_c/03_imss_boletin", "archivo": "01_actividades-inspeccion-movilizacion_2dotrim2025.csv", "tipo": "CSV Inspección", "desc": "Inspección fitozoosanitaria y movilización agropecuaria"},
    {"num": "04-C", "grupo": "Fuente C", "tema": "Movilidad / Va y Ven", "folder": "fuente_c/04_transporte_vayven", "archivo": "export.geojson", "tipo": "GeoJSON Rutas", "desc": "565 rutas y paraderos de transporte Va y Ven al Centro"},
    {"num": "05-C", "grupo": "Fuente C", "tema": "Transparencia / Salud", "folder": "fuente_c/05_solicitud_salubridad", "archivo": "remuneraciones_trim02_2026.csv", "tipo": "CSV Sueldos PNT", "desc": "Tabulador de remuneraciones brutas y netas sector salud"},
    {"num": "06-C", "grupo": "Fuente C", "tema": "Scraping Apps Delivery", "folder": "fuente_c/06_scraping_delivery", "archivo": "comparativa_precios_canasta_basica.csv", "tipo": "CSV Comparativa", "desc": "2,501 registros de sobreprecio delivery vs tienda física"},
    {"num": "07-C", "grupo": "Fuente C", "tema": "Entrevistas Locatarios", "folder": "fuente_c/07_entrevistas_mercado", "archivo": "entrevistas_locatarios_mercado.csv", "tipo": "CSV Entrevistas", "desc": "Entrevistas estructuradas a locatarios de Lucas de Gálvez"},
    {"num": "08-C", "grupo": "Fuente C", "tema": "OpenTopography / Radar", "folder": "fuente_c/08_opentopography", "archivo": "topografia_srtm_nasadem_merida_vs_montanas.csv", "tipo": "CSV Topográfico", "desc": "2,401 puntos de cota SRTM/NASADEM Mérida vs montañas"},
    {"num": "09-C", "grupo": "Fuente C", "tema": "Waypoints AR Lucas Gálvez", "folder": "fuente_c/09_ar_waypoints", "archivo": "ruta_ar_lucas_galvez.json", "tipo": "JSON Navegación AR", "desc": "Ruta de guiado peatonal AR hacia pasillo económico"}
]

def verificar_todo():
    resumen = []
    for f in FUENTES:
        ruta_archivo = os.path.join(DATA_DIR, f["folder"], f["archivo"])
        existe = os.path.exists(ruta_archivo)
        tamaño_kb = round(os.path.getsize(ruta_archivo) / 1024, 1) if existe else 0
        
        resumen.append({
            "#": f["num"],
            "Grupo": f["grupo"],
            "Tema": f["tema"],
            "Archivo": f["archivo"],
            "Formato": f["tipo"],
            "Estatus": "Listo" if existe else "Faltante",
            "Tamaño": f"{tamaño_kb} KB" if existe else "-",
            "Descripción": f["desc"]
        })

    df_res = pd.DataFrame(resumen)
    print("=" * 135)
    print("                     ESTADO DE LOS 27 DATASETS DEL PROYECTO (FUENTES A, B Y C)")
    print("=" * 135)
    print(df_res.to_string(index=False))
    print("=" * 135)
    
    total = len(df_res)
    listos = sum(df_res["Estatus"] == "Listo")
    print(f"\nResumen: {listos} de {total} datasets listos y verificados en disco.")

if __name__ == "__main__":
    verificar_todo()
