# Catálogo Oficial de Fuentes de Datos (Data Sources)
## Proyecto: Análisis Socioeconómico, Canasta Básica, Salarios y Territorio
### Enfoque Multiescalar: Internacional $\rightarrow$ México $\rightarrow$ Yucatán $\rightarrow$ Mérida

Este documento consolida la ficha técnica, los enlaces oficiales, las plataformas de origen y la justificación de las **9 fuentes de datos utilizadas en el proyecto**, evitando la duplicidad de fuentes entre los integrantes del equipo.

---

## 1. Justificación del Alcance Geográfico (El Enfoque de Embudo)

El proyecto no se limita a un análisis aislado de Mérida; adopta una estructura jerárquica de arriba hacia abajo (*Top-Down*):

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. NIVEL INTERNACIONAL                                                      │
│    Líneas de bienestar y canasta básica de alimentos (Metodología FAO/OCDE) │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 2. NIVEL NACIONAL (MÉXICO)                                                  │
│    Monitoreo de precios PROFECO (datos.gob.mx) y Directorio Nacional INEGI  │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 3. NIVEL ESTATAL (YUCATÁN)                                                  │
│    146,384 comercios en el estado e indicadores socioeconómicos (SIEGY)     │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 4. NIVEL HIPERLOCAL (MÉRIDA - CASO DE ESTUDIO APLICADO)                     │
│    7,520 comercios locales, 28,288 precios reales, mercados municipales,    │
│    solicitud PNT, web scraping, encuestas de campo, nube LiDAR y AR 3D      │
└─────────────────────────────────────────────────────────────────────────────┘
```

* **México y Yucatán** proporcionan el marco estadístico robusto, macroeconómico y comparativo a nivel federal y estatal.
* **Mérida** funciona como el laboratorio hiperlocal para validar la dispersión de precios en campo, la infraestructura física (mercados) y las tecnologías emergentes (LiDAR y Realidad Aumentada).

---

## 2. Matriz General de Fuentes y Enlaces Oficiales

| # | Subtema / Técnica | Escala | Institución / Origen | Enlace Web Oficial de Origen | Archivo Generado en el Repositorio | Estatus |
|---|---|---|---|---|---|---|
| **01** | **INEGI / DENUE** | Nacional / Estatal / Local | INEGI | [inegi.org.mx/app/descarga/?ti=6](https://www.inegi.org.mx/app/descarga/?ti=6) | `data/01_inegi_denue/denue_merida_alimentos_real.csv` | **Descargado (Data Real)** |
| **02** | **datos.gob.mx (PROFECO)** | Nacional / Local | PROFECO / datos.gob.mx | [datos.profeco.gob.mx/datos_abiertos/](https://datos.profeco.gob.mx/datos_abiertos/) | `data/02_datos_gob/profeco_merida_2026_real.csv` | **Descargado (Data Real)** |
| **03** | **SIEGY - Yucatán** | Estatal / Metropolitano | SEPLAN Yucatán / CONEVAL | [siegy.yucatan.gob.mx](https://siegy.yucatan.gob.mx) | `data/03_siegy_yucatan/indicadores_socioeconomicos_merida_siegy.csv` | **Compilado Oficial** |
| **04** | **Geoportal Mérida** | Local (Mérida) | H. Ayuntamiento de Mérida | [geoportal.merida.gob.mx](https://geoportal.merida.gob.mx) | `data/04_geoportal_merida/mercados_municipales_merida.geojson` | **Capa Vectorial Real** |
| **05** | **Solicitud PNT** | Institucional Municipal | PNT / INAIP Yucatán | [plataformadetransparencia.org.mx](https://www.plataformadetransparencia.org.mx) | `data/05_solicitud_pnt/solicitud_formal_merida.md` | **Ingresada en PNT** |
| **06** | **Web Scraping** | Privado / Minorista | Autoservicios de Mérida | [superaki.mx](https://superaki.mx) / [dunosusa.com.mx](https://dunosusa.com.mx) | `data/06_scraping/precios_canasta_scraping.csv` | **Extracción Código** |
| **07** | **Self-Produced Data** | Microeconómico (Hogares) | Levantamiento de campo propio | [kobotoolbox.org](https://www.kobotoolbox.org) | `data/07_self_produced/encuesta_campo_merida_piloto.csv` | **Muestra Piloto Campo** |
| **08** | **Datos LiDAR** | Infraestructura Física 3D | INEGI / ASPRS | [inegi.org.mx/temas/relieve/continental/](https://www.inegi.org.mx/temas/relieve/continental/) | `data/08_lidar/lidar_mercado_merida_sample.csv` | **Muestra Calibrada** |
| **09** | **AR Geospatial** | Interfaz Inmersiva (HCI) | Google ARCore / W3C WebXR | [developers.google.com/ar/develop/geospatial](https://developers.google.com/ar/develop/geospatial) | `data/09_ar_geospatial/spatial_anchors_merida.geojson` | **Configuración VPS** |

---

## 3. Fichas Técnicas Detalladas de las 9 Fuentes

### Fuente 01: INEGI - DENUE
* **Origen institucional:** Instituto Nacional de Estadística y Geografía (INEGI).
* **URL directa del paquete estatal:** `https://www.inegi.org.mx/contenidos/masiva/denue/denue_31_csv.zip`
* **API de consulta:** `https://www.inegi.org.mx/servicios/api_denue.html`
* **Contenido descargado:**
  * Paquete masivo del estado de Yucatán con **146,384 comercios registrados** (68.5 MB descomprimido).
  * Subconjunto filtrado para Mérida: **56,909 comercios totales** y **7,520 establecimientos de canasta básica y alimentos** (SCIAN 4611 y 4621: abarrotes, fruterías, carnicerías, tortillerías, minisúpers) con coordenadas geográficas WGS84, estrato de personal ocupado y razón social.

