"""
Script de validacion y despliegue de Anclas Geoespaciales para Realidad Aumentada (AR).
"""
import json
import pandas as pd

def inspeccionar_anclas_ar():
    with open("spatial_anchors_merida.geojson", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    filas = []
    for feat in data["features"]:
        props = feat["properties"]
        geom = feat["geometry"]
        ui = props["tarjeta_ar_ui"]
        filas.append({
            "ID_Ancla": props["anchor_id"],
            "Lugar": props["lugar"],
            "Tipo_Ancla": props["tipo_ancla"],
            "Longitud": geom["coordinates"][0],
            "Latitud": geom["coordinates"][1],
            "Altitud_m": geom["coordinates"][2],
            "Semaforo_Precio": ui["semaforo_precios"],
            "Gasto_Semanal": ui["costo_canasta_promedio_semanal"],
            "Ahorro_Estimado": ui["ahorro_vs_supermercado_pct"],
            "Asset_3D": props["asset_3d_uri"]
        })
        
    df = pd.DataFrame(filas)
    print("=== Anclas Geoespaciales de Realidad Aumentada (AR Core / WebXR) ===")
    print(df.to_string(index=False))

if __name__ == "__main__":
    inspeccionar_anclas_ar()
