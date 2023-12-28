import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote
import streamlit as st


# st.set_page_config(layout='wide')

user = 'root'
password = quote('MySQL@123')
host = '127.0.0.1'
port = 3306
database = 'image_processing'

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')
my_db = engine.connect()


def update():

    tab3, tab4, tab5 = st.columns([1, 2, 1])
    with tab4:
        tab6, tab7 = st.columns([1.5, 2.5])
        with tab6:
            st.markdown('### Name:')
        with tab7:
            name = [st.text_input('Name', label_visibility='collapsed', key='name'), 'Name']

        tab8, tab9 = st.columns([1.5, 2.5])
        with tab8:
            st.markdown('### Designation:')
        with tab9:
            desc = [st.text_input("Designation", label_visibility='collapsed', key='desc'), 'Designation']

        tab10, tab11 = st.columns([1.5, 2.5])
        with tab10:
            st.markdown('### Phone Number:')
        with tab11:
            phn = [st.text_input("Phone Number", label_visibility='collapsed', key='phn'), '`Phone Number`']

        tab12, tab13 = st.columns([1.5, 2.5])
        with tab12:
            st.markdown('### E-Mail:')
        with tab13:
            email = [st.text_input("E-Mail", label_visibility='collapsed', key='email'), '`E-Mail`']

        tab14, tab15 = st.columns([1.5, 2.5])
        with tab14:
            st.markdown('### Address:')
        with tab15:
            addrs = [st.text_input("Address", label_visibility='collapsed', key='addrs'), 'Address']

        tab16, tab17 = st.columns([1.5, 2.5])
        with tab16:
            st.markdown('### Website:')
        with tab17:
            website = [st.text_input("Website", label_visibility='collapsed', key='website'), 'Website']

        tab18, tab19 = st.columns([1.5, 2.5])
        with tab18:
            st.markdown('### Brand:')
        with tab19:
            brand = [st.text_input("Brand", label_visibility='collapsed', key='brand'), 'Brand']

        st.markdown('')
        st.markdown('')
        return [desc, phn, email, addrs, website, brand, name]


def updateDel():
    st.header("Want to Update or Delete Data")

    st.write("### Please Enter the card name you want to `Update` or `Delete` (refer the Dataframe for `Name`)")
    radio = st.radio("Update/Delete:", ["Updating in Dataframe", "Deleting in Dataframe"], horizontal=True)
    if radio == 'Updating in Dataframe':
        st.markdown('#### 🧿Update the Details here')
        card_name = st.text_input('Card holder Name for updating', key='input')
        st.write('### Fill the Column(s) You want to update')
        up = update()
        col1, col2 = st.columns([1.75, 2.25])
        with col2:
            button = st.button('Update In Database')

        if button and len(card_name) > 0:
            sql_name = pd.read_sql_query("select Name from images", engine)
            sql_name_list = list(sql_name['Name'])
            if card_name not in sql_name_list:
                st.warning(f"The name {card_name} is not in Database, Please check your Spelling.")
            else:
                my_db.execute(text('SET SQL_SAFE_UPDATES = 0'))
                my_db.commit()
                for col in up:
                    if len(col[0]) > 0:
                        my_db.execute(text(f"update images set {col[1]} = '{col[0]}' where Name = '{card_name}'"))
                        my_db.commit()
                    else:
                        continue
                my_db.execute(text('SET SQL_SAFE_UPDATES = 1'))
                my_db.commit()
                st.success("Updated in Database")

        elif button and len(card_name) == 0:
            st.warning("Card holder Name is Compulsory")

        st.divider()
    elif radio == "Deleting in Dataframe":
        st.markdown('#### 🧿Delete Details here')
        st.write("### Warning: If you hit the `Delete from Database` button, it will `permanently delete` the data from database")
        card_name_delete = st.text_input('Card holder Name for deleting', key='del')
        del_button = st.button('Delete from Database')
        if del_button and len(card_name_delete) > 0:
            sql_name = pd.read_sql_query("select Name from images", engine)
            sql_name_list = list(sql_name['Name'])
            if card_name_delete not in sql_name_list:
                st.warning(f"The name {card_name_delete} is not in Database, Please check your Spelling.")
            else:
                my_db.execute(text('SET SQL_SAFE_UPDATES = 0'))
                my_db.commit()
                my_db.execute(text(f"delete from images where Name = '{card_name_delete}'"))
                my_db.commit()
                my_db.execute(text('SET SQL_SAFE_UPDATES = 1'))
                my_db.commit()
                st.success("Deleted in Database")
        elif del_button and len(card_name_delete) == 0:
            st.warning("Please enter Card Name")
        st.divider()

# updateDel()
