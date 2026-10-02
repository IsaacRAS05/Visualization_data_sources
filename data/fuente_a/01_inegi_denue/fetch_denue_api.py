"""
Script para consultar la API oficial del DENUE de INEGI.
Documentacion: https://www.inegi.org.mx/servicios/api_denue.html
"""
import requests
import json
import pandas as pd

# Sustituye con tu token generado en inegi.org.mx/servicios/api_indicadores.html
INEGI_TOKEN = "AQUI_TU_TOKEN_INEGI"

def buscar_comercios_merida(termino="supermercado", lat=20.967370, lon=-89.592586, distancia_metros=3000):
    """
    Busca establecimientos comerciales alrededor de unas coordenadas en Merida.
    """
    url = f"https://www.inegi.org.mx/app/api/denue/v1/consulta/Buscar/{termino}/{lat},{lon}/{distancia_metros}/{INEGI_TOKEN}"
    print(f"Consultando API DENUE para: '{termino}'...")
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        if response.status_code == 200:
            datos = response.json()
            if isinstance(datos, list):
                df = pd.DataFrame(datos)
                print(f"Se encontraron {len(df)} establecimientos.")
                df.to_csv("denue_api_resultados.csv", index=False, encoding="utf-8-sig")
                print("Guardado en 'denue_api_resultados.csv'")
                return df
            else:
                print("Respuesta de INEGI:", datos)
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print("Error de conexion:", e)

if __name__ == "__main__":
    print("Para usar este script, registra tu token gratuito en el portal de INEGI.")
    # buscar_comercios_merida("abarrotes")
