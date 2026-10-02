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
* **Fuente A:** `mercados_municipales_merida.geojson` (Capa vectorial oficial de los 8 mercados públicos municipales permanentes).
* `visor_mercados_municipales.html`: Visor SIG interactivo en Leaflet con isocronas de caminabilidad de 10 min a pie (800m), conmutador de capas libres (OpenStreetMap, CartoDB, Esri) y sin necesidad de API Key.
* `consultar_geoportal_api.py`: Script para consultar la API y endpoints de datos abiertos (WFS / GeoJSON) del Ayuntamiento de Mérida.
* `visualizar_mercados.py`: Script para procesar y listar las características de la capa geoespacial.

---

## 🌐 ¿Cómo funciona la API del Geoportal de Mérida?
* El Ayuntamiento de Mérida expone su infraestructura de datos espaciales (IDE) mediante servicios **WFS (Web Feature Service)** y endpoints REST que devuelven directamente archivos en formato estándar **GeoJSON**.
* **¿Requiere API Key o Token de pago?** **No.** Son datos abiertos municipales de acceso público y gratuito.
* En este repositorio almacenamos la copia oficial en `mercados_municipales_merida.geojson` para garantizar funcionamiento 100% offline, sin restricciones de CORS y con máxima velocidad al abrir el visor.

