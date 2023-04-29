import streamlit as st
import subprocess
import openai

# Set up the app layout
st.set_page_config(page_title="EDUMIZE", page_icon=":books:")
st.title("DOSA Multilingual IDE")
st.header("By Logic Dosa\n")

# Set up OpenAI API key
openai.api_key = "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"
model = "text-davinci-002"


def open_file(url):
    with open(url, "r") as file:
        file_contents = file.read()
    return file_contents

def open_file1(text):
    with open(text, 'r') as file:
        file_contents = file.read()
    return file_contents

# Set up app menu
st.markdown("DOSA - Multilungual IDE for 'Python' & 'Julia' ")
menu = ["Python IDE", "Julia IDE"]
choice = st.sidebar.selectbox("Select a tool:", menu)

if choice == "Python IDE":
    st.subheader("Visual Learning")
    if st.button("Run Visualization"):
        subprocess.run(["python", "graphviz_ast1.py"])
    if st.button("Give Prompt"):
        st.markdown("---")
        prompt = st.text_area("Enter your prompt here", height=150)
        st.markdown("---")
        if st.button("Generate Output"):
            model = model
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=1000,
            )
            generated_text = response.choices[0].text
            st.markdown("---")
            st.subheader("Generated Output:")
            st.code(generated_text, language='python')

if choice == "Julia IDE":
    st.subheader("Not Built yet")
