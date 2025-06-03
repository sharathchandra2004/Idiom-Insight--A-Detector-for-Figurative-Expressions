# 💬 Idiom Insight – A Detector for Figurative Expressions

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![NLP](https://img.shields.io/badge/NLP-Figurative_Expressions-purple)

> 🧠 A smart NLP-powered tool to detect idiomatic and figurative expressions from user-provided text, with real-time explanations. Built with Streamlit.

---

## ✨ Project Overview

**Idiom Insight** allows users to input a paragraph and intelligently identifies idioms (figurative expressions), explains their meaning, and highlights the sentence in which they appear.

💡 Useful for:
- 🧑‍🏫 Teachers
- 🧑‍🎓 Language Learners
- 🤖 NLP Explorers
- ✍️ Writers & Editors

---

## 📸 Demo Preview

<img src="https://raw.githubusercontent.com/sharathchandra2004/Idiom-Insight--A-Detector-for-Figurative-Expressions/main/demo.gif" width="800">

---

## 🧠 How It Works

1. Text is split into sentences using **NLTK**.
2. Each sentence is compared against a dataset of idioms using **FuzzyWuzzy’s partial ratio**.
3. Idioms with similarity scores > 85% are flagged.
4. Streamlit displays:
   - ✅ Detected idiom
   - 💡 Meaning
   - 📌 Sentence in which it appears

---

## 🛠 Tech Stack

| Tool         | Purpose                              |
|--------------|--------------------------------------|
| Python       | Main programming language            |
| Streamlit    | Web app framework                    |
| NLTK         | Sentence tokenization                |
| FuzzyWuzzy   | Fuzzy string matching (idiom detection) |
| Pandas       | Data handling                        |

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/sharathchandra2004/Idiom-Insight--A-Detector-for-Figurative-Expressions.git
cd Idiom-Insight--A-Detector-for-Figurative-Expressions

# Install required packages
pip install -r requirements.txt

# Run the app
streamlit run app.py
