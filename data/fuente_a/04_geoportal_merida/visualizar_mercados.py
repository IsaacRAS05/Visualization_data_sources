"""
Script para leer y analizar la capa GeoJSON de mercados municipales de Mérida.
"""
import json
import pandas as pd
import os

def listar_mercados():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    geojson_path = os.path.join(current_dir, "mercados_municipales_merida.geojson")
    with open(geojson_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    filas = []
    for feat in data["features"]:
        props = feat["properties"]
        geom = feat["geometry"]
        filas.append({
            "id": props["id_mercado"],
            "nombre": props["nombre"],
            "colonia": props["colonia"],
            "locales": props["locales_activos"],
            "afluencia_diaria": props["afluencia_diaria_estimada"],
            "nivel_precios": props["nivel_precios"],
            "longitud": geom["coordinates"][0],
            "latitud": geom["coordinates"][1]
        })
    
    df = pd.DataFrame(filas)
    print("=== Mercados Municipales de Mérida (Geoportal Oficial) ===")
    print(df.to_string(index=False))
    print(f"\n[INFO] Para explorar el mapa interactivo con isocronas de caminabilidad:")
    print(f"       -> {os.path.join(current_dir, 'visor_mercados_municipales.html')}")
    return df

if __name__ == "__main__":
    listar_mercados()
