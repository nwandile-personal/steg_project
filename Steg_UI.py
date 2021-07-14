
# #UI
# import os
# from random import randint
# #import io

# #os.chdir('C:/CG/TME/Solutions/My/Steganography')
# import streamlit as st
# import cv2
# #from PIL import Image
# from Steg import encode, decode
# from usersession import get_state

# state = get_state()





# # def get_image_download_link(img,filename,text):
# #     buffered = io.BytesIO()
# #     img.save(buffered, format="JPEG")
# #     img_str = io.base64.b64encode(buffered.getvalue()).decode()
# #     href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
# #     return href


# #Creating Separate Pages
# option = st.sidebar.radio("Go to", ('Encode','Decode'))


# if option == 'Encode':
    
#     st.title("Steganography Encode")
#     if not state.widget_key:
#         state.widget_key = str(randint(1000, 100000000))

#     #key1 = key
#     #key = str(random.randint(10,1000))
#     #key = '0001'
#     uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'], key = state.widget_key)
#     if uploaded_file is not None:
#         file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
#         st.write(file_details)
        
#         with open(os.path.join("input_file_temp.PNG"),"wb") as f: 
#             f.write(uploaded_file.getbuffer())         

#         st.image("input_file_temp.PNG", use_column_width=True, caption = 'This image will be encoded')
#         input_image = uploaded_file.name
#         output_image = "encoded_image.PNG"
        
#         secret_data = st.text_input("Write your secret message", "")
#         #secret_data = input("Enter data to be encoded : ")  
        
#         if st.button('Confirm'):
#             state.widget_key = str(randint(1000, 100000000))
#             encoded_image = encode(image_name=input_image, secret_data=secret_data)
#             cv2.imwrite(output_image, encoded_image)

#             st.write("Encoding.....")
#             st.success("Encoding Complete")
#             os.remove("input_file_temp.PNG")


#             st.image(output_image, use_column_width=True, caption = 'Save This Encoded Image')
            
# if option == 'Decode':    
    
#     st.title("Steganography Decode")
    
#     if not state.widget_key:
#         state.widget_key = str(randint(1000, 100000000))

#     #key1 = key
#     #key = str(random.randint(10,1000))
#     #key = '0001'
#     uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'], key = state.widget_key)
#     # key = '0002'
#     # uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'], key = key)
    
#     if uploaded_file is not None:
#         file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
#         st.write(file_details)
        
        
#         with open(os.path.join("input_file_temp.PNG"),"wb") as f: 
#             f.write(uploaded_file.getbuffer())          
        
        
        
#         st.image("input_file_temp.PNG", use_column_width=True, caption = 'This image will be decoded')
#         output_image = uploaded_file.name
        
        
        
        
#         if st.button('Confirm'):
#             state.widget_key = str(randint(1000, 100000000))
#             st.write("Decoding...")
#             decoded_data = decode(output_image)
#             st.success("Decoding Complete")

#             st.write(decoded_data)
            
        
        
# # if st.button('Decode'):
# #     uploaded_file = st.file_uploader("Choose an image...", type="png")
# #     if uploaded_file is not None:
# #         st.image(uploaded_file, use_column_width="always")
# #         output_image = "encoded_image.PNG"
# #         decoded_data = decode(output_image)
# #         st.text(decoded_data)


###############################################################################

#UI
import os
from random import randint
#import io

os.chdir('C:/CG/TME/Solutions/My/Steganography')
import streamlit as st
import cv2
#from PIL import Image
from Steg import encode, decode
from usersession import get_state
# from PIL import Image
import numpy as np

state = get_state()

option = st.sidebar.radio("Go to", ('Encode','Decode'))

if option == 'Encode':
    
    st.title("Steganography Encode")
    if not state.widget_key:
        state.widget_key = str(randint(1000, 100000000))


    uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg','jpg'], key = state.widget_key)
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)
        
        # with open(uploaded_file.name,'wb') as f:
        #     f.write(uploaded_file.read())

        
        #image = Image.open(uploaded_file)
        #st.image(image, caption='Input', use_column_width=True)
        #img_array = np.array(image)
        #cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))
        
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)


        # with open("input_file_temp.PNG","wb") as f: 
        #     f.write(uploaded_file.getbuffer())         
        
        input_image = opencv_image #uploaded_file.name
        
        st.image(uploaded_file, use_column_width=True, caption = 'This image will be encoded')
        
        output_image = "encoded_image.png"
        
        secret_data = st.text_input("Write your secret message", "")
        #secret_data = input("Enter data to be encoded : ")  
        
        if st.button('Confirm'):
            state.widget_key = str(randint(1000, 100000000))
            encoded_image = encode(input_image, secret_data=secret_data)
            cv2.imwrite(output_image, encoded_image)
            
            
            
            # open_cv_image = np.array(encoded_image) 
            # open_cv_image = open_cv_image[:, :, ::-1].copy() 
           
            
        
            # file_bytes1 = np.asarray(bytearray(encoded_image), dtype=np.uint8)
            # opencv_image1 = cv2.imdecode(encoded_image, 1)            
                

            st.write("Encoding.....")
            st.success("Encoding Complete")
            #os.remove("input_file_temp.PNG")


            st.image(output_image, use_column_width=True, caption = 'Save This Encoded Image')
            
if option == 'Decode':    
    
    st.title("Steganography Decode")
    
    if not state.widget_key:
        state.widget_key = str(randint(1000, 100000000))

    uploaded_file1 = st.file_uploader("Upload Files",type=['png','jpeg'], key = state.widget_key)

    if uploaded_file1 is not None:
        file_details1 = {"FileName":uploaded_file1.name,"FileType":uploaded_file1.type,"FileSize":uploaded_file1.size}
        st.write(file_details1)
        
        # file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        # opencv_image = cv2.imdecode(file_bytes, 1)        
        
        # with open(os.path.join("input_file_temp.PNG"),"wb") as f: 
        #     f.write(uploaded_file.getbuffer())      
        
        file_bytes1 = np.asarray(bytearray(uploaded_file1.read()), dtype=np.uint8)
        opencv_image1 = cv2.imdecode(file_bytes1, 1)
        
        
        
        st.image(uploaded_file1, use_column_width=True, caption = 'This image will be decoded')
        
        
        
        
        
        if st.button('Confirm'):
            state.widget_key = str(randint(1000, 100000000))
            st.write("Decoding...")
            decoded_data = decode(opencv_image1)
            st.success("Decoding Complete")
            st.write(decoded_data)
            
        
        
# if st.button('Decode'):
#     uploaded_file = st.file_uploader("Choose an image...", type="png")
#     if uploaded_file is not None:
#         st.image(uploaded_file, use_column_width="always")
#         output_image = "encoded_image.PNG"
#         decoded_data = decode(output_image)
#         st.text(decoded_data)





