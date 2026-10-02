# 01. INEGI - DENUE (Directorio Estadístico Nacional de Unidades Económicas)

## Descripción de la Fuente
El **DENUE** es la base de datos geográfica oficial del INEGI que identifica y georreferencia todos los establecimientos comerciales, industriales y de servicios en territorio mexicano.

* **Institución:** Instituto Nacional de Estadística y Geografía (INEGI)
* **Cobertura temática:** Unidades económicas de comercio al por menor de alimentos y abarrotes (Canasta básica).
* **Entidad Federativa:** 31 - Yucatán
* **Municipio clave:** 050 - Mérida

## Códigos SCIAN relevantes para la Canasta Básica
* `461110`: Comercio al por menor en tiendas de abarrotes, ultramarinos y misceláneas.
* `462111`: Comercio al por menor en supermercados y minisúpers.
* `461121`: Comercio al por menor de carnes rojas (carnicerías).
* `461122`: Comercio al por menor de carne de aves (pollerías).
* `461160`: Comercio al por menor de tortillas de maíz y nixtamal.
* `461140`: Comercio al por menor de frutas y verduras frescas.

## Variables Principales en el Dataset
1. `id`: Identificador único de unidad económica en DENUE.
2. `clee`: Clave Estadística Empresarial.
3. `nom_estab`: Nombre comercial del establecimiento.
4. `raz_social`: Razón social legal.
5. `codigo_act`: Código del Sistema de Clasificación Industrial de América del Norte (SCIAN).
6. `nombre_act`: Descripción de la actividad económica.
7. `per_ocu`: Estrato de personal ocupado (ej. 0 a 5 personas, 6 a 10 personas, etc.).
8. `tipo_vial`, `nom_vial`, `numero_ext`, `asentamiento`: Dirección física en Mérida.
9. `cod_postal`: Código postal.
10. `latitud`, `longitud`: Coordenadas geográficas WGS84 para mapas y SIG.

## Archivos incluidos en esta carpeta:
* **Fuente A:** `denue_merida_alimentos_real.csv` (7,520 comercios reales de canasta básica en Mérida filtrados de los 146,384 del estado) y `denue_yucatan_oficial/` (paquete masivo estatal).
* **Fuente B (EXTRA 1):** `censos_economicos_saic_merida.csv` (Datos de los Censos Económicos de INEGI / SAIC con ingresos totales, remuneraciones y personal ocupado en el comercio de alimentos en Mérida).
* `fetch_denue_api.py`: Script para consultar la API oficial del DENUE con token.

