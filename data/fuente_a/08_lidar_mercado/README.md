# 08. Datos LiDAR (Light Detection and Ranging)

## Descripción de la Tecnología y Fuente
El **LiDAR** es un sensor activo aerotransportado o terrestre que emite pulsos de luz láser para calcular distancias exactas en tres dimensiones $(X, Y, Z)$. En México, el **INEGI** realiza vuelos fotogramétricos y LiDAR para generar el **Continuo de Elevaciones Mexicano (CEM)** y nubes de puntos georreferenciadas.

* **Institución:** Instituto Nacional de Estadística y Geografía (INEGI) - Dirección General de Geografía y Medio Ambiente.
* **Proyección / CRS:** UTM Zona 16 Norte (WGS 84 / EPSG:32616).
* **Formatos estándar:** `.LAS` / `.LAZ` (binario ASPRS) o tablas de puntos $(X, Y, Z, I, C)$.

## Estándar de Clasificación ASPRS (American Society for Photogrammetry and Remote Sensing):
* **Clase 1:** Sin clasificar / Ruido.
* **Clase 2:** Terreno natural / Suelo (Ground).
* **Clase 3, 4, 5:** Vegetación baja, media y alta (copas de árboles).
* **Clase 6:** Edificaciones y techumbres comerciales (Buildings).
* **Clase 9:** Cuerpos de agua.

## Aplicación en el Proyecto:
Permite analizar la morfología urbana de los centros de abasto en Mérida (Mercado Lucas de Gálvez):
* Altura de techumbres y ventilación de naves comerciales.
* Cálculo de volumen construido y sombras urbanas sobre tianguis al aire libre.
* Modelo Digital de Superficie (MDS) vs Modelo Digital de Terreno (MDT).

## Archivos en esta carpeta:
* **Fuente A:** `lidar_mercado_merida_sample.csv` (Muestra de nube de puntos 3D de alta densidad con clasificación ASPRS de techumbres y terreno del Mercado Lucas de Gálvez).
* **Fuente B (EXTRA 1):** `inegi_cem_mde_merida_grid.csv` (Malla de elevaciones del Continuo de Elevaciones Mexicano CEM 3.0 de INEGI para Mérida, con pendientes, aspectos e índice de vulnerabilidad a encharcamientos).
* `procesar_lidar.py`: Script para cargar la nube, filtrar por clasificación ASPRS y calcular perfiles de elevación.

