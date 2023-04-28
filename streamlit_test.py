import streamlit as st
import subprocess

# Set up the app layout
st.set_page_config(page_title="EDUMIZE", page_icon=":books:")
st.title("DOSA Multilingual IDE")
st.header("By Logic Dosa\n")

def open_file(url):
    with open(url, "r") as file:
        file_contents = file.read()
    return file_contents

def open_file1(text):
    with open(text, 'r') as file:
        file_contents = file.read()
    return file_contents

st.markdown("Welcome to EDUMIZE, an educational app that provides various tools for learning.")

menu = ["Python IDE", "Julia IDE"]
choice = st.sidebar.selectbox("Select a tool:", menu)

if choice == "Python IDE":
    st.subheader("Visual Learning")
    if st.button("Run Visualization"):
        subprocess.run(["python", "graphviz_ast1.py"])
if choice == "Julia IDE":
    st.subheader("Not Built yet")
    
