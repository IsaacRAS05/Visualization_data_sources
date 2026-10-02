# Guía Maestra del Proyecto: Título, Subtemas y 27 Fuentes de Datos

## Proyecto: Análisis Multiescalar del Salario, la Canasta Básica y el Territorio

### Enfoque de Embudo: Internacional $\rightarrow$ México $\rightarrow$ Yucatán $\rightarrow$ Mérida

Este documento es la **guía oficial para el equipo**. Explica el título elegido, los 9 subtemas redactados de forma clara y la **matriz completa de 27 fuentes de datos** (la fuente que ya tenemos lista + **2 fuentes extra por categoría** para que cada integrante pueda aportar las 18 restantes sin repetir información).

---

## 1. El Título del Proyecto

### 🏆 Título Oficial:

> **"Del Mundo a la Esquina: ¿Cuánto Cuesta Comer?"**

## ¿Por qué elegimos este título?

1. **Es *catchy* y humano:** Le da la vuelta al dicho clásico *"trabajar para comer o comer para trabajar"*. Plantea una postura positiva: el objetivo del trabajo no es la simple supervivencia biológica, sino el bienestar y la dignidad.
3. **Es multiescalar:** El subtítulo aclara que no es un proyecto cerrado solo a Mérida; toma como base los estándares internacionales y nacionales, y usa a Mérida como el laboratorio de validación en la calle.

---

## 2. Los 9 Subtemas del Proyecto (En palabras claras y sencillas)

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        ESTRUCTURA DEL PROYECTO                         │
├────────────────────────────────────────────────────────────────────────┤
│  MÓDULO 1: LA REALIDAD ECONÓMICA (¿Dónde compramos y cuánto ganamos?)  │
│    1. El Mapa del Comercio: Dónde están las tiendas y supermercados    │
│    2. El Costo de la Comida: Cómo cambian los precios en la ciudad     │
│    3. Sueldo vs. Canasta Básica: ¿Para qué alcanza el salario hoy?     │
│                                                                        │
│  MÓDULO 2: LOS MERCADOS PÚBLICOS Y EL GOBIERNO                         │
│    4. Mercados Tradicionales: La opción de abasto más popular          │
│    5. Transparencia Municipal: Cuánto pagan y cómo operan los locales  │
│                                                                        │
│  MÓDULO 3: LEVANTAMIENTO DE DATOS EN LA ERA DIGITAL                    │
│    6. Rastreo Web: Extracción automática de precios en supermercados   │
│    7. La Voz de la Gente: Lo que las familias gastan cada semana       │
│                                                                        │
│  MÓDULO 4: TECNOLOGÍA VISUAL Y EL FUTURO DE LAS COMPRAS                │
│    8. Escaneo Láser en 3D: Conociendo la forma y altura del mercado    │
│    9. Realidad Aumentada: Ver precios y ahorros flotando en la calle   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Matriz Maestra: Las 27 Fuentes de Datos (3 por Categoría)

Para cumplir con el requerimiento del profesor (**3 fuentes por cada uno de los 9 tipos de datos = 27 fuentes en total**):

* ✅ **Fuente A (9 datasets):** Descargadas e integradas en el repositorio.
* ✅ **Fuente B (9 datasets):** **¡Recién generadas e integradas en el repositorio!** (18 fuentes listas en total).
* 📝 **Fuente C (9 datasets restantes):** Quedan asignadas como tareas específicas para que los integrantes del equipo las aporten según los enlaces y guías aquí descritas.

---

### MÓDULO 1: LA REALIDAD ECONÓMICA

#### 01. Tipo: INEGI / DENUE (Directorios y Censos de Empresas)

