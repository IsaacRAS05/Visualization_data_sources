# 09. Datos de Realidad Aumentada (AR Geospatial Anchors)

## Descripción de la Tecnología y Datos
La **Realidad Aumentada Geoespacial (AR Geospatial)** combina el Sistema de Posicionamiento Visual (**VPS** - Visual Positioning System), sensores inerciales (**IMU**) y geolocalización satelital para anclar contenido tridimensional interactivo a coordenadas exactas del mundo físico.

* **Frameworks compatibles:** Google ARCore Geospatial API / Niantic Lightship VPS / WebXR Device API / Unity AR Foundation.
* **Sistema de Coordenadas:** WGS 84 (Latitud, Longitud, Altitud elipsoidal en metros) y orientación en cuaterniones $(X, Y, Z, W)$ o ángulos de Euler $(yaw, pitch, roll)$.

## Caso de Uso del Dataset:
Superposición de tarjetas interactivas de Realidad Aumentada frente a las fachadas de tiendas y mercados en Mérida:
1. El usuario apunta la cámara del teléfono hacia la fachada del Mercado Lucas de Gálvez o de un supermercado.
2. El sistema detecta el ancla geoespacial (`Geospatial Anchor`).
3. Aparece flotando en el espacio 3D un semáforo de precios con el costo de la canasta básica en ese local comparado con el promedio municipal.

## Archivos en esta carpeta:
* **Fuente A:** `spatial_anchors_merida.geojson` (Dataset GeoJSON con 4 anclas espaciales VPS georreferenciadas con semáforos de precios de canasta básica en Mérida).
* **Fuente B (EXTRA 1):** `catalogo_modelos_3d_canasta.json` (Especificación y catálogo de modelos 3D optimizados en formato glTF/GLB para proyectar canastas, letreros y HUD holográfico en AR).
* `ar_geospatial_config.json`: Archivo de configuración listo para ser consumido por un motor AR (Unity / WebXR / Three.js).
* `visualizar_ar_anchors.py`: Script para validar las anclas espaciales y su contenido interactivo.

