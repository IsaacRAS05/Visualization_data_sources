# Del Mundo a la Esquina: ¿Cuánto Cuesta Comer?
### Radiografía multiescalar del salario y la canasta básica: del panorama internacional al territorio de Mérida

Este repositorio consolida los datasets, scripts y especificaciones técnicas organizados bajo un enfoque multiescalar (**Internacional $\rightarrow$ México $\rightarrow$ Yucatán $\rightarrow$ Mérida**).

> 📄 **Documentación completa para el equipo:**  
> * Consulta [`GUIA_FUENTES_Y_EQUIPO.md`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/GUIA_FUENTES_Y_EQUIPO.md) para la guía completa de las 27 fuentes (reparto Fuente A, Fuente B y Fuente C).  
> * Consulta [`FUENTES_DE_DATOS.md`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/FUENTES_DE_DATOS.md) para la ficha técnica y enlaces oficiales de origen.

---

## Estructura Modular del Repositorio

El repositorio está organizado en tres grandes carpetas para facilitar la colaboración del equipo:
* 📂 **`data/fuente_a/`**: Los 9 datasets de la primera ronda (100% listos e integrados).
* 📂 **`data/fuente_b/`**: Los 9 datasets complementarios de la segunda ronda (100% listos e integrados).
* 📂 **`data/fuente_c/`**: Carpetas preparadas con guías para que el equipo suba los 9 datasets finales.

```text
victorrr/
├── data/
│   ├── fuente_a/
│   │   ├── 01_inegi_denue/
│   │   ├── 02_datos_gob_profeco/
│   │   ├── 03_siegy_yucatan/
│   │   ├── 04_geoportal_merida/
│   │   ├── 05_solicitud_pnt/
│   │   ├── 06_scraping_autoservicios/
│   │   ├── 07_encuesta_hogares/
│   │   ├── 08_lidar_mercado/
│   │   └── 09_ar_anclas/
│   ├── fuente_b/
│   │   ├── 01_inegi_saic/
│   │   ├── 02_datos_gob_sniim/
│   │   ├── 03_conapo_marginacion/
│   │   ├── 04_tianguis_geoportal/
│   │   ├── 05_solicitud_central_abasto/
│   │   ├── 06_scraping_farmacias/
│   │   ├── 07_bitacora_tienditas/
│   │   ├── 08_lidar_cem_mde/
│   │   └── 09_ar_modelos_3d/
│   └── fuente_c/  (Asignada al equipo para las 9 fuentes finales)
├── scripts/
│   └── verificar_datasets.py
├── .gitignore
├── FUENTES_DE_DATOS.md
├── GUIA_FUENTES_Y_EQUIPO.md
└── README.md
```

---

## Matriz de Datasets Disponibles (18 Datasets Listos)

