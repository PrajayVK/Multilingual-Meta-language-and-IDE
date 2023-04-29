import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Set up Streamlit app
st.title("OpenAI API Example")
prompt = st.text_area("Enter your prompt here")

# Make API request
if st.button("Generate text"):
    model = "text-davinci-002"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1000,
    )
    generated_text = response.choices[0].text
    st.write("Generated text:")
    st.text(generated_text)