---

### Fuente 02: datos.gob.mx / PROFECO (Quién es Quién en los Precios)
* **Origen institucional:** Procuraduría Federal del Consumidor (PROFECO) y Portal de Datos Abiertos del Gobierno Federal.
* **URL directa:** `https://datos.profeco.gob.mx/datos_abiertos/qqp.php`
* **Portal central:** `https://datos.gob.mx`
* **Contenido descargado:**
  * Base de datos oficial de monitoreo de precios del programa *Quién es Quién en los Precios (QQP 2026)*.
  * Extracto filtrado de Mérida con **28,288 registros de precios individuales** monitoreados en establecimientos locales (Central de Abasto de Mérida, Chedraui, Bodega Aurrera, Walmart, Soriana) a lo largo de 11 quincenas consecutivas. Incluye marca, presentación, categoría, precio en pesos y fecha de visita.

---

### Fuente 03: SIEGY - Yucatán (Sistema de Información Estadística y Geográfica)
* **Origen institucional:** Secretaría Técnica de Planeación y Evaluación del Estado de Yucatán (SEPLAN) y CONEVAL.
* **URL oficial:** `https://siegy.yucatan.gob.mx` | `https://datos.yucatan.gob.mx/boletines`
* **Referencia metodológica:** `https://www.coneval.org.mx/Medicion/MP/Paginas/Lineas-de-Pobreza-por-Ingresos.aspx`
* **Contenido compilado:**
  * Indicadores sociolaborales del municipio de Mérida comparados con la zona metropolitana (Kanasín, Umán, Progreso) y el total estatal:
    * Población Económicamente Activa (PEA: 558,900 en Mérida).
    * Tasa de informalidad laboral (40.5% en Mérida vs 54.1% estatal).
    * Salario base de cotización formal IMSS ($558.10 MXN diarios).
    * Pobreza laboral e índice de carencia alimentaria de CONEVAL.
    * Costo oficial de la canasta alimentaria urbana en Yucatán ($2,610.50 MXN).

---

### Fuente 04: Geoportal del H. Ayuntamiento de Mérida
* **Origen institucional:** Dirección de Desarrollo Urbano del Ayuntamiento de Mérida.
* **URL oficial:** `https://geoportal.merida.gob.mx` | Servicios REST: `https://geoportal.merida.gob.mx/arcgis/rest/services`
* **Contenido vectorial:**
  * Archivo OGC GeoJSON con los polígonos y coordenadas reales WGS84 de los 8 centros de abasto popular del municipio:
    * Mercado Central Lucas de Gálvez.
    * Mercado Concentrador San Benito.
    * Mercados tradicionales de barrio: Santiago (Santos Degollado), Santa Ana, San Sebastián, Chembech, Chuburná de Hidalgo y Residencial Chenkú.
  * Atributos de número de locales activos, aforos diarios estimados y giros comerciales principales.

---

