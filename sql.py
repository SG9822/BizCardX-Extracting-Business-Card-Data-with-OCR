import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote
import streamlit as st
import pymysql
import mysql.connector


def sql(data, image):
    user = 'root'
    password = quote('MySQL@123')
    host = '127.0.0.1'
    port = 3306
    database = 'image_processing'

    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')
    try:
        myconnection = pymysql.connect(host='127.0.0.1', user='root', passwd='MySQL@123')
        cur = myconnection.cursor()
        cur.execute('create database image_processing')

        myconnection = pymysql.connect(host='127.0.0.1', user='root', passwd='MySQL@123', database='Youtube_Data')
        cursor = myconnection.cursor()
        cursor.execute('use image_processing')

        return st.warning("Please again migrate the channel")
    except:
        try:
            sql_names = pd.read_sql_query("select Name, Brand from images", engine)
            sql_names_list = list(sql_names['Name'])
            sql_brand_list = list(sql_names['Brand'])
            if data['Name'] in sql_names_list:
                st.warning(f"##### This Business card name **{data['Name']}** is already in Database If you want to update or delete go to `update/delete` page")
            elif data['Brand'] in sql_brand_list:
                st.warning(
                    f"##### This Business card name **{data['Brand']}** is already in Database If you want to update or delete go to `update/delete` page")
            else:
                images = image.read()
                data['Image Data'].append(images)
                data = pd.DataFrame(data, index=[1])
                data.to_sql('images', con=engine, if_exists='append', index=False)
                st.balloons()
                st.success("Uploaded into Database")

        except:
            st.warning("Image error")
