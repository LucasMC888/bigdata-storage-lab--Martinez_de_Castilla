import io
import pandas as pd
import streamlit as st

from src.transform import normalize_columns, to_silver
from src.validate import basic_checks
from src.ingest import tag_lineage, concat_bronze

# ----------------------------
# Configuración básica
# ----------------------------
st.set_page_config(
    page_title="Big Data Storage Lab",
    layout="wide"
)

st.title("📊 Almacén Analítico - Laboratorio")
st.markdown("Transformación de CSVs heterogéneos hacia un modelo confiable.")

# ----------------------------
# Sidebar: configuración
# ----------------------------
st.sidebar.header("Configuración de columnas origen")
date_col = st.sidebar.text_input("Columna origen para 'date'", "fecha")
partner_col = st.sidebar.text_input("Columna origen para 'partner'", "cliente")
amount_col = st.sidebar.text_input("Columna origen para 'amount'", "importe")

mapping = {
    date_col: "date",
    partner_col: "partner",
    amount_col: "amount"
}

# ----------------------------
# Subida de archivos
# ----------------------------
uploaded_files = st.file_uploader(
    "Sube uno o más archivos CSV",
    type=["csv"],
    accept_multiple_files=True
)

bronze_frames = []

if uploaded_files:
    for file in uploaded_files:
        try:
            df = pd.read_csv(file, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding="latin-1")

        # Normalización y linaje
        df_norm = normalize_columns(df, mapping)
        df_tagged = tag_lineage(df_norm, file.name)
        bronze_frames.append(df_tagged)

    # ----------------------------
    # Construcción de bronze unificado
    # ----------------------------
    bronze = concat_bronze(bronze_frames)
    st.subheader("📂 Bronze (unificado)")
    st.dataframe(bronze.head(20))

    # ----------------------------
    # Validaciones
    # ----------------------------
    st.subheader("✅ Validaciones básicas")
    errors = basic_checks(bronze)

    if errors:
        st.error("Se encontraron problemas en los datos:")
        for e in errors:
            st.write(f"- {e}")
    else:
        st.success("Todos los checks básicos pasaron correctamente.")

        # ----------------------------
        # Silver (partner × mes)
        # ----------------------------
        silver = to_silver(bronze)

        st.subheader("📈 Silver (aggregado partner × mes)")
        st.dataframe(silver.head(20))

        # KPIs simples
        total_amount = silver["amount"].sum()
        num_partners = silver["partner"].nunique()

        st.metric("💶 Total Amount (EUR)", f"{total_amount:,.2f}")
        st.metric("👥 Nº de Partners", num_partners)

        # Gráfico de barras: amount por mes
        st.subheader("Gráfico de Amount por Mes")
        chart_data = silver.groupby("month")["amount"].sum().reset_index()
        st.bar_chart(chart_data.set_index("month"))

        # ----------------------------
        # Descargas
        # ----------------------------
        st.subheader("⬇️ Descargas")
        bronze_csv = bronze.to_csv(index=False).encode("utf-8")
        silver_csv = silver.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Descargar Bronze CSV",
            data=bronze_csv,
            file_name="bronze.csv",
            mime="text/csv"
        )

        st.download_button(
            "Descargar Silver CSV",
            data=silver_csv,
            file_name="silver.csv",
            mime="text/csv"
        )
else:
    st.info("Por favor, sube al menos un archivo CSV para comenzar.")