* **Fuente A (Ya en el repo):** `denue_merida_alimentos_real.csv`
  * *Origen:* [INEGI Descarga Masiva](https://www.inegi.org.mx/app/descarga/?ti=6). Paquete estatal de 146,384 comercios de Yucatán filtrado a los 7,520 negocios de canasta básica en Mérida.
* **Fuente B (EXTRA 1):** **Censos Económicos de INEGI (Sistema SAIC)**
  * *Qué buscar:* Ingresos totales, sueldos promedio pagados y personal ocupado en el comercio al por menor de alimentos en Mérida.
  * *Enlace directo:* [INEGI - Consulta Interactiva Censos Económicos](https://www.inegi.org.mx/programas/ce/) (Descargar tabulado en Excel/CSV).
* **Fuente C (EXTRA 2):** **ENOE (Encuesta Nacional de Ocupación y Empleo) - Microdatos INEGI**
  * *Qué buscar:* Niveles de ingreso por horas trabajadas y porcentaje de trabajadores sin prestaciones en Yucatán.
  * *Enlace directo:* [INEGI - Datos Abiertos ENOE](https://www.inegi.org.mx/programas/enoe/15ymas/) (Descargar tabulados trimestrales de ocupación).

---

#### 02. Tipo: datos.gob.mx (Datos Abiertos Federales / Precios)

* **Fuente A (Ya en el repo):** `profeco_merida_2026_real.csv`
  * *Origen:* [PROFECO Datos Abiertos](https://datos.profeco.gob.mx/datos_abiertos/qqp.php). 28,288 precios reales de alimentos en Mérida durante 2026.
* **Fuente B (EXTRA 1):** **SNIIM (Sistema Nacional de Información e Integración de Mercados) - Secretaría de Economía**
  * *Qué buscar:* Precios diarios de mayoreo y medio mayoreo de frutas, verduras, huevo y carne en la Central de Abasto de Mérida.
  * *Enlace directo:* [SNIIM - Mercados Agrícolas y Pecuarios](http://www.economia-sniim.gob.mx/) o vía [datos.gob.mx](https://datos.gob.mx).
* **Fuente C (EXTRA 2):** **Padrón de Tiendas Comunitarias DICONSA / SEGALMEX en datos.gob.mx**
  * *Qué buscar:* Ubicación y catálogo de productos con precio subsidiado de las tiendas comunitarias en comisarías de Mérida y Yucatán.
  * *Enlace directo:* [datos.gob.mx - Tiendas Diconsa](https://datos.gob.mx/busca/dataset/tiendas-diconsa).

---

#### 03. Tipo: SIEGY - Yucatán (Estadísticas Estatales y Municipales)

* **Fuente A (Ya en el repo):** `indicadores_socioeconomicos_merida_siegy.csv`
  * *Origen:* [SIEGY Yucatán](https://siegy.yucatan.gob.mx). Datos de PEA, salarios IMSS y pobreza laboral para Mérida y zona conurbada.
* **Fuente B (EXTRA 1):** **Índice de Marginación Urbana por Colonia/AGEB (CONAPO / SIEGY)**
  * *Qué buscar:* Nivel de marginación socioeconómica desglosado por colonia dentro de Mérida (Norte vs. Sur).
  * *Enlace directo:* [CONAPO - Marginación Urbana](https://www.gob.mx/conapo/documentos/indices-de-marginacion-2020-284372) / Portal SIEGY.
* **Fuente C (EXTRA 2):** **Boletín Mensual de Salarios y Empleo Formal IMSS Yucatán (SEPLAN)**
  * *Qué buscar:* Reporte mensual del salario base de cotización formal por sector (comercio, servicios, manufactura) en Yucatán.
  * *Enlace directo:* [Datos Yucatán - Boletines Económicos](https://datos.yucatan.gob.mx/boletines).

---

### MÓDULO 2: LOS MERCADOS PÚBLICOS Y EL GOBIERNO

#### 04. Tipo: Geoportal Mérida (Sistemas de Información Geográfica Municipal)

* **Fuente A (Ya en el repo):** `mercados_municipales_merida.geojson`
  * *Origen:* [Geoportal Mérida](https://geoportal.merida.gob.mx). Capa de polígonos y puntos de los 8 mercados públicos de la ciudad.
* **Fuente B (EXTRA 1):** **Capa de Tianguis y Comercio en Vía Pública del Geoportal de Mérida**
  * *Qué buscar:* Polígonos de tianguis sobre ruedas autorizados en colonias (Macroplaza, Chenkú, Pacabtún, Esperanza, etc.) y días de operación.
  * *Cómo obtenerla:* Entrar al visor en [geoportal.merida.gob.mx/visor/](https://geoportal.merida.gob.mx/visor/) $\rightarrow$ Capas de Comercio/Equipamiento $\rightarrow$ Exportar a GeoJSON/KML.
* **Fuente C (EXTRA 2):** **Capa de Conectividad y Paraderos de Autobús hacia el Centro (IMDUT / Geoportal)**
  * *Qué buscar:* Rutas y paraderos del sistema de transporte (Va y Ven) que conectan las colonias periféricas con el Mercado Lucas de Gálvez.
  * *Enlace directo:* [Geoportal Mérida - Movilidad](https://geoportal.merida.gob.mx) / [IMDUT Yucatán](https://movilidad.yucatan.gob.mx).

---

#### 05. Tipo: Solicitud de Información (Transparencia / PNT)

* **Fuente A (Ya en el repo):** `solicitud_formal_merida.md`
  * *Trámite:* Solicitud ingresada en la PNT al Municipio de Mérida (`YUC - Mérida`) sobre el padrón de locatarios y tarifas de piso en mercados.
* **Fuente B (EXTRA 1):** **Solicitud PNT dirigida a la Central de Abasto de Mérida (Organismo Descentralizado)**
  * *Sujeto obligado en PNT:* `YUC - Central de Abasto Mérida`.
  * *Qué preguntar:* *"Volumen mensual en toneladas de entrada de alimentos básicos (granos, huevo, carne) y tarifas de pesaje cobradas a mayoristas en el último año."*
* **Fuente C (EXTRA 2):** **Solicitud PNT a la Secretaría de Salud de Yucatán (SSY / COFEPRIS)**
  * *Sujeto obligado en PNT:* `Poder Ejecutivo del Estado de Yucatán` $\rightarrow$ `Secretaría de Salud`.
  * *Qué preguntar:* *"Reportes de inspección sanitaria, clausuras y decomisos de alimentos en mal estado realizados en expendios de canasta básica en Mérida durante 2025 y 2026."*

---

### MÓDULO 3: LEVANTAMIENTO DE DATOS EN LA ERA DIGITAL

#### 06. Tipo: Web Scraping (Monitoreo Automatizado de Precios)

* **Fuente A (Ya en el repo):** `precios_canasta_scraping.csv`
  * *Herramienta:* Script Python propio con catálogo de 18 artículos en autoservicios locales (Súper Akí, Dunosusa, Chedraui).
* **Fuente B (EXTRA 1):** **Scraper de Farmacias y Tiendas de Conveniencia en Mérida (OXXO / Farmacias Guadalajara)**
  * *Qué extraer:* Precios de productos de higiene y canasta complementaria (papel higiénico, jabón neutro, leche en polvo infantil).
  * *Sitio web a raspar:* [farmaciasguadalajara.com](https://www.farmaciasguadalajara.com).
* **Fuente C (EXTRA 2):** **Scraper de Apps de Entrega a Domicilio en Mérida (Rappi / UberEats / Cornershop)**
  * *Qué extraer:* Comparativa de precios de los mismos artículos de canasta básica comprados en app vs. en tienda física (para medir el sobreprecio digital de entrega).
  * *Sitio web a raspar:* Catálogos públicos de tiendas en [rappi.com.mx](https://www.rappi.com.mx).

---

#### 07. Tipo: Self-Produced Data (Datos Producidos por el Equipo)

* **Fuente A (Ya en el repo):** `encuesta_campo_merida_piloto.csv`
  * *Instrumento:* Cuestionario formal de 13 preguntas sobre ingresos, gasto semanal y percepción del salario en hogares.
* **Fuente B (EXTRA 1):** **Auditoría Directa de Góndola en Tienditas de Esquina (Bitácora de Campo)**
  * *Dinámica:* Que un integrante del equipo visite 5 tienditas de la esquina de su colonia y anote en una tabla el precio exacto de 5 cosas: 1 kg de tortilla, 1 reja/kilo de huevo, 1 L de leche, 1 kg de frijol y 1 barra de pan.
  * *Entregable:* Archivo `bitacora_precios_tienditas.csv`.
* **Fuente C (EXTRA 2):** **Entrevista Breve Estructurada a Locatarios de Mercados (5 preguntas)**
  * *Dinámica:* Aplicar una breve entrevista a 3 locatarios del Mercado Lucas de Gálvez o de su mercado de barrio:
    1. ¿De dónde trae su mercancía? 2. ¿Cuánto le subieron los precios sus proveedores este mes? 3. ¿La gente compra menos cantidad que antes?
  * *Entregable:* Transcripción y tabla estructurada `entrevistas_locatarios_mercado.csv`.

---

### MÓDULO 4: TECNOLOGÍAS VISUALES Y EL FUTURO DE LAS COMPRAS

#### 08. Tipo: Datos LiDAR (Nube de Puntos 3D y Elevaciones)

* **Fuente A (Ya en el repo):** `lidar_mercado_merida_sample.csv`
  * *Contenido:* Nube de puntos clasificada ASPRS de la techumbre y suelo del Mercado Lucas de Gálvez (Centro de Mérida).
* **Fuente B (EXTRA 1):** **Continuo de Elevaciones Mexicano (CEM 3.0) de INEGI - Ráster GeoTIFF**
  * *Qué buscar:* Modelo Digital de Superficie de alta resolución para la celda de Mérida (Hoja F16C25).
  * *Enlace directo:* [INEGI - Continuo de Elevaciones](https://www.inegi.org.mx/temas/relieve/continental/) (Descarga de archivo `.tif` o `.bil`).
* **Fuente C (EXTRA 2):** **OpenTopography / USGS EarthExplorer (Datos Globales SRTM / NASADEM / GEDI)**
  * *Qué buscar:* Datos de elevación satelital y radar de la Península de Yucatán para comparar la topografía plana de Mérida frente a ciudades montañosas.
  * *Enlace directo:* [OpenTopography Data Portal](https://portal.opentopography.org/datasets) o [USGS EarthExplorer](https://earthexplorer.usgs.gov/).

---

#### 09. Tipo: AR Geospatial (Realidad Aumentada / 3D)

* **Fuente A (Ya en el repo):** `spatial_anchors_merida.geojson`
  * *Contenido:* Archivo GeoJSON con 4 anclas espaciales VPS georreferenciadas frente a las fachadas de tiendas y mercados en Mérida.
* **Fuente B (EXTRA 1):** **Repositorio de Modelos 3D de Productos de Canasta Básica (`.GLB` / `.GLTF`)**
  * *Qué buscar:* Modelos 3D optimizados para web/AR de alimentos esenciales (ej. cartón de leche, canasta de frutas, reja de huevo) con licencia abierta.
  * *Enlace directo:* [Poly Pizza (Modelos 3D Low-Poly abiertos)](https://poly.pizza) o [Sketchfab CC](https://sketchfab.com).
* **Fuente C (EXTRA 2):** **Ruta de Navegación Espacial AR / Waypoints Geoespaciales**
  * *Qué diseñar:* Archivo JSON que conecta puntos secuenciales para guiar en Realidad Aumentada al usuario desde la calle hacia el pasillo más barato del Mercado Lucas de Gálvez.
  * *Herramienta de soporte:* [Google Geospatial Creator para Unity](https://developers.google.com/ar/develop/geospatial/unity/creator).

---

## 4. Reparto Oficial de Fuentes por Integrante (27 Fuentes en Total)

El proyecto está distribuido de manera equitativa entre los **3 integrantes del equipo (9 fuentes por integrante = 27 fuentes)**:

* 👤 **Valeria Nicol Hernández León — Responsable de Fuente A (9 fuentes):**
  * `01-A` INEGI / DENUE (7,520 comercios de canasta básica en Mérida).
  * `02-A` datos.gob.mx / PROFECO (28,288 precios reales QQP Mérida 2026).
  * `03-A` SIEGY Yucatán (PEA, salario IMSS y costo de canasta urbana).
  * `04-A` Geoportal Mérida (Capa SIG de los 8 mercados públicos municipales).
  * `05-A` Solicitud PNT (Trámite formal al H. Ayuntamiento de Mérida sobre locatarios).
  * `06-A` Web Scraping (18 productos básicos en autoservicios locales Akí/Dunosusa).
  * `07-A` Self-Produced (Encuesta formal de campo aplicada a 25 hogares).
  * `08-A` LiDAR 3D (Nube de puntos ASPRS clasificada del Mercado Lucas de Gálvez).
  * `09-A` AR Geospatial (Anclas espaciales VPS para semáforos de precios en fachadas).

* 👤 **Jorge Ramiro Chay Koyoc — Responsable de Fuente B (9 fuentes):**
  * `01-B` INEGI / Censos Económicos SAIC (Ingresos, personal y salarios en alimentos).
  * `02-B` datos.gob.mx / SNIIM (Precios de mayoreo diarios en la Central de Abasto).
  * `03-B` CONAPO / SIEGY (Índice de marginación urbana por colonias en Mérida).
  * `04-B` Geoportal Mérida (Capa SIG de tianguis y comercio rodante autorizado).
  * `05-B` Solicitud PNT (Trámite a la Central de Abasto sobre pesajes y toneladas).
  * `06-B` Web Scraping (Monitoreo en Farmacias Guadalajara y tiendas OXXO).
  * `07-B` Self-Produced (Auditoría de góndola en 5 tienditas de la esquina de Mérida).
  * `08-B` LiDAR / CEM (Malla de elevación continua CEM 3.0 de INEGI para drenaje).
  * `09-B` AR Geospatial (Catálogo y especificación de modelos 3D glTF/GLB para AR).

* 👤 **Isaac René Andrade Sánchez — Responsable de Fuente C (9 fuentes):**
  * `01-C` INEGI / ENOE (Microdatos 1T-2025 de hogares, viviendas y 45 catálogos).
  * `02-C` SEGALMEX / DICONSA (Catálogo oficial de artículos y proveedores DICONSA).
  * `03-C` SENASICA / SEDER (Inspección fitozoosanitaria y movilización agropecuaria).
  * `04-C` IMDUT / Va y Ven (565 rutas y paraderos de transporte conectando al Centro).
  * `05-C` PNT / Sector Salud (Tabulador de remuneraciones de salubridad).
  * `06-C` Web Scraping (2,501 tickets comparando compra física vs delivery Rappi/Uber).
  * `07-C` Self-Produced (3 entrevistas estructuradas a locatarios del Lucas de Gálvez).
  * `08-C` OpenTopography (2,401 cotas satelitales SRTM/NASADEM Mérida vs montañas).
  * `09-C` AR Geospatial (Ruta de 6 waypoints AR hacia el pasillo más barato del mercado).

---

Con esto, el proyecto tendrá los **27 datasets completos (3 por cada uno de los 9 tipos)** sin que nadie se repita.

🔗 **Repositorio GitHub:** [IsaacRAS05/Visualization_data_sources](https://github.com/IsaacRAS05/Visualization_data_sources)
