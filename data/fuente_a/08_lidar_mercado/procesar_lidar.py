"""
Script para procesamiento y analisis de nube de puntos LiDAR en el Mercado Lucas de Galvez de Merida.
"""
import pandas as pd
import os

def procesar_nube_puntos():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "lidar_mercado_merida_sample.csv")
    df = pd.read_csv(csv_path)
    print("=== Análisis de Nube de Puntos LiDAR (Centro de Mérida) ===")
    print(f"Total de retornos LiDAR registrados: {len(df)}")
    
    print("\n--- Desglose por Clasificación ASPRS ---")
    conteo_clases = df.groupby(["classification_code", "classification_label"]).agg(
        num_puntos=("point_id", "count"),
        cota_z_min=("elevation_z", "min"),
        cota_z_max=("elevation_z", "max"),
        cota_z_prom=("elevation_z", "mean"),
        intensidad_prom=("intensity", "mean")
    )
    print(conteo_clases.round(2))
    
    cota_terreno_prom = df[df["classification_code"] == 2]["elevation_z"].mean()
    cota_edificio_max = df[df["classification_code"] == 6]["elevation_z"].max()
    altura_edificio_mercado = cota_edificio_max - cota_terreno_prom
    
    print("\n--- Métricas Estructurales del Mercado ---")
    print(f"Elevación promedio del terreno (cota base): {cota_terreno_prom:.2f} m s.n.m.")
    print(f"Cota máxima de techumbre (Domo central): {cota_edificio_max:.2f} m s.n.m.")
    print(f"Altura estructural neta calculada del mercado: {altura_edificio_mercado:.2f} metros")
    print(f"\n[INFO] Para interactuar en 3D con la nube de puntos, abre en tu navegador:")
    print(f"       -> {os.path.join(current_dir, 'visor_3d_mercado.html')}")

if __name__ == "__main__":
    procesar_nube_puntos()
