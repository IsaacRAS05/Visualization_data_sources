# 06. Web Scraping de Precios de Canasta Básica en Mérida

## Descripción de la Técnica
El **Web Scraping** es la técnica de extracción automatizada de datos no estructurados o semiestructurados de sitios web públicos. En este proyecto se utiliza para capturar los precios en línea vigentes de artículos de primera necesidad en tiendas de autoservicio y abarroteras presentes en Mérida (ej. Súper Akí, Chedraui, Dunosusa).

* **Propósito:** Seguimiento de inflación de alta frecuencia (monitoreo diario/semanal).
* **Herramientas:** Python (`requests`, `BeautifulSoup4`, `pandas`).
* **Aspectos Éticos y Técnicos:**
  * Respeto a las directivas de `robots.txt`.
  * Pausas de cortesía (`time.sleep`) entre peticiones para no saturar servidores.
  * Extracción con `User-Agent` descriptivo y con fines estrictamente académicos.

## Variables Generadas por el Scraper
1. `fecha_scraping`: Timestamp de la captura (Año-Mes-Día Hora).
2. `fuente_tienda`: Cadena comercial (ej. Súper Akí Mérida / Dunosusa / Chedraui).
3. `categoria`: Categoría del producto (Granos, Lácteos, Carnes, Aceites, Abarrotes).
4. `producto_nombre`: Nombre descriptivo completo del artículo.
5. `presentacion`: Contenido neto o gramaje.
6. `precio_regular_mxn`: Precio estándar de lista.
7. `precio_oferta_mxn`: Precio promocional o con descuento.
8. `en_stock`: Booleano o indicador de disponibilidad.
9. `url_producto`: Enlace de origen del producto.

## Archivos en esta carpeta:
* **Fuente A:** `precios_canasta_scraping.csv` (Monitoreo automatizado de 18 alimentos esenciales en autoservicios locales de Mérida: Súper Akí, Chedraui, Dunosusa).
* **Fuente B (EXTRA 1):** `precios_farmacias_conveniencia_merida.csv` (Monitoreo de canasta complementaria de higiene, salud e infancia en Farmacias Guadalajara, Similares y tiendas OXXO de Mérida).
* `scraper_canasta_merida.py`: Script para autoservicios.
* `scraper_farmacias_conveniencia_merida.py`: Script para farmacias y conveniencia.