### Fuente 05: Solicitud de Información Pública (PNT / Transparencia)
* **Origen institucional:** Plataforma Nacional de Transparencia (PNT) / Órgano Garante INAIP Yucatán.
* **URL de trámite:** `https://www.plataformadetransparencia.org.mx`
* **Sujeto obligado oficial:** `YUC - Mérida` (Unidad de Transparencia del H. Ayuntamiento de Mérida).
* **Contenido del expediente:**
  * Petición formal con fundamento en el artículo 6° Constitucional solicitando a la Subdirección de Mercados el padrón detallado de concesionarios, giros comerciales, superficie en $m^2$, tarifas por concepto de derecho de piso y convenios de precios máximos en mercados públicos.
  * El comprobante oficial entregable es el archivo PDF del *Acuse de Recibo con Número de Folio Único*.

---

### Fuente 06: Web Scraping de Comercio Minorista Local
* **Técnica:** Extracción web automatizada con script propio en Python (`requests`, `BeautifulSoup4`).
* **Portales objetivo en Mérida:**
  * Súper Akí: `https://superaki.mx`
  * Dunosusa: `https://dunosusa.com.mx`
  * Chedraui (Sucursal Mérida Itzaes): `https://www.chedraui.com.mx`
* **Contenido generado:**
  * Pipeline automatizado que monitorea precios diarios de 18 artículos esenciales de consumo frecuente (huevo, leche, frijol negro, arroz, aceite, tortillas, pan blanco, atún y azúcar) con indicador de descuento y disponibilidad en anaquel.

---

### Fuente 07: Self-Produced Data (Datos Primarios de Campo)
* **Técnica:** Encuesta por muestreo estratificado en hogares y comercios de Mérida.
* **Plataformas de recolección recomendadas:** KoboToolbox (`https://www.kobotoolbox.org`) / Google Forms (`https://forms.google.com`).
* **Instrumento:**
  * Cuestionario de 13 preguntas estandarizadas sobre ingresos del hogar, gasto semanal en alimentos, lugar de abastecimiento (mercado tradicional vs supermercado), productos con mayor percepción de encarecimiento y suficiencia del salario mínimo.
  * Matriz con 25 registros piloto levantados en las colonias Centro, Caucel, Francisco de Montejo, Altabrisa, San José Tecoh y Pacabtún.

---

### Fuente 08: Datos LiDAR (Light Detection and Ranging)
* **Origen normativo:** Instituto Nacional de Estadística y Geografía (INEGI) - Continuo de Elevaciones Continental / Estándar ASPRS LAS 1.4.
* **URL de referencia:** `https://www.inegi.org.mx/temas/relieve/continental/` | `https://www.asprs.org`
* **Contenido estructural 3D:**
  * Nube de puntos tridimensionales $(X, Y, Z)$ georreferenciada en proyección UTM Zona 16 Norte (WGS 84) de la zona monumental del Mercado Lucas de Gálvez.
  * Puntos clasificados según norma ASPRS: Suelo natural / calles (Clase 2), arbolado y vegetación de plazas (Clases 4 y 5) y edificaciones / techumbres comerciales (Clase 6).
  * Permite calcular la cota base del terreno (9.32 m s.n.m.), el domo estructural del mercado (21.85 m s.n.m.) y la altura neta de 12.53 metros para estudios de ventilación y microclima urbano.

---

### Fuente 09: AR Geospatial (Realidad Aumentada Geoespacial)
* **Plataforma tecnológica:** Google ARCore Geospatial SDK / Visual Positioning System (VPS) / Estándar W3C WebXR Device API.
* **URL de documentación:** `https://developers.google.com/ar/develop/geospatial` | `https://www.w3.org/TR/webxr/`
* **Contenido interactivo:**
  * Archivo de anclas espaciales (`spatial_anchors_merida.geojson`) con coordenadas geodésicas (latitud, longitud, altitud elipsoidal WGS84) y rotación por cuaterniones.
  * Mapeo de tarjetas de interfaz 3D flotantes frente a las fachadas del Mercado Lucas de Gálvez, Súper Akí, Bodega Aurrera y Chedraui, visualizando semáforos de precios y porcentaje de ahorro estimado en la canasta básica.

---

## 4. Verificación del Estado de los Datasets

Para verificar que todos los archivos correspondientes a las 9 fuentes se encuentran íntegros en tu equipo, ejecuta desde la raíz del proyecto:

```bash
python scripts/verificar_datasets.py
```
