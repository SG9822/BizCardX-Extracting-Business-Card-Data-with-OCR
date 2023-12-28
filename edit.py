import streamlit as st
import pandas as pd
from sql import sql


def edit(r, image):
    st.markdown('## Your Details Please change the value if it is incorrect ')
    tab3, tab4, tab5 = st.columns([1, 2, 1])
    with tab4:
        tab6, tab7 = st.columns([1.5, 2.5])
        with tab6:
            st.markdown('### Name:')
        with tab7:
            name = st.text_input('Name', value=r['Name'], label_visibility='collapsed')

        tab8, tab9 = st.columns([1.5, 2.5])
        with tab8:
            st.markdown('### Designation:')
        with tab9:
            des = st.text_input("Designation", value=r['Designation'], label_visibility='collapsed')

        tab10, tab11 = st.columns([1.5, 2.5])
        with tab10:
            st.markdown('### Phone Number:')
        with tab11:
            ph = st.text_input("Phone Number", value=r['Phone Number'], label_visibility='collapsed')

        tab12, tab13 = st.columns([1.5, 2.5])
        with tab12:
            st.markdown('### E-Mail:')
        with tab13:
            mail = st.text_input("E-Mail", value=r['E-Mail'], label_visibility='collapsed')

        tab14, tab15 = st.columns([1.5, 2.5])
        with tab14:
            st.markdown('### Address:')
        with tab15:
            addr = st.text_input("Address", value=r['Address'], label_visibility='collapsed')

        tab16, tab17 = st.columns([1.5, 2.5])
        with tab16:
            st.markdown('### Website:')
        with tab17:
            web = st.text_input("Website", value=r['Website'], label_visibility='collapsed')

        tab18, tab19 = st.columns([1.5, 2.5])
        with tab18:
            st.markdown('### Brand:')
        with tab19:
            brand = st.text_input("Brand", value=r['Brand'], label_visibility='collapsed')

        st.markdown('')
        st.markdown('')
        button = st.button('Push to Database')
        if button:
            data = {'Name': name, 'Designation': des, 'Phone Number': ph, 'E-Mail': mail, 'Address': addr, 'Website': web,
                    'Brand': brand, 'Image Name': image.name, 'Image Data': []}
            sql(data, image)

    st.divider()
