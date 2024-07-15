# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 17:50:45 2024

@author: codyo
"""

import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)