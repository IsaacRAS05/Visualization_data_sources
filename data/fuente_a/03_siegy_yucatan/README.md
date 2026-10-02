# 03. SIEGY - Sistema de Información Estadística y Geográfica de Yucatán

## Descripción de la Fuente
El **SIEGY** es la plataforma oficial coordinada por la Secretaría Técnica de Planeación y Evaluación (**SEPLAN**) del Gobierno del Estado de Yucatán. Consolida datos sobre dinámica poblacional, mercado laboral, pobreza multidimensional, carencia alimentaria y desarrollo económico de los 106 municipios del estado.

* **Institución:** Gobierno del Estado de Yucatán / SEPLAN / SIEGY
* **Portales oficiales:** `siegy.yucatan.gob.mx` y `datos.yucatan.gob.mx`
* **Ámbito geográfico:** Municipio de Mérida (Clave 050) y Zona Metropolitana (Kanasín, Umán, Conkal, Ucú).

## Indicadores Socioeconómicos Clave
1. **Población Económicamente Activa (PEA):** Volumen de población en edad de trabajar y ocupada.
2. **Salario Promedio de Cotización (IMSS):** Salario base de cotización formal reportado en Mérida.
3. **Pobreza Laboral e Ingreso Laboral:** Porcentaje de la población con ingreso laboral inferior al valor de la canasta alimentaria.
4. **Carencia por Acceso a la Alimentación Nutritiva y de Calidad:** Indicador multidimensional de CONEVAL / SIEGY.
5. **Índice de Marginación Urbana:** Grado de marginación por AGEB o sector territorial en Mérida.

## Archivos en esta carpeta:
* **Fuente A:** `indicadores_socioeconomicos_merida_siegy.csv` (Indicadores sociolaborales, PEA, Salario promedio IMSS y costo de la canasta alimentaria urbana de CONEVAL).
* **Fuente B (EXTRA 1):** `marginacion_urbana_colonias_merida.csv` (Índice de Marginación Urbana CONAPO / SIEGY por colonia en Mérida, contrastando el Norte vs Sur).
* `explorar_siegy.py`: Script con enlaces directos a boletines de empleo y tableros oficiales.

