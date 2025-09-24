# 📖 Diccionario de Datos Canónico

## Esquema Canónico
| Campo    | Tipo de dato  | Descripción                                  |
|----------|---------------|----------------------------------------------|
| date     | DATE (YYYY-MM-DD) | Fecha del registro en formato ISO estándar |
| partner  | STRING        | Nombre de la entidad asociada                |
| amount   | FLOAT (EUR)   | Monto de la transacción expresado en euros   |

---

## 🔄 Mapeos Origen → Canónico

| Origen (CSV) | Campo origen    | Campo canónico | Regla/Transformación                                  |
|--------------|-----------------|----------------|-------------------------------------------------------|
| ventas.csv   | fecha           | date           | Parsear fecha DD/MM/YYYY a YYYY-MM-DD                 |
| ventas.csv   | cliente         | partner        | Copiar valor tal cual                                 |
| ventas.csv   | importe         | amount         | Convertir a float                                     |
| pagos.csv    | transaction_dt  | date           | Parsear timestamp a YYYY-MM-DD                        |
| pagos.csv    | vendor          | partner        | Normalizar a minúsculas                               |
| pagos.csv    | value_usd       | amount         | Convertir USD → EUR con tipo de cambio de referencia  |

