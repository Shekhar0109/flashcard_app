import streamlit as st
from transformers import pipeline

# Initialize text generation pipeline with a lightweight model
@st.cache_resource
def load_generator():
    return pipeline("text-generation", model="sshleifer/tiny-gpt2")

generator = load_generator()

st.title("🧠 Flashcard Generator")
st.write("Enter a concept or topic, and this app will generate a flashcard question based on it.")

# Input box
input_text = st.text_area("Enter a concept/topic:", "")

if st.button("Generate Flashcard"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating flashcard..."):
            result = generator(input_text, max_length=50, num_return_sequences=1)
            flashcard = result[0]["generated_text"]
            st.success("Here's your flashcard:")
            st.write(f"**Q:** {input_text}")
            st.write(f"**A:** {flashcard[len(input_text):].strip()}")
