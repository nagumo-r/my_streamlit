import streamlit as st
from multiapp import MultiApp
from apps import main, data_stats

app = MultiApp() 

app.add_app("Home", main.app)
app.add_app("Data Stats", data_stats.app) 

app.run()
