# 02. datos.gob.mx - Quién es Quién en los Precios (PROFECO)

## Descripción de la Fuente
El portal **datos.gob.mx** es la plataforma central de la Política de Datos Abiertos del Gobierno de México. Una de sus bases de datos más relevantes sobre consumo popular es el programa **Quién es Quién en los Precios (QQP)** de la Procuraduría Federal del Consumidor (PROFECO).

* **Institución:** Procuraduría Federal del Consumidor (PROFECO) / datos.gob.mx
* **Licencia:** Libre Uso MX (Datos abiertos gubernamentales).
* **Frecuencia:** Monitoreo semanal.
* **Cobertura:** Ciudades principales de México, incluyendo **Mérida, Yucatán**.

## Productos Clave Monitoreados (Canasta Básica)
1. Tortilla de maíz a granel (1 kg).
2. Frijol negro en grano (1 kg en bolsa).
3. Arroz pulido grano largo (1 kg).
4. Aceite comestible mixto / vegetal (botella de 800 - 900 ml).
5. Huevo blanco fresco (paquete de 18 piezas o 1 kg).
6. Leche pasteurizada entera (1 litro).
7. Pollo entero fresco (1 kg).
8. Chuleta de puerco fresca (1 kg).
9. Azúcar estándar (1 kg).

## Variables del Dataset
* `fecha_levantamiento`: Fecha en que el verificador de PROFECO registró el precio en la tienda.
* `cadena_comercial`: Nombre de la cadena (ej. Chedraui, Walmart, Soriana, Bodega Aurrera, Mercado Municipal).
* `sucursal`: Nombre o dirección de la sucursal en Mérida.
* `municipio`: Mérida.
* `estado`: Yucatán.
* `categoria`: Alimentos / Canasta Básica / Abarrotes.
* `producto`: Nombre genérico del bien de consumo.
* `marca_presentacion`: Marca y gramaje específico.
* `precio_monitoreado`: Precio en pesos mexicanos ($ MXN) reportado al consumidor.

## Archivos en esta carpeta:
* **Fuente A:** `profeco_merida_2026_real.csv` (28,288 precios reales de 2026 monitoreados por inspectores de PROFECO en Mérida).
* **Fuente B (EXTRA 1):** `sniim_mayoreo_central_abasto_merida.csv` (Precios mayoristas y medio mayoreo del SNIIM - Secretaría de Economía / datos.gob.mx para la Central de Abasto de Mérida).
* `profeco_qqp_merida_sample.csv`: Muestra sintética inicial de referencia.
* `consultar_datos_gob.py`: Script en Python para explorar la API CKAN de datos.gob.mx.

