# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:57:25 2021

@author: nwandile
"""

#UI
import os
from random import randint
from io import BytesIO
import base64

os.chdir('C:/CG/TME/Solutions/My/Steganography')
import streamlit as st
import cv2
from PIL import Image
from Steg import encode, decode
from usersession import get_state
import numpy as np

state = get_state()

def get_image_download_link(img,filename,text):
    buffered = BytesIO()
    img.save(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href



#Creating Separate Pages
option = st.sidebar.radio("Go to", ('Encode','Decode'))


if option == 'Encode':
    
    st.title("Steganography Encode")
    if not state.widget_key:
        state.widget_key = str(randint(1000, 100000000))

    #key1 = key
    #key = str(random.randint(10,1000))
    #key = '0001'
    uploaded_file = st.file_uploader("Upload Files",type=['jpeg'], key = state.widget_key)
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)
    
    
    
    # if uploaded_file is not None:
        st.image(uploaded_file, use_column_width=True, caption = 'This image will be encoded')
        input_image = uploaded_file.name
        output_image = "encoded_image.PNG"
        
        secret_data = st.text_input("Write your secret message", "")
        #secret_data = input("Enter data to be encoded : ")  
        
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        
        if st.button('Confirm'):
            state.widget_key = str(randint(1000, 100000000))
            encoded_image = encode(image_name=opencv_image, secret_data=secret_data)
            cv2.imwrite(output_image, encoded_image)
            st.write("Encoding.....")
            st.write("Encoding Complete")
            
            oo = Image.open(output_image)
            st.image(oo, use_column_width=True, caption = "Save",output_format="PNG")
            #st.markdown(get_image_download_link(oo,"output_image",'Download output_image'), unsafe_allow_html=True)
            #state.sync()
            
if option == 'Decode':    
    
    st.title("Steganography Decode")
    
    if not state.widget_key:
        state.widget_key = str(randint(1000, 100000000))

    #key1 = key
    #key = str(random.randint(10,1000))
    #key = '0001'
    uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'], key = state.widget_key)
    # key = '0002'
    # uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'], key = key)
    
    
    
    
    
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)
        st.image(uploaded_file, use_column_width=True, caption = 'This image will be decoded')
        output_image = uploaded_file.name
        
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)        
        
        
        if st.button('Confirm'):
            state.widget_key = str(randint(1000, 100000000))
            st.write("Decoding...")
            decoded_data = decode(opencv_image)
            st.write("Decoding Complete")
            st.write(decoded_data)
            
        
        
# if st.button('Decode'):
#     uploaded_file = st.file_uploader("Choose an image...", type="png")
#     if uploaded_file is not None:
#         st.image(uploaded_file, use_column_width="always")
#         output_image = "encoded_image.PNG"
#         decoded_data = decode(output_image)
#         st.text(decoded_data)



