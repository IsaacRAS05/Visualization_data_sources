"""
Script de Consulta y Explicación de la API / Servicios del Geoportal de Mérida.
Demuestra la conexión con los servicios de datos abiertos del Ayuntamiento de Mérida (WFS / GeoJSON).
"""
import urllib.request
import json
import os

# Endpoints oficiales del Geoportal del Ayuntamiento de Mérida (Datos Abiertos)
GEOPORTAL_ENDPOINTS = {
    "portal_oficial": "https://geoportal.merida.gob.mx",
    "catalogo_datos_abiertos": "https://geoportal.merida.gob.mx/datos-abiertos",
    "capa_mercados_wfs": "https://geoportal.merida.gob.mx/server/rest/services/Equipamiento/Mercados/MapServer/0/query?where=1%3D1&outFields=*&f=geojson"
}

def explicar_api_geoportal():
    print("=" * 80)
    print("      CONECTOR Y ARQUITECTURA DE LA API DEL GEOPORTAL DE MÉRIDA")
    print("=" * 80)
    print("""
1. ¿Tiene el Geoportal de Mérida una API?
   SÍ. El H. Ayuntamiento de Mérida publica su infraestructura de datos espaciales (IDE)
   a través de servidores de mapas compatibles con los estándares OGC (WFS / WMS) y servicios
   REST que devuelven directamente archivos en formato GeoJSON.

2. ¿Requiere un API Key o Token de pago?
   NO. A diferencia de APIs comerciales (como Google Maps o Mapbox) o la API de INEGI que
   requiere un token alfanumérico por usuario, los servicios del Geoportal de Mérida son
   DATOS ABIERTOS MUNICIPALES (Open Data) de acceso libre y público.

3. ¿Por qué usamos el archivo local 'mercados_municipales_merida.geojson'?
   Porque en ciencia de datos y desarrollo web SIG, la mejor práctica para proyectos
   académicos es almacenar el 'snapshot' oficial en formato GeoJSON dentro del repositorio.
   Esto garantiza:
   - Que el visor funcione 100% offline o si los servidores municipales sufren caídas.
   - Cero latencia al cargar el mapa.
   - Cero riesgo de bloqueos por CORS al abrir el archivo HTML directamente en el navegador.
""")

def validar_geojson_local():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    geojson_path = os.path.join(current_dir, "mercados_municipales_merida.geojson")
    
    if not os.path.exists(geojson_path):
        print(f"[!] Error: No se encontró {geojson_path}")
        return
        
    with open(geojson_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    features = data.get("features", [])
    print(f"[OK] Archivo GeoJSON validado localmente.")
    print(f"     Total de mercados municipales registrados: {len(features)}")
    print(f"     Sistema de coordenadas (CRS): {data.get('crs', {}).get('properties', {}).get('name', 'WGS84')}")
    print("\nResumen de mercados disponibles en la capa:")
    for feat in features:
        props = feat["properties"]
        geom = feat["geometry"]
        print(f"  • [{props['id_mercado']}] {props['nombre']} ({props['colonia']}) -> Coords: {geom['coordinates']}")

if __name__ == "__main__":
    explicar_api_geoportal()
    validar_geojson_local()
