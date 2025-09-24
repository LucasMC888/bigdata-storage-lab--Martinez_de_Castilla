# 🛡️ Lineamientos de Gobernanza de Datos

## 1. Origen y linaje de datos
- Todo dataset debe registrarse con **fuente de origen** (CSV, API, etc.).
- Mantener trazabilidad: cada transformación (raw → bronze → silver → gold) debe estar documentada.
- Usar carpetas `/data/raw`, `/data/bronze`, `/data/silver`, `/data/gold` para reflejar el linaje.

## 2. Validaciones mínimas
- Formato de fecha debe cumplir ISO (YYYY-MM-DD).
- Montos deben ser numéricos, positivos y en EUR.
- `partner` no puede estar vacío.
- Eliminación de duplicados según combinación (`date`, `partner`, `amount`).

## 3. Política de mínimos privilegios
- Separar roles de **lectura** y **escritura** en el almacén de datos.
- El acceso a capas superiores (silver/gold) se restringe a usuarios analíticos.
- No se deben almacenar ni compartir datos sensibles o identificables.

## 4. Trazabilidad
- Mantener **logs de ingesta y transformación**.
- Incluir comentarios o metadata en cada script indicando versión y responsable.
- Documentar cada KPI derivado con su fuente original y reglas de cálculo.

## 5. Roles
- **Data Engineer**: implementación de pipelines y validaciones.
- **Data Steward**: aseguramiento de la calidad y cumplimiento de gobernanza.
- **Data Analyst**: consumo de datos en silver/gold y construcción de KPIs.
- **Administrador**: gestión de accesos y políticas de seguridad.
