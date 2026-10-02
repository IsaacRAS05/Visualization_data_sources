"""
Script informativo y de consulta sobre los indicadores del SIEGY - Yucatan
"""
import pandas as pd

def mostrar_resumen_siegy():
    df = pd.read_csv("indicadores_socioeconomicos_merida_siegy.csv")
    print("=== Indicadores Socioeconomicos y Alimentarios (Mérida y Yucatán) ===")
    print(df[["nombre_municipio", "año_periodo", "salario_promedio_diario_imss_mxn", "pobreza_laboral_pct", "costo_canasta_alimentaria_urbana_mxn"]])
    
    merida = df[df["nombre_municipio"] == "Merida"].iloc[-1]
    canasta_diaria = merida['costo_canasta_alimentaria_urbana_mxn'] / 30.0
    dias_trabajo_canasta = merida['costo_canasta_alimentaria_urbana_mxn'] / merida['salario_promedio_diario_imss_mxn']
    
    print("\n--- Analisis de Poder Adquisitivo en Merida ---")
    print(f"Costo mensual canasta alimentaria urbana: ${merida['costo_canasta_alimentaria_urbana_mxn']:.2f} MXN")
    print(f"Salario diario promedio IMSS: ${merida['salario_promedio_diario_imss_mxn']:.2f} MXN/dia")
    print(f"Dias de salario promedio necesarios para cubrir 1 canasta individual: {dias_trabajo_canasta:.1f} dias")

if __name__ == "__main__":
    mostrar_resumen_siegy()
