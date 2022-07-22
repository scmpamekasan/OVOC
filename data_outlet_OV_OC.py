import streamlit as st
import pandas as pd
import streamlit as st  # pip install streamlit
import streamlit.components.v1 as components
import numpy as np


st.set_page_config(layout="wide")

st.title('DAFTAR OUTLET BELUM OV & OC')

st.markdown("""---""")

df_OC_OV =  pd.read_excel(
            io="Data_CL_OV_OC_Sem2.xlsx",
            engine="openpyxl",
            sheet_name="CL",
            usecols="A:H",
            nrows=20000
            )



df_OC_OV_1 = df_OC_OV.drop(['DSO Name','Daerah','Zona','LastTransaction(OC)'], axis=1)
df_OC_OV_3 = df_OC_OV.drop(['DSO Name','Daerah','Zona','LastVisit(OV)'], axis=1)

df_OC_OV_2 = df_OC_OV_1[df_OC_OV_1['LastVisit(OV)'].isnull()]
df_OC_OV_4 = df_OC_OV_3[df_OC_OV_3['LastTransaction(OC)'].isnull()]




sektor1 = (df_OC_OV_2.loc[:,("Sektor")].drop_duplicates())
list_sektor1 = sektor1.values.tolist()

sektor2 = (df_OC_OV_4.loc[:,("Sektor")].drop_duplicates())
list_sektor2 = sektor2.values.tolist()

Sektor = st.selectbox("Pilih Sektor", list_sektor1)
st.write("Update Per 16 Juli 2022 (data akan diupdate tiap minggu)")

#
col1,col2 = st.columns(2)
with col1 :
    st.subheader ('Outlet Belum ⚽️🅥')
    
    df_selection = df_OC_OV_2.query("Sektor==@Sektor" )
    st.write('Jumlah Outlet Belum Visit=',len(df_selection.index))
    st.write(df_selection)

with col2 :
    st.subheader ('Outlet Belum ⚽️🅲')
 

    df_selection2 = df_OC_OV_4.query("Sektor==@Sektor" )
    st.write('Jumlah Outlet Belum Transaksi=',len(df_selection2.index))
    st.write(df_selection2)
#
