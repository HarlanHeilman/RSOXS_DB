import streamlit as st
import plotly.graph_objects as go
from PIL import Image

im = Image.open("rsoxs_logo.png")

st.set_page_config(page_title="Test RSOXS Front End", layout="wide", page_icon=im)
st.title("RSOXS Front End")
