"""
Script para procesamiento y analisis de nube de puntos LiDAR en el Mercado Lucas de Galvez de Merida.
"""
import pandas as pd

def procesar_nube_puntos():
    df = pd.read_csv("lidar_mercado_merida_sample.csv")
    print("=== Analisis de Nube de Puntos LiDAR (Centro de Merida) ===")
    print(f"Total de retornos LiDAR registrados: {len(df)}")
    
    print("\n--- Desglose por Clasificacion ASPRS ---")
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
    
    print("\n--- Metricas Estructurales del Mercado ---")
    print(f"Elevacion promedio del terreno (cota base): {cota_terreno_prom:.2f} m s.n.m.")
    print(f"Cota maxima de techumbre (Domo central): {cota_edificio_max:.2f} m s.n.m.")
    print(f"Altura estructural neta calculada del mercado: {altura_edificio_mercado:.2f} metros")

if __name__ == "__main__":
    procesar_nube_puntos()
