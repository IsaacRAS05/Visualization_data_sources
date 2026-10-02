# Protocolo de Integración y Colaboración: Fuente B
### Guía Técnica para Jorge Ramiro Chay Koyoc (Responsable de Fuente B)

¡Bienvenido, **Jorge**, al repositorio del proyecto **"Del Mundo a la Esquina: ¿Cuánto Cuesta Comer?"**!

Este documento explica cómo está organizada la **Fuente B**, qué contiene cada una de tus 9 carpetas y las instrucciones exactas para que integres tus datos sin generar ningún conflicto de código o de Git (*merge conflicts*).

---

## 1. Dónde se encuentra tu trabajo: `data/fuente_b/`

Para que todo el equipo trabaje en paralelo sin pisarse los pies, **todo el contenido de la Fuente B vive de forma 100% aislada dentro de la carpeta `data/fuente_b/`**:

```text
data/fuente_b/
├── 01_inegi_saic/                 # Censos Económicos (Ingresos, personal y salarios en alimentos)
├── 02_datos_gob_sniim/            # Precios mayoristas Central de Abasto (Secretaría de Economía)
├── 03_conapo_marginacion/         # Índice de Marginación Urbana por colonia (CONAPO / SIEGY)
├── 04_tianguis_geoportal/         # Tianguis en vía pública autorizados (GeoJSON de comercio rodante)
├── 05_solicitud_central_abasto/   # Trámite formal PNT a la Central de Abasto de Mérida
├── 06_scraping_farmacias/         # Scraper de farmacias y tiendas de conveniencia (OXXO, Guadalajara)
├── 07_bitacora_tienditas/         # Auditoría de campo en 5 tienditas de la esquina de Mérida
├── 08_lidar_cem_mde/              # Malla de elevación CEM 3.0 de INEGI (Modelo Digital de Elevación)
└── 09_ar_modelos_3d/              # Catálogo y especificaciones de assets 3D glTF/GLB para AR
```

> 💡 **Nota importante:** Todas estas carpetas **ya cuentan con una base funcional y datos limpios pre-estructurados**. Si tienes nuevas versiones de tus archivos o datos adicionales, simplemente colócalos o reemplázalos dentro de su respectiva subcarpeta.

---

## 2. Las 3 Reglas de Oro para Colaborar en Git sin Conflictos

1. **Trabaja únicamente dentro de `data/fuente_b/`:**  
   No modifiques archivos dentro de `data/fuente_a/` ni de `data/fuente_c/`. Al mantenerte dentro de tu carpeta, Git te permitirá hacer `pull` y `push` sin ningún conflicto de fusión.
2. **Conserva los nombres de columnas estándar:**  
   Si reemplazas o enriqueces un CSV, mantén nombres de columnas intuitivos en minúsculas (por ejemplo: `producto`, `precio`, `colonia`, `cadena_comercial`). Esto permite que los visores y scripts analíticos sigan leyendo tus datos automáticamente.
3. **Valida antes de subir:**  
   Antes de hacer `git push`, corre en tu terminal:
   ```bash
   python scripts/verificar_datasets.py
   ```
   Si el script marca `18/18 Datasets Verificados`, tus cambios están impecables y listos para subirse.

---

## 3. ¿Qué hará el equipo automáticamente en cuanto subas tus fuentes?

Tan pronto como hagas `git push` con tus fuentes o envíes tus archivos:

1. **Tu capa de Tianguis (04-B):** Se acoplará directamente al visor de mercados municipales para mostrar la red completa de abasto formal vs ambulante en Mérida.
2. **Tus precios del SNIIM (02-B):** Se cruzarán contra los 28k registros de PROFECO (`02-A`) para calcular el margen de ganancia de los intermediarios en la canasta básica.
3. **Tu base de CONAPO (03-B):** Se cruzará contra los 7,520 comercios de DENUE (`01-A`) para generar el mapa de desiertos alimentarios en colonias populares de Mérida.
4. **Tus modelos 3D (09-B):** Se enlazarán en el visor WebXR / AR para que el semáforo proyecte los modelos 3D flotantes sobre las fachadas de los mercados.

---

## 4. Comandos rápidos de Git para subir tus avances

```bash
# 1. Asegúrate de tener los últimos cambios del equipo
git pull origin main

# 2. Agrega únicamente tus cambios de la Fuente B
git add data/fuente_b/

# 3. Guarda tu commit
git commit -m "feat(fuente_b): actualizacion de datasets y fuentes de la persona B"

# 4. Sube tus cambios al repositorio oficial
git push origin main
```
