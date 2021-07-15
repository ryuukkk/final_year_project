# Including required python libraries used in this project
import numpy as np
import pandas as pd
import emoji
import np_utils



import tensorflow as tf
from tensorflow import keras
import streamlit as st

# reading train emoji and test emoji data which are attached in the repo
train = pd.read_csv('train_emoji.csv',header=None)
test = pd.read_csv('test_emoji.csv',header=None)

# Creating dictionary for some emoji's, consisting of key - number and value - emoji 
emoji_dict = { 0 : ":heart:", 1 : ":baseball:", 2 : ":smile:", 3 : ":disappointed:", 4 : ":fork_and_knife:"}

st.title("Emojify")
s = st.text_input("Type your sentence: ")
if s!=False:   
    st.write(emoji.emojize(emoji_dict[3]))