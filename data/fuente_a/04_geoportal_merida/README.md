# 04. Geoportal Mérida (Ayuntamiento de Mérida)

## Descripción de la Fuente
El **Geoportal del Ayuntamiento de Mérida** (`geoportal.merida.gob.mx`) es el Sistema de Información Geográfica (SIG) oficial del municipio de Mérida. Contiene las capas cartográficas de zonificación urbana, equipamiento público, vialidades y centros de abasto municipal.

* **Institución:** H. Ayuntamiento de Mérida / Dirección de Desarrollo Urbano / Subdirección de Tecnologías de la Información.
* **Portal:** `geoportal.merida.gob.mx`
* **Sistema de Coordenadas de Referencia:** WGS 84 (EPSG:4326) / UTM Zona 16 Norte (EPSG:32616).

## Capas Clave para el Abasto y Comercio
1. **Mercados Públicos Municipales:** Puntos nodales de abasto de canasta básica tradicional a menor costo.
2. **Tianguis y Comercio en Vía Pública:** Polígonos autorizados para comercio popular semanal.
3. **Equipamiento Comercial y de Servicios:** Centros comerciales, supermercados y bodegas de abasto.
4. **Límites de Cuadrantes y Colonias:** Delimitación territorial de las más de 400 colonias y fraccionamientos de Mérida.

## Archivos en esta carpeta:
* **Fuente A:** `mercados_municipales_merida.geojson` (Capa vectorial de los 8 mercados públicos municipales permanentes).
* **Fuente B (EXTRA 1):** `tianguis_comercio_via_publica_merida.geojson` (Capa de tianguis sobre ruedas autorizados por la Subdirección de Mercados en colonias de Mérida con días y horarios de operación).
* `visualizar_mercados.py`: Script para procesar y listar las características de la capa geoespacial.

