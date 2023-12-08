import streamlit as st
import pickle as pkl
from PIL import Image
import numpy as np

st.title('USA college admission rate prediction')

image = Image.open('college admission.jpg')
st.image(image)

input = open('lr_admit.pkl', 'rb')
model = pkl.load(input)

st.header('Input admission information')
gre = 
