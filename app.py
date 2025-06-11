import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from fuzzywuzzy import fuzz

# Download punkt tokenizer for sentence splitting
nltk.download('punkt')

# --- Custom Streamlit Styling ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
    }
    .stTextArea textarea {
        background-color: #f7fafc !important;
        border-radius: 10px !important;
        border: 1.5px solid #b6c9e2 !important;
        font-size: 1.1rem !important;
        color: #22223b !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #48c6ef 0%, #6f86d6 100%);
        color: white;
        border-radius: 8px;
        border: none;
        font-size: 1.1rem;
        padding: 0.5em 2em;
        margin-top: 10px;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #6f86d6 0%, #48c6ef 100%);
        color: #fff;
        transform: scale(1.03);
    }
    .stMarkdown h3 {
        color: #2d3142;
        margin-top: 1.5em;
    }
    .stMarkdown ul {
        background: #f0f4f8;
        border-radius: 8px;
        padding: 1em;
        margin-bottom: 1em;
        box-shadow: 0 2px 8px rgba(100, 100, 150, 0.07);
    }
    </style>
""", unsafe_allow_html=True)

# Load idioms CSV file
try:
    df_idioms = pd.read_csv('english_idioms 2.csv', encoding='latin-1')
except FileNotFoundError:
    st.error("Make sure 'english_idioms 2.csv' exists in the same directory and has 'idioms' and 'meaning' columns.")
    st.stop()

# Preprocess idioms
df_idioms['idioms'] = df_idioms['idioms'].str.lower()
idiom_dict = dict(zip(df_idioms['idioms'], df_idioms['meaning']))

# Streamlit UI
st.title("🧠 Idiom Detector")
st.write("Enter a paragraph below. The app will detect and explain any idioms used.")

# Text Input
input_text = st.text_area("Input Paragraph", height=200)

# Detect Idioms
if st.button("Detect Idioms"):
    if not input_text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        sentences = sent_tokenize(input_text)
        detected_idioms = []

        for sentence in sentences:
            for idiom in idiom_dict:
                similarity = fuzz.partial_ratio(idiom, sentence.lower())
                if similarity > 85:
                    detected_idioms.append({
                        "idiom": idiom,
                        "meaning": idiom_dict[idiom],
                        "sentence": sentence
                    })

        if detected_idioms:
            st.markdown("### ✅ Detected Idioms")
            for entry in detected_idioms:
                st.markdown(f"""
                <div style="background-color:#1e1e1e; color:white; padding:15px; border-radius:10px; margin-bottom:10px; font-size:16px;">
                    <b>Idiom:</b> <i>{entry['idiom']}</i><br>
                    <b>Meaning:</b> {entry['meaning']}<br>
                    <b>Sentence:</b> "{entry['sentence']}"
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No idioms detected.")