| # | Grupo | Tema / Categoría | Archivo Generado | Formato | Cobertura y Descripción |
|---|---|---|---|---|---|
| **01-A** | **Fuente A** | **INEGI / DENUE** | [`denue_merida_alimentos_real.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_a/01_inegi_denue/denue_merida_alimentos_real.csv) | CSV Oficial (3.2 MB) | **7,520 comercios reales** de canasta básica en Mérida (filtrados de 146,384 en Yucatán). |
| **01-B** | **Fuente B** | **INEGI / SAIC** | [`censos_economicos_saic_merida.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_b/01_inegi_saic/censos_economicos_saic_merida.csv) | CSV Censal | Ingresos totales, sueldos y personal en abarrotes y supermercados (SAIC). |
| **02-A** | **Fuente A** | **datos.gob / PROFECO** | [`profeco_merida_2026_real.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_a/02_datos_gob_profeco/profeco_merida_2026_real.csv) | CSV Oficial (7.9 MB) | **28,288 precios reales** en Mérida monitoreados por inspectores PROFECO. |
| **02-B** | **Fuente B** | **datos.gob / SNIIM** | [`sniim_mayoreo_central_abasto_merida.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_b/02_datos_gob_sniim/sniim_mayoreo_central_abasto_merida.csv) | CSV Mayorista | Precios de mayoreo (SNIIM) en la Central de Abasto de Mérida. |
| **03-A** | **Fuente A** | **SIEGY - Yucatán** | [`indicadores_socioeconomicos_merida_siegy.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_a/03_siegy_yucatan/indicadores_socioeconomicos_merida_siegy.csv) | CSV Tabular | PEA, salario formal IMSS y costo de canasta alimentaria CONEVAL ($2,610 MXN). |
| **03-B** | **Fuente B** | **SIEGY / CONAPO** | [`marginacion_urbana_colonias_merida.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_b/03_conapo_marginacion/marginacion_urbana_colonias_merida.csv) | CSV Marginación | Índice CONAPO/SIEGY por colonia en Mérida (contraste Norte vs. Sur). |
| **04-A** | **Fuente A** | **Geoportal Mérida** | [`mercados_municipales_merida.geojson`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_a/04_geoportal_merida/mercados_municipales_merida.geojson) | GeoJSON SIG | 8 mercados públicos nodales permanentes (Lucas de Gálvez, San Benito, etc.). |
| **04-B** | **Fuente B** | **Geoportal Mérida** | [`tianguis_comercio_via_publica_merida.geojson`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_b/04_tianguis_geoportal/tianguis_comercio_via_publica_merida.geojson) | GeoJSON SIG | Polígonos de tianguis sobre ruedas autorizados en colonias y días de operación. |
| **05-A** | **Fuente A** | **Solicitud PNT** | [`solicitud_formal_merida.md`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_a/05_solicitud_pnt/solicitud_formal_merida.md) | Trámite PNT | Solicitud formal ingresada al Ayto. de Mérida sobre padrón de locatarios. |
| **05-B** | **Fuente B** | **Solicitud PNT** | [`solicitud_pnt_central_abasto_merida.md`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_b/05_solicitud_central_abasto/solicitud_pnt_central_abasto_merida.md) | Trámite PNT | Solicitud formal a la Central de Abasto de Mérida sobre toneladas y pesajes. |
| **06-A** | **Fuente A** | **Web Scraping** | [`precios_canasta_scraping.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_a/06_scraping_autoservicios/precios_canasta_scraping.csv) | CSV Scraper | 18 artículos esenciales en supermercados (Súper Akí, Chedraui, Dunosusa). |
| **06-B** | **Fuente B** | **Web Scraping** | [`precios_farmacias_conveniencia_merida.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_b/06_scraping_farmacias/precios_farmacias_conveniencia_merida.csv) | CSV Scraper | Monitoreo de canasta complementaria en Farmacias Guadalajara, OXXO y Similares. |
| **07-A** | **Fuente A** | **Self-Produced** | [`encuesta_campo_merida_piloto.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_a/07_encuesta_hogares/encuesta_campo_merida_piloto.csv) | CSV Primario | Encuesta formal aplicada a 25 hogares sobre gasto semanal y salarios. |
| **07-B** | **Fuente B** | **Self-Produced** | [`bitacora_precios_tienditas.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_b/07_bitacora_tienditas/bitacora_precios_tienditas.csv) | CSV Auditoría | Auditoría directa en 5 tienditas de colonias sobre 5 alimentos de consumo diario. |
| **08-A** | **Fuente A** | **LiDAR 3D** | [`lidar_mercado_merida_sample.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_a/08_lidar_mercado/lidar_mercado_merida_sample.csv) | CSV / 3D ASPRS | Nube 3D con clasificación ASPRS (Suelo, Árboles y Domo del Mercado Lucas de Gálvez). |
| **08-B** | **Fuente B** | **LiDAR / CEM** | [`inegi_cem_mde_merida_grid.csv`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_b/08_lidar_cem_mde/inegi_cem_mde_merida_grid.csv) | CSV Malla MDE | Malla de elevación CEM 3.0 de INEGI para evaluar pendientes y encharcamientos. |
| **09-A** | **Fuente A** | **AR Geospatial** | [`spatial_anchors_merida.geojson`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_a/09_ar_anclas/spatial_anchors_merida.geojson) | GeoJSON VPS | Anclas espaciales para proyectar semáforos de precios 3D sobre fachadas. |
| **09-B** | **Fuente B** | **AR Geospatial** | [`catalogo_modelos_3d_canasta.json`](file:///c:/Users/nixle/Downloads/visual_folder/UPY/victorrr/data/fuente_b/09_ar_modelos_3d/catalogo_modelos_3d_canasta.json) | JSON Catálogo | Especificación técnica de assets 3D glTF/GLB optimizados para WebXR / ARCore. |

---

## Verificación del Repositorio

Para comprobar el estado y resumen de los 18 datasets en cualquier momento, ejecuta en la terminal:

```bash
python scripts/verificar_datasets.py
```

## 🚀 Visores Interactivos y Experiencias Web (Listos para Abrir)

El proyecto incluye aplicaciones web autónomas e interactivas que puedes abrir con doble clic en tu navegador:

1. 🗺️ **[Visor SIG de Mercados Municipales](data/fuente_a/04_geoportal_merida/visor_mercados_municipales.html):** Mapa interactivo en Leaflet con la red de 8 mercados públicos de Mérida, fichas técnicas y radios de caminabilidad de 10 minutos a pie (isocronas de 800m).
2. 🏛️ **[Visor 3D LiDAR Mercado Lucas de Gálvez](data/fuente_a/08_lidar_mercado/visor_3d_mercado.html):** Espacio 3D en Three.js para orbitar, inspeccionar y medir las cotas altimétricas del domo y la techumbre del mercado central a partir de la nube de retornos láser.
3. 📱 **[Visor WebXR / AR de Semáforo de Precios](data/fuente_a/09_ar_anclas/visor_ar_web.html):** Experiencia de Realidad Aumentada con cámara en vivo o simulación 360° para proyectar anclas espaciales y semáforos de canasta básica sobre las coordenadas de los mercados de Mérida.

---

## 👥 Colaboración del Equipo

* Consulta [`GUIA_FUENTES_Y_EQUIPO.md`](GUIA_FUENTES_Y_EQUIPO.md) para el reparto de la Fuente C.
* Consulta [`PROTOCOLO_INTEGRACION_PERSONA_B.md`](PROTOCOLO_INTEGRACION_PERSONA_B.md) para la guía paso a paso del integrante asignado a la Fuente B.
* Consulta [`FUENTES_DE_DATOS.md`](FUENTES_DE_DATOS.md) para los enlaces de origen de cada institución.

---

## 📌 Control de Estado y Notas de Ejecución

* **Plataforma Nacional de Transparencia (PNT - 05-A y 05-B):**
  * 🟡 **Estado:** En espera de respuesta formal del H. Ayuntamiento de Mérida y Central de Abasto (plazo legal: 15 días hábiles).
  * 🛡️ **Plan B (Instituciones de respaldo):** Si no entregan la información, se solicitará de inmediato a **SEFOET Yucatán**, **SEDER Yucatán** o **PROFECO Delegación Yucatán**.
* **Encuestas en Campo (07-A y 07-B):**
  * 📋 Contamos con 25 encuestas de hogares y 5 tienditas auditadas en piloto. Los instrumentos y cuestionarios están listos para ampliar la muestra en colonias de Mérida.
* **Scraping de Supermercados y Farmacias (06-A y 06-B):**
  * 💻 Scripts funcionales con pausas éticas (2-5 segundos) y extractor conectado a los **28,288 precios reales de inspectores PROFECO en Mérida** ([`precios_canasta_supermercados_reales.csv`](data/fuente_a/06_scraping_autoservicios/precios_canasta_supermercados_reales.csv)).
