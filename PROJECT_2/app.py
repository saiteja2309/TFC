import streamlit as st
from matplotlib import image
from PIL import Image
import os
st.title('TASTY FRIED CHICKEN :poultry_leg:')
st.header('T.F.C')
st.subheader('CEO : Dhagad Deepak :sunglasses:')
st.snow()
#FILE_DIR =os.path.dirname(os.path.abspath(__file__))
#PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
#dir_of_interest = os.path.join(PARENT_DIR,'resources')
#image_path = os.path.join(dir_of_interest,'deepak.jpg')
#img=image.imread(image_path)
#st.image(image_path,caption='Dhagad Bholthey :maple_leaf:')
# absolute path to this file
file_directory1 = os.path.dirname(os.path.abspath(__file__))

# absolute path to this file's root directory
parent_directory1 = os.path.join(file_directory1, os.pardir)

# absolute path of directory of interest
dir_of_interest1 = os.path.join(parent_directory1,'PROJECT_2',"resources")

image_path1 = os.path.join(dir_of_interest1,'images',"deepak.jpg")


st.title("Dhagad Bholthey :sunglasses:")

img = image.imread(image_path1)
st.image(img)

#image = Image.open("C:\Users\saite\OneDrive\Desktop\INTERNSHIP  DS\PROJECT_2\resources\deepak.jpg")

#st.image(image, caption='Sunrise by the mountains')
st.header('Avaialable items')
st.caption('1.Fried wings')
st.caption('2.Popcorn')
st.caption('3.Strips')
st.caption('4.Legs')
st.caption('5.Breast')

st.title('IF YOU ARE NOT IN THE MOOD TO EAT,juST')

if st.button('click me'):
    st.title('FUCK me and gimme 100rs')
else:
    st.write('Dont laugh after clicking')

st.balloons()