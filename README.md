# De CSVs heterogéneos a un almacén analítico confiable  
Repositorio: `bigdata-storage-lab-<apellido>`

---

## 🎯 Objetivo del laboratorio
El propósito de este laboratorio es diseñar y ejecutar un flujo de procesamiento de datos que permita transformar **archivos CSV heterogéneos** en un **almacén analítico confiable**, siguiendo buenas prácticas de ingeniería de datos:

1. **Ingesta**: recepción y almacenamiento inicial de archivos CSV de distintas fuentes y formatos.  
2. **Validación**: controles básicos (tipos de datos, duplicados, valores nulos, reglas de negocio mínimas).  
3. **Normalización**: unificación de esquemas, estandarización de nombres de columnas, tipos y formatos.  
4. **Persistencia en capas**:  
   - **Bronze**: datos crudos validados.  
   - **Silver**: datos normalizados y listos para análisis.  
5. **Exposición de KPIs**: construcción de métricas agregadas y visualización con una app en **Streamlit**.

---

## 📦 Entregables
- **Repositorio GitHub público** con:
  - Código fuente (scripts/notebooks/pipelines).  
  - Definición del modelo de datos (diccionario de datos o esquema).  
  - Documentación clara en Markdown.  
- **Aplicación Streamlit** publicada (ej. en Streamlit Cloud o similar) que muestre los KPIs principales y el flujo de trabajo.

---

## ✅ Criterios de evaluación
1. **Diseño y justificación técnica**  
   - Elección de librerías/herramientas y explicación de decisiones.  
   - Claridad en la arquitectura de ingesta–procesamiento–almacenamiento.  

2. **Calidad de datos**  
   - Validaciones implementadas.  
   - Manejo explícito de inconsistencias.  

3. **Trazabilidad y diseño de DW**  
   - Organización de capas **bronze/silver**.  
   - Evidencia de lineage o comentarios que permitan seguir el rastro de los datos.  

4. **Documentación**  
   - README y diagramas claros.  
   - Instrucciones reproducibles para ejecutar el laboratorio.  

---

## 🚫 Qué NO subir
- Datos sensibles, personales o confidenciales.  
- Archivos CSV con información propietaria.  
- Credenciales (tokens, claves, contraseñas).  
- Dumps de bases de datos reales.  

En su lugar, utilice **datasets sintéticos o públicos** (ej. Kaggle, data.gov, OpenData).

---

## ⏱️ Tiempo estimado por fase
- **Ingesta de CSVs** → 2 h  
- **Validación y limpieza** → 3 h  
- **Normalización y modelado en capas (bronze/silver)** → 4 h  
- **Generación de KPIs y exposición en Streamlit** → 3 h  
- **Documentación y entrega en GitHub** → 2 h  

**Total estimado:** ~14 horas de trabajo.

---

## 📝 Notas finales
Este laboratorio busca emular un escenario real de **data engineering** donde la trazabilidad y la confianza en los datos son tan importantes como la implementación técnica.  
