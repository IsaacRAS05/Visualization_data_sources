"""
Script para explorar catalogos abiertos del portal datos.gob.mx
"""
import requests
import json
import pandas as pd

def listar_recursos_precios():
    url = "https://datos.gob.mx/busca/api/3/action/package_search"
    params = {
        "q": "precios canasta profeco",
        "rows": 5
    }
    headers = {"User-Agent": "Mozilla/5.0"}
    print("Consultando catalogo de datos.gob.mx...")
    try:
        r = requests.get(url, params=params, headers=headers, timeout=12)
        if r.status_code == 200:
            res = r.json()
            results = res.get("result", {}).get("results", [])
            print(f"Paquetes encontrados: {len(results)}")
            for p in results:
                print(f"- Titulo: {p.get('title')}")
                for res_item in p.get("resources", [])[:2]:
                    print(f"  * Archivo: {res_item.get('name')} -> {res_item.get('url')}")
        else:
            print(f"Estado HTTP {r.status_code}. El portal suele actualizar su endpoint CKAN.")
    except Exception as e:
        print("Error de conexion:", e)

if __name__ == "__main__":
    listar_recursos_precios()
