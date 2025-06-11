import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from fuzzywuzzy import fuzz

# Download punkt tokenizer for sentence splitting

import nltk
nltk.download('punkt', download_dir='nltk_data')
nltk.data.path.append('nltk_data')


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
            st.subheader("✅ Detected Idioms")
            for entry in detected_idioms:
                st.markdown(f"**Idiom:** *{entry['idiom']}*")
                st.markdown(f"**Meaning:** {entry['meaning']}")
                st.markdown(f"**Sentence:** \"{entry['sentence']}\"")
                st.markdown("---")
        else:
            st.info("No idioms detected.")
