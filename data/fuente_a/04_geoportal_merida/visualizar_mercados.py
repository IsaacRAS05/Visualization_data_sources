"""
Script para leer y analizar la capa GeoJSON de mercados municipales de Mérida.
"""
import json
import pandas as pd

def listar_mercados():
    with open("mercados_municipales_merida.geojson", "r", encoding="utf-8") as f:
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
    print("=== Mercados Municipales de Mérida (Geoportal) ===")
    print(df.to_string(index=False))
    return df

if __name__ == "__main__":
    listar_mercados()
