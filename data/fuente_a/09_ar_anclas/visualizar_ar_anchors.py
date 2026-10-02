"""
Script de validacion y despliegue de Anclas Geoespaciales para Realidad Aumentada (AR).
"""
import json
import pandas as pd
import os

def inspeccionar_anclas_ar():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    geojson_path = os.path.join(current_dir, "spatial_anchors_merida.geojson")
    with open(geojson_path, "r", encoding="utf-8") as f:
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
            "Semáforo": ui["semaforo_precios"],
            "Gasto_Semanal": ui["costo_canasta_promedio_semanal"],
            "Ahorro": ui["ahorro_vs_supermercado_pct"]
        })
        
    df = pd.DataFrame(filas)
    print("=== Anclas Geoespaciales de Realidad Aumentada (AR Core / WebXR Mérida) ===")
    print(df.to_string(index=False))
    print(f"\n[INFO] Para probar la experiencia WebXR / AR inmersiva en tu navegador:")
    print(f"       -> {os.path.join(current_dir, 'visor_ar_web.html')}")

if __name__ == "__main__":
    inspeccionar_anclas_ar()
