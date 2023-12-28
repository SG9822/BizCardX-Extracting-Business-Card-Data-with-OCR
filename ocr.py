import easyocr as ocr
import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import re


def dictionary(result_text):
    dictionary = {'Name': '', 'Designation': '', 'Phone Number': [], 'E-Mail': '', 'Address': '', 'Website': '', 'Brand': ''}

    ph = []
    mail = []
    addr = []
    web = []
    brand = []

    result_text_copy = result_text.copy()

    # img = input_image
    name = result_text[0]
    result_text_copy.remove(result_text[0])
    des = result_text[1].title()
    result_text_copy.remove(result_text[1])

    for detail in result_text[2:]:
        if re.search(r'\b\d{2,}-\d{3}-\d{4}|[+]\d{2,}-\d{3}-\d{4}|[+]\d{2,} \d{3} \d{4}|\d{2,} \d{3} \d{4}|[+] \d{10}|[+]-\d{10}|\d{10}\b', detail):
            ph.append(detail)
            result_text_copy.remove(detail)
        if re.search(r'\b[A-Za-z0-9.-_+%]+@[A-Za-z0-9+-/?=%]+\.com|\.in\b', detail) or re.search(
                r'[A-Za-z0-9.-_+%]+@[a-zA-Z0-9]+ com| in', detail):
            mail.append(re.sub(' ,', ',', detail))
            result_text_copy.remove(detail)

        pattern_1 = re.compile(r'\b\d+\s+(?:[A-Za-z]+\s*,?\s*)+([A-Za-z]+)\s*,?\s*([A-Za-z]+)\b', re.IGNORECASE)
        pattern_2 = re.compile(r'\b\d+\s+(?:[A-Za-z]+\s*,?\s*)+([A-Za-z]+)\s*,?\s*([A-Za-z]+),\s*(\d{6})\b',
                               re.IGNORECASE)
        pattern_3 = re.compile(
            r'\b([A-Za-z]*\s*(Address|address|street|Street)\s*[A-Za-z]*)|([A-Za-z]*\s*(Address|addressstreet|Street)\s*[A-Za-z]*)(\d{6})\b',
            re.IGNORECASE)
        if pattern_1.search(detail) or pattern_2.search(detail) or pattern_3.search(detail):
            addr.append(re.sub(r'(\d+)\s*([A-Za-z]+)', r'\1, \2', detail))
            result_text_copy.remove(detail)

        if re.fullmatch(r'St ,|st ,|St,|st,|Street,|street,|Street ,|street ,', detail):
            addr.insert(1, detail)
            result_text_copy.remove(detail)

        if re.search(r'\b[A-Za-z] [0-9]{6}|\d{6}\b', detail):
            addr.append(re.sub(' ', ', ', detail))
            result_text_copy.remove(detail)

        if re.search(r'(WWW|WWW.|www|www.|[A-Za-z0-9]+\.com|.in|\.com)', detail):
            if '@' in detail:
                continue
            else:
                web.append(re.sub(r'([A-Za-z0-9]+)(com)', r'\1.\2', detail))
                result_text_copy.remove(detail)

    for alpha in result_text_copy:

        pattern = re.compile(r'[A-Za-z]+,')
        if pattern.fullmatch(alpha):
            addr.insert(-1, alpha)
            result_text_copy.remove(alpha)
    brand.append(' '.join(result_text_copy))

    dictionary['Name'] = name.title()
    dictionary['Designation'] = des
    dictionary['Phone Number'] = ', '.join(ph)
    dictionary['E-Mail'] = ' '.join(mail).replace(',', '.').replace(';', '.').strip().lower()
    dictionary['Website'] = ' '.join(web).replace(' ', '.').lower()
    dictionary['Address'] = ' '.join(addr).replace(';', ',').replace(' ,', ',').replace(',,', ',').strip().title()
    dictionary['Brand'] = ' '.join(brand).title()

    print(dictionary)
    return dictionary


