# Catálogo Maestro y Resumen de las 27 Fuentes de Datos
## Proyecto: "Del Mundo a la Esquina: ¿Cuánto Cuesta Comer?"
### Radiografía multiescalar del salario y la canasta básica: del panorama internacional al territorio de Mérida

> 📌 **Estado del Repositorio:** **27 de 27 fuentes listas, verificadas e integradas al 100%** en el repositorio.  
> Cada una de las 9 categorías temáticas cuenta con sus **3 fuentes independientes** (Fuente A, Fuente B y Fuente C).

---

## 1. Tabla Resumen Ejecutiva de las 27 Fuentes

| # | Categoría Temática | Grupo | Institución / Origen | Enlace Oficial de Referencia | Archivo Local en el Repositorio | Resumen de Contenido y Cobertura | Estatus |
|---|---|---|---|---|---|---|:---:|
| **01-A** | **01. Directorios / Censos** | Fuente A | **INEGI (DENUE)** | [inegi.org.mx/app/descarga](https://www.inegi.org.mx/app/descarga/?ti=6) | [`data/fuente_a/01_inegi_denue/denue_merida_alimentos_real.csv`](data/fuente_a/01_inegi_denue/denue_merida_alimentos_real.csv) | **7,520 comercios** de alimentos y canasta básica en Mérida (SCIAN 4611/4621). | ✅ Listo |
| **01-B** | **01. Directorios / Censos** | Fuente B | **INEGI (Censos / SAIC)** | [inegi.org.mx/programas/ce](https://www.inegi.org.mx/programas/ce/) | [`data/fuente_b/01_inegi_saic/censos_economicos_saic_merida.csv`](data/fuente_b/01_inegi_saic/censos_economicos_saic_merida.csv) | Ingresos totales, sueldos y personal ocupado en comercio de alimentos. | ✅ Listo |
| **01-C** | **01. Directorios / Censos** | Fuente C | **INEGI (ENOE Microdatos)** | [inegi.org.mx/programas/enoe](https://www.inegi.org.mx/programas/enoe/15ymas/) | [`data/fuente_c/01_enoe_microdatos/0_indice_tablas_enoe_2025_1t.csv`](data/fuente_c/01_enoe_microdatos/0_indice_tablas_enoe_2025_1t.csv) | Microdatos 1T-2025 de hogares y viviendas (>300,000 registros + 45 catálogos). | ✅ Listo |
| **02-A** | **02. Precios / Datos Abiertos** | Fuente A | **PROFECO (QQP 2026)** | [datos.profeco.gob.mx](https://datos.profeco.gob.mx/datos_abiertos/qqp.php) | [`data/fuente_a/02_datos_gob_profeco/profeco_merida_2026_real.csv`](data/fuente_a/02_datos_gob_profeco/profeco_merida_2026_real.csv) | **28,288 precios reales** monitoreados en tiendas y mercados de Mérida. | ✅ Listo |
| **02-B** | **02. Precios / Datos Abiertos** | Fuente B | **SNIIM (Secretaría Economía)** | [economia-sniim.gob.mx](http://www.economia-sniim.gob.mx/) | [`data/fuente_b/02_datos_gob_sniim/sniim_mayoreo_central_abasto_merida.csv`](data/fuente_b/02_datos_gob_sniim/sniim_mayoreo_central_abasto_merida.csv) | Precios diarios de mayoreo y medio mayoreo en la Central de Abasto de Mérida. | ✅ Listo |
| **02-C** | **02. Precios / Datos Abiertos** | Fuente C | **SEGALMEX / DICONSA** | [datos.gob.mx/busca/dataset/tiendas-diconsa](https://datos.gob.mx/busca/dataset/tiendas-diconsa) | [`data/fuente_c/02_diconsa_segalmex/DICONSA_8_Listado_de_articulos_por_proveedor.csv`](data/fuente_c/02_diconsa_segalmex/DICONSA_8_Listado_de_articulos_por_proveedor.csv) | **4,064 artículos** subsidiados de canasta básica y proveedores Diconsa. | ✅ Listo |
| **03-A** | **03. Indicadores Estatales** | Fuente A | **SIEGY Yucatán / CONEVAL** | [siegy.yucatan.gob.mx](https://siegy.yucatan.gob.mx) | [`data/fuente_a/03_siegy_yucatan/indicadores_socioeconomicos_merida_siegy.csv`](data/fuente_a/03_siegy_yucatan/indicadores_socioeconomicos_merida_siegy.csv) | PEA, informalidad, salario IMSS y costo de canasta alimentaria urbana ($2,610). | ✅ Listo |
| **03-B** | **03. Indicadores Estatales** | Fuente B | **CONAPO / SIEGY** | [gob.mx/conapo](https://www.gob.mx/conapo/documentos/indices-de-marginacion-2020-284372) | [`data/fuente_b/03_conapo_marginacion/marginacion_urbana_colonias_merida.csv`](data/fuente_b/03_conapo_marginacion/marginacion_urbana_colonias_merida.csv) | Grados de marginación urbana por colonias y AGEBs en Mérida (Norte vs. Sur). | ✅ Listo |
| **03-C** | **03. Indicadores Estatales** | Fuente C | **SENASICA / SEDER** | [datos.gob.mx](https://datos.gob.mx) | [`data/fuente_c/03_imss_boletin/01_actividades-inspeccion-movilizacion_2dotrim2025.csv`](data/fuente_c/03_imss_boletin/01_actividades-inspeccion-movilizacion_2dotrim2025.csv) | Puntos de inspección fitozoosanitaria y movilización de productos pecuarios. | ✅ Listo |
| **04-A** | **04. SIG Municipal / Geoportal** | Fuente A | **Geoportal Mérida (Mercados)** | [geoportal.merida.gob.mx](https://geoportal.merida.gob.mx) | [`data/fuente_a/04_geoportal_merida/mercados_municipales_merida.geojson`](data/fuente_a/04_geoportal_merida/mercados_municipales_merida.geojson) | Polígonos y puntos de los 8 mercados públicos nodales de Mérida. | ✅ Listo |
| **04-B** | **04. SIG Municipal / Geoportal** | Fuente B | **Geoportal Mérida (Tianguis)** | [geoportal.merida.gob.mx/visor](https://geoportal.merida.gob.mx/visor/) | [`data/fuente_b/04_tianguis_geoportal/tianguis_comercio_via_publica_merida.geojson`](data/fuente_b/04_tianguis_geoportal/tianguis_comercio_via_publica_merida.geojson) | Tianguis sobre ruedas autorizados en colonias, días y aforos. | ✅ Listo |
| **04-C** | **04. SIG Municipal / Geoportal** | Fuente C | **IMDUT / Va y Ven** | [movilidad.yucatan.gob.mx](https://movilidad.yucatan.gob.mx) | [`data/fuente_c/04_transporte_vayven/export.geojson`](data/fuente_c/04_transporte_vayven/export.geojson) | **565 rutas y paraderos** del sistema Va y Ven conectando con el Centro. | ✅ Listo |
| **05-A** | **05. Solicitud PNT** | Fuente A | **PNT / Ayuntamiento Mérida** | [plataformadetransparencia.org.mx](https://www.plataformadetransparencia.org.mx) | [`data/fuente_a/05_solicitud_pnt/solicitud_formal_merida.md`](data/fuente_a/05_solicitud_pnt/solicitud_formal_merida.md) | Solicitud formal de padrón de locatarios y tarifas de piso en mercados públicos. | ✅ Listo |
| **05-B** | **05. Solicitud PNT** | Fuente B | **PNT / Central de Abasto** | [plataformadetransparencia.org.mx](https://www.plataformadetransparencia.org.mx) | [`data/fuente_b/05_solicitud_central_abasto/solicitud_pnt_central_abasto_merida.md`](data/fuente_b/05_solicitud_central_abasto/solicitud_pnt_central_abasto_merida.md) | Solicitud de pesajes y volumen mensual en toneladas de entrada de alimentos. | ✅ Listo |
| **05-C** | **05. Solicitud PNT** | Fuente C | **PNT / Sector Salud** | [plataformadetransparencia.org.mx](https://www.plataformadetransparencia.org.mx) | [`data/fuente_c/05_solicitud_salubridad/remuneraciones_trim02_2026.csv`](data/fuente_c/05_solicitud_salubridad/remuneraciones_trim02_2026.csv) | Tabulador oficial de remuneraciones netas y brutas del sector salud (41 puestos). | ✅ Listo |
| **06-A** | **06. Web Scraping Precios** | Fuente A | **Scraper Supermercados** | [superaki.mx](https://superaki.mx) / [dunosusa.com.mx](https://dunosusa.com.mx) | [`data/fuente_a/06_scraping_autoservicios/precios_canasta_scraping.csv`](data/fuente_a/06_scraping_autoservicios/precios_canasta_scraping.csv) | 18 artículos de consumo básico en autoservicios locales (Akí, Chedraui, Dunosusa). | ✅ Listo |
| **06-B** | **06. Web Scraping Precios** | Fuente B | **Scraper Farmacias / Tiendas** | [farmaciasguadalajara.com](https://www.farmaciasguadalajara.com) / [oxxo.com](https://www.oxxo.com) | [`data/fuente_b/06_scraping_farmacias/precios_farmacias_conveniencia_merida.csv`](data/fuente_b/06_scraping_farmacias/precios_farmacias_conveniencia_merida.csv) | Precios de higiene y canasta complementaria en Farmacias Guadalajara y OXXO. | ✅ Listo |
| **06-C** | **06. Web Scraping Precios** | Fuente C | **Scraper Delivery Apps** | [rappi.com.mx](https://www.rappi.com.mx) / [ubereats.com](https://www.ubereats.com) | [`data/fuente_c/06_scraping_delivery/comparativa_precios_canasta_basica.csv`](data/fuente_c/06_scraping_delivery/comparativa_precios_canasta_basica.csv) | **2,501 tickets** comparando tienda física vs app directa vs delivery con tarifas. | ✅ Listo |
| **07-A** | **07. Self-Produced Data** | Fuente A | **Encuesta Hogares Mérida** | Levantamiento directo en campo | [`data/fuente_a/07_encuesta_hogares/encuesta_campo_merida_piloto.csv`](data/fuente_a/07_encuesta_hogares/encuesta_campo_merida_piloto.csv) | Encuesta de 13 preguntas sobre ingresos, gasto semanal y abasto (25 hogares). | ✅ Listo |
| **07-B** | **07. Self-Produced Data** | Fuente B | **Bitácora Tienditas Esquina** | Auditoría directa en góndola | [`data/fuente_b/07_bitacora_tienditas/bitacora_precios_tienditas.csv`](data/fuente_b/07_bitacora_tienditas/bitacora_precios_tienditas.csv) | Monitoreo directo en 5 tienditas de colonias de 5 alimentos de consumo diario. | ✅ Listo |
| **07-C** | **07. Self-Produced Data** | Fuente C | **Entrevistas Locatarios** | Entrevistas presenciales | [`data/fuente_c/07_entrevistas_mercado/entrevistas_locatarios_mercado.csv`](data/fuente_c/07_entrevistas_mercado/entrevistas_locatarios_mercado.csv) | Entrevistas a locatarios del Lucas de Gálvez (proveedores, mermas y ventas). | ✅ Listo |
| **08-A** | **08. Datos LiDAR / 3D** | Fuente A | **LiDAR ASPRS Lucas Gálvez** | [asprs.org](https://www.asprs.org) / INEGI | [`data/fuente_a/08_lidar_mercado/lidar_mercado_merida_sample.csv`](data/fuente_a/08_lidar_mercado/lidar_mercado_merida_sample.csv) | Nube 3D con clasificación ASPRS (suelo, arbolado y domo del mercado central). | ✅ Listo |
| **08-B** | **08. Datos LiDAR / 3D** | Fuente B | **CEM 3.0 INEGI (MDE)** | [inegi.org.mx/temas/relieve](https://www.inegi.org.mx/temas/relieve/continental/) | [`data/fuente_b/08_lidar_cem_mde/inegi_cem_mde_merida_grid.csv`](data/fuente_b/08_lidar_cem_mde/inegi_cem_mde_merida_grid.csv) | Malla de elevación continua de Mérida para análisis de pendientes y drenaje. | ✅ Listo |
| **08-C** | **08. Datos LiDAR / 3D** | Fuente C | **OpenTopography / Radar** | [portal.opentopography.org](https://portal.opentopography.org/) | [`data/fuente_c/08_opentopography/topografia_srtm_nasadem_merida_vs_montanas.csv`](data/fuente_c/08_opentopography/topografia_srtm_nasadem_merida_vs_montanas.csv) | **2,401 cotas** satelitales SRTM/NASADEM comparando Mérida vs zonas montañosas. | ✅ Listo |
| **09-A** | **09. Realidad Aumentada / AR** | Fuente A | **Google ARCore / VPS** | [developers.google.com/ar](https://developers.google.com/ar/develop/geospatial) | [`data/fuente_a/09_ar_anclas/spatial_anchors_merida.geojson`](data/fuente_a/09_ar_anclas/spatial_anchors_merida.geojson) | Anclas espaciales georreferenciadas con semáforos de precios 3D en fachadas. | ✅ Listo |
| **09-B** | **09. Realidad Aumentada / AR** | Fuente B | **Poly Pizza / Modelos glTF** | [poly.pizza](https://poly.pizza) | [`data/fuente_b/09_ar_modelos_3d/catalogo_modelos_3d_canasta.json`](data/fuente_b/09_ar_modelos_3d/catalogo_modelos_3d_canasta.json) | Especificación y catálogo de modelos 3D glTF/GLB optimizados para WebXR. | ✅ Listo |
| **09-C** | **09. Realidad Aumentada / AR** | Fuente C | **Geospatial Creator / AR** | [developers.google.com/ar](https://developers.google.com/ar) | [`data/fuente_c/09_ar_waypoints/ruta_ar_lucas_galvez.json`](data/fuente_c/09_ar_waypoints/ruta_ar_lucas_galvez.json) | Ruta de 6 waypoints AR para guiar desde Calle 56 hacia el pasillo más barato. | ✅ Listo |

---

## 2. Resumen por Módulo Temático (Triangulación de las 3 Fuentes)

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        ESTRUCTURA DE TRIANGULACIÓN                     │
├────────────────────────────────────────────────────────────────────────┤
│  MÓDULO 1: LA REALIDAD ECONÓMICA                                       │
│    • Categoría 01 (Censos/Negocios): DENUE (A) + SAIC (B) + ENOE (C)    │
│    • Categoría 02 (Precios Oficiales): PROFECO (A) + SNIIM (B) + DICONSA(C)│
│    • Categoría 03 (Indicadores): SIEGY (A) + CONAPO (B) + SANIDAD (C)   │
│                                                                        │
│  MÓDULO 2: ABASTO POPULAR Y GOBIERNO                                   │
│    • Categoría 04 (Cartografía SIG): Mercados (A) + Tianguis (B) + Va y Ven (C)│
│    • Categoría 05 (Transparencia): Ayto. Mérida (A) + Central Abasto (B) + Salud (C)│
│                                                                        │
│  MÓDULO 3: LEVANTAMIENTO DIGITAL Y DE CAMPO                            │
│    • Categoría 06 (Scraping Web): Súper (A) + Farmacias (B) + Delivery (C) │
│    • Categoría 07 (Datos Propios): Hogares (A) + Tienditas (B) + Locatarios (C)│
│                                                                        │
│  MÓDULO 4: TECNOLOGÍAS ESPACIALES E INMERSIVAS                         │
│    • Categoría 08 (Nube 3D / Relieve): LiDAR Domo (A) + CEM INEGI (B) + SRTM (C)│
│    • Categoría 09 (Realidad Aumentada): Anclas VPS (A) + Assets 3D (B) + Waypoints (C)│
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Visores Interactivos y Experiencias Web Disponibles

El proyecto ya cuenta con visores web independientes que se pueden abrir con doble clic:

1. 🗺️ **[Visor SIG de Mercados Municipales](data/fuente_a/04_geoportal_merida/visor_mercados_municipales.html):** Mapa interactivo a todo color en Leaflet con la red de mercados, isocronas de caminabilidad de 10 minutos (800m) y capas satelitales/topográficas sin bloqueos 403 ni dependencias de API keys.
2. 🏛️ **[Visor 3D LiDAR Mercado Lucas de Gálvez](data/fuente_a/08_lidar_mercado/visor_3d_mercado.html):** Espacio 3D en Three.js con navegación orbital y calibración de cotas altimétricas del techo monumental.
3. 📱 **[Visor WebXR / AR de Semáforo de Precios](data/fuente_a/09_ar_anclas/visor_ar_web.html):** Experiencia inmersiva con cámara en vivo o simulación de 360° para proyectar anclas espaciales y ahorros de canasta básica sobre fachadas.

---

## 4. Comando de Verificación Automatizada

Para ejecutar en terminal el diagnóstico y confirmar la existencia y tamaño de cada uno de los 27 archivos:

```bash
python scripts/verificar_datasets.py
```
*(Resultado esperado: 27 de 27 datasets listos en disco).*
