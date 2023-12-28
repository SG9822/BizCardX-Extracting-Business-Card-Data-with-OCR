import easyocr as ocr
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title='BizCardX', page_icon=':credit_card:', layout='wide')

selected = option_menu(
    menu_title="BizCardX: Extracting Business Card Data with OCR",
    options=["Home", "Dataframe", "Update/Delete"],
    icons=["house", "database-fill", "ubuntu"],
    menu_icon='card-heading',
    default_index=0,
    orientation="horizontal", )

from ocr import dictionary
from edit import edit


def home():
    st.title("Image to Text using EasyOCR")

    image = st.file_uploader(label="Upload Your jpeg/png/jpg Image", type=['png', 'jpg', 'jpeg'])

    with st.spinner("🤖Your Assistant at Work!", cache=True):
        if image is not None:
            input_image = Image.open(image)
            st.markdown('')
            st.markdown('')
            st.markdown('## Your Business Card')
            tab1, tab2, tab = st.columns([1.25, 2, 1])
            with tab2:
                st.image(input_image, width=500)
            reader = ocr.Reader(['en'], model_storage_directory='.')
            result = reader.readtext(np.array(input_image), detail=0)
            result_text = [text for text in result]
            r = dictionary(result_text)
            st.divider()
            edit(r, image)


from edit_del import updateDel
from dataframe import dataFrame

if selected == 'Home':
    home()
elif selected == 'Update/Delete':
    updateDel()
elif selected == "Dataframe":
    dataFrame()
