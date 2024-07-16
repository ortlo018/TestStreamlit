# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 17:50:45 2024

@author: codyo
"""

import streamlit as st
import random

# Create an input box to enter a number
input_number = st.number_input("Enter a number", min_value=0, value=10, step=1)

# Generate a random number between the input number and 0
random_number = random.uniform(0, input_number)

# Display the result
st.write("Random number between 0 and", input_number, "is", random_number)
