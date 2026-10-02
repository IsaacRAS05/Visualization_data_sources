"""
Script de analisis estadistico descriptivo sobre los datos de campo generados (Self-Produced).
"""
import pandas as pd

def analizar_resultados():
    df = pd.read_csv("encuesta_campo_merida_piloto.csv")
    print("=== Resumen de Encuesta de Campo en Merida ===")
    print(f"Total de cuestionarios capturados: {len(df)}")
    
    gasto_prom = df["gasto_semanal_alimentos_mxn"].mean()
    gasto_med = df["gasto_semanal_alimentos_mxn"].median()
    print(f"\nGasto semanal promedio en alimentos: ${gasto_prom:.2f} MXN")
    print(f"Mediana del gasto semanal: ${gasto_med:.2f} MXN")
    
    print("\n--- Gasto Semanal Promedio por Zona de Mérida ---")
    gasto_zona = df.groupby("zona_merida")["gasto_semanal_alimentos_mxn"].agg(["count", "mean", "min", "max"])
    print(gasto_zona.round(2))
    
    print("\n--- Lugares Principales de Compra ---")
    print(df["lugar_compra_principal"].value_counts(normalize=True).mul(100).round(1).astype(str) + " %")
    
    print("\n--- Percepcion del Salario Minimo ---")
    print(df["percepcion_salario_minimo"].value_counts(normalize=True).mul(100).round(1).astype(str) + " %")

if __name__ == "__main__":
    analizar_resultados()
