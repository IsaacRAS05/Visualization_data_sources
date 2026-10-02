# 07. Self-Produced Data (Datos Producidos por uno Mismo)

## Descripción de la Metodología
Los **datos producidos por uno mismo** (*self-produced data*) son datos primarios recolectados directamente por el investigador mediante instrumentos de campo diseñados a medida. Permiten capturar variables cualitativas y cuantitativas que no existen en los registros estadísticos oficiales.

* **Tema del Levantamiento:** Hábitos de compra, gasto semanal en canasta básica y percepción del salario mínimo en hogares de Mérida.
* **Técnica de recolección:** Encuesta estructurada aplicada en campo mediante formularios móviles (KoboToolbox / Google Forms / ODK Collect).
* **Muestreo:** Estratificado por zonas de la ciudad (Centro, Norte, Poniente, Oriente y Sur).
* **Aspectos Éticos:** Consentimiento informado de los participantes, anonimización total y protección de datos personales.

## Variables del Dataset Primario
1. `id_encuesta`: Folio único de cuestionario.
2. `fecha_hora`: Fecha y hora del levantamiento.
3. `zona_merida`: Zona geográfica (Centro, Norte, Sur, Poniente, Oriente).
4. `colonia`: Nombre de la colonia o fraccionamiento.
5. `integrantes_hogar`: Número de personas que dependen del gasto del hogar.
6. `ingreso_mensual_hogar_mxn`: Rango de ingreso familiar total en pesos.
7. `gasto_semanal_alimentos_mxn`: Gasto estimado en canasta de alimentos y bebidas por semana.
8. `lugar_compra_principal`: Establecimiento principal de compra (Mercado municipal, Supermercado, Tienda de abarrotes de la esquina, Tianguis).
9. `producto_mayor_impacto_alza`: Producto que el usuario percibe con mayor encarecimiento reciente.
10. `percepcion_salario_minimo`: Evaluación de si el salario mínimo actual cubre o no las necesidades básicas (Totalmente insuficiente, Insuficiente, Apenas suficiente, Suficiente).
11. `metodo_pago_habitual`: Efectivo, Tarjeta de débito/crédito, Transferencia bancaria (CoDi / Dimo).

## Archivos en esta carpeta:
* **Fuente A:** `encuesta_campo_merida_piloto.csv` (Encuesta de 13 variables aplicada a 25 hogares sobre gasto semanal, lugar de abasto y percepción salarial).
* **Fuente B (EXTRA 1):** `bitacora_precios_tienditas.csv` (Auditoría de campo directa realizada en 5 tienditas de la esquina de colonias populares de Mérida: Centro, Caucel, Tecoh, Pacabtún y Montejo sobre 5 alimentos clave).
* `instrumento_cuestionario_canasta.md`: El diseño completo de las preguntas para implementar en Google Forms o KoboToolbox.
* `analizar_encuesta.py`: Script para procesar y resumir estadísticamente los hallazgos de campo.

